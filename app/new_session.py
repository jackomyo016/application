import requests

base_url = 'http://localhost:8000/prediction'

requete = '?Pclass=1&Name=Cumings,%20Mrs.%20John%20Bradley%20(Florence%20Briggs%20Thayer)&Sex=male&SibSp=1&Parch=0&Ticket=PC%2017599&Fare=16&Cabin=C85&Embarked=S&Age=22'

url = base_url + requete
response = requests.get(url)
print(response.json())
