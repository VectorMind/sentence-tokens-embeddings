import json

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def save_json(filename,data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    return

def load_text(filename):
    return open(filename, 'r', encoding='utf-8').read()

