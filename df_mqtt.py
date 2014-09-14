import paho.mqtt.client as mosquitto
import os, json, socket

# config
topic = "/data/sysmon/" + socket.gethostname() + "/os/df"
hostname = "localhost"
port = 1883
client_id = "df_python_script"

# connect to broker
mosquittoClient = mosquitto.Mosquitto(client_id)
mosquittoClient.connect(hostname, port)

# process the data
data = [s.split() for s in os.popen("df -P").read().splitlines()]

#remove the header
del data[0]

for item in data:
        dict = {'Filesystem':item[0], 'Size':item[1], 'Used':item[2], 'Avail':item[3], 'Use_pc':item[4].replace("%",""), 'Mounted':item[5]}
        # publish it on the broker
        mosquittoClient.publish(topic,json.dumps(dict))

mosquittoClient.disconnect()
