import requests
response = requests.get('https://newsapi.org/v2/top-headlines?country=tw&apikey=0b5b20fd456a4a618237774ffa449953')
for article in response.json()['articles']:
	print(article['title'])