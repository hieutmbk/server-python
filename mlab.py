import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds135335.mlab.com:35335/nlp-db

host = "ds135335.mlab.com"
port = 21980
db_name = "nlp-db"
username = "admin"
password = "admin123"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())