import mip
import network
import time

ssid = "CyFi"
password = "SecurityA40"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    print("Connecting...")
    time.sleep(1)

print("Connected!", station.ifconfig())

# Install basic MQTT client
mip.install("umqtt.simple")

# Install robust MQTT client (auto reconnect if Wi-Fi drops)
mip.install("umqtt.robust")