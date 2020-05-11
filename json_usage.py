import json

#dictionary

file1 = {'name':'gorilla toy','color':'red'}
files2 = {'name':'banana plastic bottle','color':'yellow'}
objects = {"file1" : file1, "file2": files2}
json_file = json.dumps(objects)

print(json_file)