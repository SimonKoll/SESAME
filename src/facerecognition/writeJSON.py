# Python program to update 
# JSON 
import json 
from datetime import datetime

now = datetime.now()

def write_json(data, filename='../frontend_current/sesame-web/src/assets/entries.json'): 
	with open(filename,'w') as f: 
		json.dump(data, f, indent=4) 
def writeEntriesToJson(currentname):
    with open('../frontend_current/sesame-web/src/assets/entries.json') as json_file: 
        data = json.load(json_file)
            
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
            
        temp = data['recognized-entries']
            # python object to be appended 
        y = {"name": currentname, 
            "time": dt} 
        temp.append(y) 
        
    write_json(data) 
