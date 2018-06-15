from requests import get 

def getHarryPotterData(baseUrl, ending): 
   response = get(baseUrl + ending) 
   jsonList = response.json() 
   return jsonList 
baseUrl = 'https://hp-api.herokuapp.com/api' 
listOfEndings = ['/characters', '/characters/students', '/characters/staff'] 
listOfKeys = ['name', 'species','wand'] 
listOfJsons = [] 
for ending in listOfEndings: 
   currentJson = getHarryPotterData(baseUrl, ending) 
   for s in currentJson: 
      print(s[listOfKeys[0]], s[listOfKeys[1]])
      
