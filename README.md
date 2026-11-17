# redborder-sflow2kafka

Systemd unit that runs [x2kafka](https://github.com/redBorder/x2kafka) as the `sflow2kafka` service (sflow collector, UDP 6343).

The configuration (`/etc/sflow2kafka/config.json`) is rendered by Chef.

It replaces the legacy `sfacctd.service` of the `pmacct` package, which stays installed because `rb-exporter` needs its `pmacctd`. Since the unit has a different name, `sfacctd.service` must be kept disabled/stopped so both don't bind UDP 6343.
