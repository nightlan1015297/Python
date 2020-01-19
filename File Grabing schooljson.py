import requests
result = requests.get('http://apps.nknush.kh.edu.tw/ZeroBB/GetJson?a=headlines')
for article in result.json():
	print(article['title'])