import time, network, dht, json
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

try:
    client.connect()
    print("Connected to HiveMQ Broker")
except Exception as e:
    print("MQTT connection failed:", e)

# ---------- Hardware ----------
DHT = dht.DHT11(Pin(16))

# ---------- Main Loop with Real-time Data ----------
while True:
    try:
        # Read fresh sensor data
        DHT.measure()
        temperature = DHT.temperature()
        humidity = DHT.humidity()
        
        # Create JSON formatted messages
        temp_data = {"temperature": temperature,}
        hum_data = {"humidity": humidity}
        export_data = json.dumps({"temperature": temperature, "humidity": humidity})

        # Publish sensor data
        client.publish(TOPIC_PUB, export_data)
        print(f"Published: {export_data}")

    except Exception as e:
        print("Sensor or publish error:", e)
    
    time.sleep(10)