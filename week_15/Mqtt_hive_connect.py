import network, time, ssl
from machine import Pin
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

TOPIC_SUB     = b"pico/led"
TOPIC_PUB     = b"pico/status"

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
print("Connected to HiveMQ Broker")

# ---------- Hardware ----------
led = Pin("LED", Pin.OUT)

# ---------- Callback for subscriptions ----------
def sub_cb(topic, msg):
    print("MQTT Message:", topic, msg)
    if msg == b"ON":
        led.value(1)
        client.publish(TOPIC_PUB, b"LED is ON")
    elif msg == b"OFF":
        led.value(0)
        client.publish(TOPIC_PUB, b"LED is OFF")

client.set_callback(sub_cb)
client.connect()
client.subscribe(TOPIC_SUB)

# ---------- Main loop ----------
while True:
    client.check_msg()  # Non-blocking, listens for messages
    time.sleep(1)
    