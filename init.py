import os
import sys
import json

json_data = json.loads(open(input("Insert .mup file: "), "r").read())
open("data.json", "w+").write(json.dumps(json_data, indent=4))
new_json = json.loads("{}")


def checkInt(str):
    if str[0] in ('-', '+'):
        return str[1:].isdigit()
    return str.isdigit()

#SET UP ROOTS AND ROOT VALUES
for i in json_data["ideas"]: # Loop through every root
    x = json_data["ideas"][i]["title"]

    if not("ideas" in json_data["ideas"][i]): #Check if root has ideas in it
        new_json[x.split(" = ")[0]] = x.split(" = ")[1] # If not, assing the value
    elif(len(list(json_data["ideas"][i]["ideas"])) == 0): #If has ideas in it, but there is no any idea. Do the same thing
        new_json[x.split(" = ")[0]] = x.split(" = ")[1]
    else:
        new_json[x] = {} #If has ideas. Create empty object


for i in json_data["ideas"]: # Loop through every root
    if("ideas" in json_data["ideas"][i]):
        x = json_data["ideas"][i]["title"]

        if("ideas" in json_data["ideas"][i]):
            for y in json_data["ideas"][i]["ideas"]:
                if("ideas" in json_data["ideas"][i]["ideas"][y]):
                    new_json[x][json_data["ideas"][i]["ideas"][y]["title"]] = {}
                    for a in json_data["ideas"][i]["ideas"][y]["ideas"]:
                        if(checkInt(json_data["ideas"][i]["ideas"][y]["ideas"][a]["title"].split(" = ")[1])):
                            new_json[x][json_data["ideas"][i]["ideas"][y]["title"]][json_data["ideas"][i]["ideas"][y]["ideas"][a]["title"].split(" = ")[0]] = int(json_data["ideas"][i]["ideas"][y]["ideas"][a]["title"].split(" = ")[1])
                        else:
                            new_json[x][json_data["ideas"][i]["ideas"][y]["title"]][json_data["ideas"][i]["ideas"][y]["ideas"][a]["title"].split(" = ")[0]] = json_data["ideas"][i]["ideas"][y]["ideas"][a]["title"].split(" = ")[1]
                else:
                    if(checkInt(json_data["ideas"][i]["ideas"][y]["title"].split(" = ")[1])):
                        new_json[x][json_data["ideas"][i]["ideas"][y]["title"].split(" = ")[0]] = int(json_data["ideas"][i]["ideas"][y]["title"].split(" = ")[1])
                    else:
                        new_json[x][json_data["ideas"][i]["ideas"][y]["title"].split(" = ")[0]] = json_data["ideas"][i]["ideas"][y]["title"].split(" = ")[1]


open("new_json.json", "w+").write(json.dumps(new_json, indent=4))
