import json

def parse_json_config(path):
    with open(path, "r") as file:
        configuration = file.read()
    
    configuration_dict = json.loads(configuration)
    return configuration_dict