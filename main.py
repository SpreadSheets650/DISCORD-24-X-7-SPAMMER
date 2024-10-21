from webserver import keep_alive
import requests

channelID = 1023440914322047069
headers = {
    "authorization":
    "ODYzNDU5NzQ5MDA1NjIzMzE2.Gegy02.jwjoyvqEL7xzTJdNRFIDaNP7RPUngNVnGuicgc"
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
