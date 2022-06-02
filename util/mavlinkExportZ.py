#!/usr/bin/env python

'''
estimate attitude from an ArduPilot replay log using a python state estimator
'''
from __future__ import print_function
from builtins import range

import os

from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("log", metavar="LOG")
parser.add_argument("--debug", action='store_true')

args = parser.parse_args()

from pymavlink import mavutil
from pymavlink.rotmat import Vector3, Matrix3
from math import degrees
import datetime

GRAVITY_MSS = 9.80665

AP_NSEC_PER_SEC  = 1000000000
AP_NSEC_PER_USEC = 1000
AP_USEC_PER_SEC  = 1000000
AP_USEC_PER_MSEC = 1000
AP_MSEC_PER_SEC  = 1000
AP_SEC_PER_HOUR  = (3600)
AP_MSEC_PER_HOUR = (AP_SEC_PER_HOUR * AP_MSEC_PER_SEC)
AP_SEC_PER_WEEK  = (7 * 86400)
AP_MSEC_PER_WEEK = (AP_SEC_PER_WEEK * AP_MSEC_PER_SEC)
GPS_LEAPSECONDS_MILLIS = 18000
UNIX_OFFSET_MSEC = (17000 * 86400 + 52 * 10 * AP_MSEC_PER_WEEK - GPS_LEAPSECONDS_MILLIS)

def weeksecondstoutc(gps_week, gps_ms):
    return UNIX_OFFSET_MSEC + gps_week * AP_MSEC_PER_WEEK + gps_ms

def estimate(filename):
    '''run estimator over a replay log'''
    print("Processing log %s" % filename)

    mlog = mavutil.mavlink_connection(filename)

    output = {
            'GPS.A' : [],
            'POS.A' : [],
     }

    RGPI = None
    RFRH = None

    start_boot_timestamp_millis = 0

    while True:
        # we want replay sensor data, plus EKF3 result and SITL data
        m = mlog.recv_match(type=['POS', 'GPS'])
        if m is None:
            break
        t = m.get_type()

        if t == 'POS' and start_boot_timestamp_millis != 0:
            # output attitude of first EKF3 lane
            tmillis = m.TimeUS / 1000.
            timestamp = start_boot_timestamp_millis + tmillis
            #print(str(timestamp) + str(m))
            print(str(timestamp) + " " + str(m.Alt))
            #output['POS.A'].append((timestamp, m.Alt))

        if t == 'GPS':
            # output attitude of first EKF3 lane
            timestamp = weeksecondstoutc(m.GWk, m.GMS)
            #print(timestamp)
            start_boot_timestamp_millis = timestamp - (m.TimeUS / 1000)
            #print(str(start_boot_timestamp_millis) + str(m))
            #output['GPS.A'].append((timestamp, m.Alt))

    return
    # graph all the fields we've output
    import matplotlib.pyplot as plt
    for k in output.keys():
        t = [ v[0] for v in output[k] ]
        y = [ v[1] for v in output[k] ]
        plt.plot(t, y, label=k)
        plt.legend(loc='upper left')
    plt.show()

estimate(args.log)
