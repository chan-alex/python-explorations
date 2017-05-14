#!/usr/bin/env python

"""
Simple script to demo one way to run an external command and timing it.

"""


import sys
import time
import subprocess

print "start"
cmd = sys.argv[1]

print "cmd = " + cmd

start_time =  time.time()
error_code = subprocess.call(cmd, shell=True)
end_time =  time.time()


elapsed_time = round(end_time - start_time, 2)
start_time_asc =  time.asctime(time.localtime(time.time()))
end_time_asc =  time.asctime(time.localtime(time.time()))

print "error_code is:  {}".format(error_code)
print "Start time is: {}".format(start_time_asc)
print "End time is: {}".format(end_time_asc)
print "Elasped time in seconds: {}".format(elapsed_time)
