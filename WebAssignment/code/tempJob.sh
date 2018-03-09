#!/bin/sh
echo $(date) >> bash_cron_log.txt
/usr/bin/python /home/pi/EL_Projects/ELSpring2018/WebAssignment/code/tempDB.py >> bash_cron_log.txt
