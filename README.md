prototype mqtt=>influxdb=>grafana docker configuration.

Build the mqtt-influxdb-bridge docker image first.  Only tested on ubuntu/18.04 so far.  Uses python/3

* For the docker monitoring, add the following to /etc/docker/daemon.json

  "metrics-addr" : "ubuntu-18-04-04:9323",
  "experimental" : true

(and restart docker service)

* it's probably time to investigate telegraph instead; has plugins for docker and influxdb 

* docker-dashboard.yml is a slightly updated version of an existing file which was stale wrt upstream docker name changes

* unsurprisingly, all of the monitoring is substantially more heavyweight than the actual basic service

todo:
* have make target retrieve newer grafana dashboards
* have 2 docker-compose.yml files - 1 with the monitoring, 1 without
