#!/usr/bin/python

import argparse
import json
import time

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="configuration file used by john")
parser.add_argument("-t", "--executingType", help="single|incremental|...")
parser.add_argument("-g", "--charsetGroup", help="charset to be used for brute force")
parser.add_argument("-p", "--passwordFile", help="password file containing hashes to crack")

# /opt/john180/run/john --incremental=Alnum2 --config=/opt/john180/run/john.conf dynamic_25.psw --fork=4

args = parser.parse_args()

argsJson = {}
argsJson['config'] = args.config
argsJson['executingType'] = args.executingType
argsJson['charsetGroup'] = args.charsetGroup
argsJson['passwordFile'] = args.passwordFile
json_data = json.dumps(argsJson)


time.sleep(5)  
print json_data