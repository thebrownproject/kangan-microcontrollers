from machine import Pin, ADC
import time, network, dht, json
from umqtt.simple import MQTTClient

# ---------- Wi-Fi ----------
WIFI_SSID = "CyFi"
WIFI_PASS = "SecurityA40"

# ---------- Wi-Fi connect ----------
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASS)
while not wlan.isconnected():
    time.sleep(0.2)
print("Wi-Fi connected:", wlan.ifconfig())

# ---------- MQTT (HiveMQ Cloud) ----------
CLIENT_ID     = "pico-" + str(time.ticks_cpu() & 0xffff)
MQTT_BROKER   = "301d2478bf674954a8b8e5ad05732a73.s1.eu.hivemq.cloud"
MQTT_PORT     = 8883
MQTT_USER     = "thebrownproject"
MQTT_PASS     = "StrongPassword123!"

TOPIC_SUB        = b"museum/zone1/cmd"
TOPIC_PUB_EVENT  = b"museum/zone1/event"
TOPIC_PUB_STATE  = b"museum/zone1/state"

# ---------- MQTT connect ----------
client = MQTTClient(
    CLIENT_ID,
    MQTT_BROKER,
    port=MQTT_PORT,
    user=MQTT_USER,
    password=MQTT_PASS,
    ssl=True,    # TLS encryption
    ssl_params={"server_hostname":MQTT_BROKER}
)

try:
    client.connect()
    print("Connected to HiveMQ Broker")
except Exception as e:
    print("MQTT connection failed:", e)

# ---------- Hardware ----------
pir = ADC(Pin(26))  # PIR sensor
led = Pin(2, Pin.OUT)  # LED

# ---------- Global State Variables ----------
ALARM_ARM = False
MUTED = False
ALARM_TRIGGERED = False  # Persistent alarm state

# ---------- Callback for subscriptions ----------
def sub_callback(topic, msg):
    global ALARM_ARM, MUTED, ALARM_TRIGGERED  # Declare globals
    print("Message received on topic:", topic, msg)
    if msg == b"ARM":
        print("System armed")
        ALARM_ARM = True
        ALARM_TRIGGERED = False
    elif msg == b"DISARM":
        print("System disarmed - alarm reset")
        ALARM_ARM = False
        ALARM_TRIGGERED = False  # Reset alarm when disarmed
    elif msg == b"MUTE":
        print("System muted")
        MUTED = True
    elif msg == b"UNMUTE":
        print("System unmuted")
        MUTED = False

client.set_callback(sub_callback)
client.subscribe(TOPIC_SUB)


while True:
    client.check_msg()
    sensor_value = pir.read_u16()
    
    # Trigger alarm on motion detection
    if ALARM_ARM and not ALARM_TRIGGERED and sensor_value > 10000:
        ALARM_TRIGGERED = True
        print("Alarm triggered")
        client.publish(TOPIC_PUB_EVENT, json.dumps({"event": "alarm_triggered"}))
    
    # Control LED based on alarm state
    if ALARM_TRIGGERED and not MUTED:
        led.on()
    else:
        led.off()
    
    # Publish system state
    state_data = {"armed": ALARM_ARM, "muted": MUTED, "alarm_triggered": ALARM_TRIGGERED}
    client.publish(TOPIC_PUB_STATE, json.dumps(state_data))
    print("System state published:", state_data)

    time.sleep(3)