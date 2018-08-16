import requests

list =  input("Which list you want to create card: ")

if (list!='To Do' and list!='Doing' and list!='Done'):
	print("\nError List!")
	exit(1)
if list=='To Do':
	idList = '5b6c95b404562869fba22f6b'

elif list=='Doing':
	idList = '5b6c95b404562869fba22f6c'
	
elif list=='Done':
	idList = '5b6c95b404562869fba22f6d'
	
key =  input("API Keys: ")
token =  input("Token: ")
cardName =  input("Input card Name: ")
desc = input("input card description: ")

	

url = "https://api.trello.com/1/cards"

querystring = {"key":key,"token":token,"name":cardName,"desc":desc,"idList":idList}

response = requests.request("POST", url, params=querystring)

print(response.text)



