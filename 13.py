user = {
    "id": 42,
    "username": "jdoe",
    "email": "jdoe@example.com",
    "password": "s3cr3t",
    "joined": "2021-03-15",
}

extracts = ["id", "username", "email"]

updated={key:value for (key,value) in user.items() if key in extracts}

print(updated)