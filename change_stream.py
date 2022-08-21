from pymongo import MongoClient
import requests

SERVICE = "http://localhost:5000/people"
con = MongoClient("mongodb://192.168.2.3:27017,192.168.2.3:27018,192.168.2.3:27019/?replicaSet=PrimaryReplicaSet")
people = con['people']['people']
watching = {}

#try:
resume_token = None
with people.watch() as stream:
    for change in stream:
        print(change)
        resume_token = stream.resume_token
        match change['operationType'] :
            case 'insert':
                requests.post(SERVICE, json={'name': change['fullDocument']['name']})
            ## Stream only gets updated fields more complex logic required for other updates such as audit records
#except:
#    print("WE MESSED UP")