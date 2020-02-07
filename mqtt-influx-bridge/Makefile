mqtt-influx-bridge:	requirements.txt listener.py Dockerfile
	. venv/bin/activate && docker build -t mqtt-influx-bridge .

venv:
	pip3 install virtualenv
	virtualenv -p /usr/bin/python3 venv

requirements.txt:	venv listener.py
	. venv/bin/activate && pip install paho-mqtt influxdb
	. venv/bin/activate && pip uninstall pkg-resources==0.0.0
	. venv/bin/activate && pip freeze > requirements.txt
