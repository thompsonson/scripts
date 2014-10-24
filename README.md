scripts
=======

Place to keep odds and sods

rsnapshot-influxdb.pl
=======

I use this script with rsnapshot backups, the json is produces is picked up by NodeRed and posted to InfluxDB. Here's the crontab setup:

    # m h  dom mon dow   command
    0     */4         *         *         *         /usr/bin/rsnapshot hourly 2>&1 | /home/user/bin/rsnapshot-influxdb.pl > /home/user/rsnapshot/log/rsnapreport.json
    30    2           *         *         *         /usr/bin/rsnapshot daily 2>&1 |     /home/user/bin/rsnapshot-influxdb.pl > /home/user/rsnapshot/log/rsnapreport.json
    30    3           *         *         1         /usr/bin/rsnapshot weekly 2>&1 | /home/user/bin/rsnapshot-influxdb.pl > /home/user/rsnapshot/log/rsnapreport.json
    30    4           1         *         *         /usr/bin/rsnapshot monthly 2>&1 | /home/user/bin/rsnapshot-influxdb.pl > /home/user/rsnapshot/log/rsnapreport.json


