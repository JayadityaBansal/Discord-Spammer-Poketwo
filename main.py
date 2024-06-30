from webserver import keep_alive
import requests

channelID = 1155418506045702246
headers = {
    "authorization":
    "MTIyOTA5MjA1OTM5NTEzMzQ5MA.GWakdg.aqpRt4cbQ-KXj9EfY4HRaxEwnFJlQgUCUlElzE"
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
