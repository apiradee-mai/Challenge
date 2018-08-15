import requests

list =  input("Which list you want to create card: ")

if (list!='To Do' and list!='Doing' and list!='Done'):
	print("\nError List!")

if list=='To Do':
	idList = '5b6c95b404562869fba22f6b'

elif list=='Doing':
	idList = '5b6c95b404562869fba22f6c'
	
elif list=='Done':
	idList = '5b6c95b404562869fba22f6d'




url = "https://api.trello.com/1/cards"

querystring = {"name":"TestName","desc":"TestDesc","pos":"top","due":"2018-08-16","idList":"5b6c95b404562869fba22f6b","urlSource":"https://","keepFromSource":"all"}

response = requests.request("POST", url, params=querystring)

print(response.text)

