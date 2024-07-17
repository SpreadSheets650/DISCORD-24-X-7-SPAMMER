from webserver import keep_alive
import requests

channelID = PUT THE CHANNEL ID
headers = {
    "authorization":
    "MTI1Mzk5MDU2OTI1NzA3ODc4NA.GGgkt9.LLIrgkIOq3FyZXqC8TKLUc9sVWnTW0zo2gsL20"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{1254091637756526695}/messages",
            headers=headers,
            json={"content": line})
