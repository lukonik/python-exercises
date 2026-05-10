import json

user_json = '{"id": 1, "profile": {"name": "Alice", "settings": {"theme": "light"}}}'


def update_theme(json_str: str):
    json_data = json.loads(json_str)
    json_data["profile"]["settings"]["theme"] = "dark"
    updated_json = json.dumps(json_data, indent=4)
    print(updated_json)


update_theme(user_json)
