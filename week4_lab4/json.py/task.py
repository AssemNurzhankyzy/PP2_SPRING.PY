import json 


print("Interface status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open('week4_lab4/json.py/sample-data.json') as f:
    data = json.load(f)

request_from_server = data["imdata"][0]["l1PhysIf"]["attributes"]["dn"]
speed = data["imdata"][0]["l1PhysIf"]["attributes"]["fecMode"]
mtu = data["imdata"][0]["l1PhysIf"]["attributes"]["mtu"]
print(request_from_server, "                            ", speed," ", mtu )
print(request_from_server, "                            ", speed," ", mtu )
print(request_from_server, "                            ", speed," ", mtu )