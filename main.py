from webserver import keep_alive
import requests

channelID = 969317628202078258
headers = {
    "authorization":
    "ODg0ODA4OTk1NDk4NTA0Mjkz.GzyKqm.WfJxWVt8yuWXXm5wHX9Nqk25pGEF0e4JlKGKc0"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
