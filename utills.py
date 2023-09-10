import json

def load_file():
    with open ('operations.json', 'r', encoding='utf-8') as file:
        old_file = json.load(file)
        return old_file