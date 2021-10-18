import os
import urllib3
import re
import json
import datetime
import requests
from bs4 import BeautifulSoup

DISCORD_ID = "655861269030502453" # leave blank if you don't want ping

url = "https://igg-games.com/request-pcgames-pc6.html"

def sendWebhook(game,link):
	webhookUrl = os.environ['WEBHOOK']

	payload = {
		"username": "IGG Bot",
		"embeds": [
			{
				"title": game,
				"description": "Update detected.",
				"url": link,
				"color": 12058624,
				"timestamp": str(datetime.datetime.now()),
				"footer": {
					"text": "Very Gamer"
				}
			}
		]
	}

	if DISCORD_ID and DISCORD_ID != "":
		payload["content"] = f"<@{DISCORD_ID}>"

	headers = {
		'Content-Type': 'application/json'
	}

	requests.request("POST", webhookUrl, headers=headers, data=json.dumps(payload))


def getVersionHash(string):
	# lol wtf
	temp = re.findall(r'\d+', string)
	arr = list(map(int, temp))
	num = 0

	for adnum in arr:
		num += adnum
	
	return num

def main():
	f = open('gamelist.json')
	games = json.load(f)

	http = urllib3.PoolManager()

	response = http.request('GET', url)
	soup = BeautifulSoup(response.data, "html.parser")

	links = soup.find_all("a")

	for link in links:
		for query in games:
			if link.text.find(query) > -1:
				ver = getVersionHash(link.text)
				if ver > games[query]:
					games[query] = ver
					sendWebhook(link.text, link["href"])
	
	with open('gamelist.json', 'w', encoding='utf-8') as f:
		json.dump(games, f, ensure_ascii=False, indent=4)

	f.close()

if __name__ == "__main__":
	main()
