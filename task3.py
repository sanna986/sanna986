import requests

headers = {
    'Accept': 'application/yang-data+json',
}

response = requests.get('https://192.168.56.102:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity', headers=headers, verify=False, auth=('cisco', 'cisco123!'))


headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
}

data = '${ "severity": "alerts" }'

response = requests.post('https://192.168.56.102:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor', headers=headers, data=data, verify=False, auth=('cisco', 'cisco123!'))


