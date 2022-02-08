import json

def read_json(path):
    """
    Reads a json file and returns the data.
    """
    with open(path, 'r') as f:
        return json.load(f)