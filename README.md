# redborder-sflow2kafka

Systemd unit that runs [x2kafka](https://github.com/redBorder/x2kafka) as the `sflow2kafka` service (sflow collector, UDP 6343).

The configuration (`/etc/sflow2kafka/config.json`) is rendered by Chef.
