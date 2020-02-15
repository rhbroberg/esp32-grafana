prototype mqtt=>influxdb=>grafana docker configuration.

This is a self-contained docker project which launches a mqtt server that stores all topic data from the topic '/sensors/+/#' in an InfluxDB.
In addition to the mosquitto image, influxdb, and bridge (which listens to that topic and writes to the database), there are some monitoring images as well.
Those are: grafana, prometheus, node-exporter, cadvisor, mosquitto-exporter.  The grafana image is pre-populated with 5 dashboards which allows you to monitor system performance.

* Build the mqtt-influxdb-bridge docker image first.  Only tested on ubuntu/18.04 and osx so far.  Uses python/3, pip3, and virtualenv - make sure they're installed first.
Then
  cd mqtt-influx-bridge && make

* For now, prometheus.yml static_configs first target must match the name of your Docker host.  For DockerDesktop, the current value works; on Linux Docker, replace it with your host's hostname

* For the docker monitoring dashboard to be complete, add the 'metrics-addr' to /etc/docker/daemon.json on Linux, or the Docker Engine on osx (see https://docs.docker.com/config/thirdparty/prometheus/)
  My example uses 'ubuntu-18-04-04'.  You need to use 'localhost' on DockerDesktop, or your host's hostname on Linux.  Restart your Docker service for the change to take effect

  "metrics-addr" : "ubuntu-18-04-04:9323",
  "experimental" : true

* unsurprisingly, all of the monitoring is substantially more heavyweight than the actual basic service mqtt=>bridge=>influxdb.  cadvisor is the biggest one

* start it up with
  docker-compose up -d

* the grafana webpage is reachable at http://localhost:3000.   default username/password is admin/admin

* any float-based values to the defined topic which are posted via localhost:1883 (or hostname:1883) will auto-populate into the influxdb.  these are viewable in the grafana 'explore' pane

* if you post floats to /sensors/proto/temperature, the 'esp32 dashboard' dashboard example will show the plot

