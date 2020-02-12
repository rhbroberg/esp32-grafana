import os
import datetime
import logging
import paho.mqtt.client
from influxdb import InfluxDBClient

CLIENT_ID = os.getenv('CLIENT_ID', 'python-listener-bridge')
SUBSCRIPTION = os.getenv('SUBSCRIPTION', '/sensors/+/#')
QOS = os.getenv('QOS', 0)

def persists(message):
    current_time = datetime.datetime.utcnow().isoformat()
    json_body = [
        {
            "measurement": message.topic,
            "tags": {},
            "time": current_time,
            "fields": {
                "value": float(message.payload)
            }
        }
    ]
    logging.info(json_body)
    myresult = influx_client.write_points(json_body)
    logging.info(myresult)

logging.basicConfig(level=logging.INFO)

try:
    logging.info("attaching to influx")
    influx_client = InfluxDBClient(host='influxdb', port=8086, database='iot', username='gatherer', password='password')
except:
    logging.info("cannot connect to influx")

client = paho.mqtt.client.Client(client_id=CLIENT_ID, clean_session=False)

client.on_connect = lambda self, mosq, obj, rc: self.subscribe(SUBSCRIPTION, QOS)
client.on_message = lambda client, userdata, message: persists(message)

logging.info("attaching to mqtt")
client.connect("mosquitto", 1883, 60)

client.loop_forever()
