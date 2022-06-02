#!/bin/python3

import json
import os
import sys
import re

if len(sys.argv) < 2:
    print("Not enough argument [path] [extension]")
    exit()

path = sys.argv[1]
extension = sys.argv[2]

image_filter = sys.argv[3]
images = {}

log_file = sys.argv[4]

altitudes = {}

from pymavlink import mavutil
import datetime

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

def load_altitude(filename):
    '''run estimator over a replay log'''
    print("Processing log %s" % filename)

    mlog = mavutil.mavlink_connection(filename)

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
            altitudes[timestamp] = m.Alt
            #print(str(timestamp) + " " + str(m.Alt))
            #output['POS.A'].append((timestamp, m.Alt))

        if t == 'GPS':
            # output attitude of first EKF3 lane
            timestamp = weeksecondstoutc(m.GWk, m.GMS)
            #print(timestamp)
            start_boot_timestamp_millis = timestamp - (m.TimeUS / 1000)
            #print(str(start_boot_timestamp_millis) + str(m))
            #output['GPS.A'].append((timestamp, m.Alt))


def readFilter(file):
    f = open(file)
    lines = f.readlines()

    for i in lines:
        pattern = '(.*)-([0-9]{2,5}).ppm'
        result = re.search(pattern, i)
        folder_name = result.groups()[0]
        image_number = result.groups()[1]
        #print(folder_name)
        if not folder_name in images:
            images[folder_name] = []
        images[folder_name].append(int(image_number))
        #print(image_number)
        #print(i)

folders = ["batch_1_1_ppm", "batch_2_1_ppm"]

def addFromFile(folder, file):
    #mo = re.match("[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{6}\.[0-9]{3}-([0-9]{2,3})\.json", file)
    pattern = '([0-9]{2,5}).json'
    result = re.search(pattern, file)
    number = result.groups()[0]

    name = folder + "/" + str(number) + "." + extension

    if not os.path.exists("images/" + name):
        print("File don't exist")
        return False, ""

    if not int(number) in images[folder]:
        print("Not oriented image" + str(number))
        return False, ""

    # Opening JSON file
    f = open(path + "/" + file)
    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    timestamp = int(data["timestamp"])
    gps = data["gps"]
    print("Latitude: ")
    print(gps["lat"])
    print("Longitude: ")
    print(gps["lon"])
    # Closing file
    f.close()

    print("Altitude: ")
    alt = altitudes.get(timestamp) or altitudes[
      min(altitudes.keys(), key = lambda key: abs(key-timestamp))]
    print(str(alt))

    #kml.newpoint(name=name, coords=[(gps["lon"], gps["lat"])])
    return True, "{} {} {} {}".format(name, gps["lat"], gps["lon"], str(alt))


readFilter(image_filter)
print(images)

load_altitude(log_file)
output = open("imagesGPS.txt", "a")
files = os.listdir(path)
for f in files:
    if f.endswith(".json"):
        print(f)
        for folder in folders:
            r,line = addFromFile(folder, f)
            if r:
                output.write(line + '\n')
output.close()
