import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import datetime
import logging

def persists(msg):
    current_time = datetime.datetime.utcnow().isoformat()
    json_body = [
        {
            "measurement": "pot",
            "tags": {},
            "time": current_time,
            "fields": {
                "value": float(msg.payload)
            }
        }
    ]
    print(json_body)
    logging.info(json_body)
    myresult = influx_client.write_points(json_body)

print ("attaching to influx")
logging.basicConfig(level=logging.INFO)

try:
    influx_client = InfluxDBClient(host='influxdb', port=8086, database='iot', username='gatherer', password='password')
except:
    print("cannot connect to influx");

client = mqtt.Client(client_id="com.brobasino.python-listener", clean_session=False)

client.on_connect = lambda self, mosq, obj, rc: self.subscribe("/pot", 1)
client.on_message = lambda client, userdata, msg: persists(msg)

print ("attaching to mqtt")
client.connect("mosquitto", 1883, 60)

client.loop_forever()
