import requests

key = "AIzaSyDMcWqgiq-8y3q7Vova_3qYi5zyqZM2Iec"
address = input("請輸入地址 : ")

resultjs = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+address+'&key='+key+'&language=zh')
print(address + "  位在 ",resultjs.json()["results"][0]["address_components"][2]['long_name'])
