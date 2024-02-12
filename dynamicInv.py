#!/usr/bin/env python3
# dynamic inventory.ini generator for ansible
import json

# for example my webservers and database servers or everything we want
dynamicHosts = {
    'webServers': ['web1', 'web2'],
    'databaseServers': ['db1', 'db2'],
}

print(json.dumps(dynamicHosts))


# after this we have to add this line to our ansible.cfg file
[defaults] 
inventory = /path to this script 

# for certainaity we can check ansible-inventory --list and all dynamicHosts should add to our inventory!