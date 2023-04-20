message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis et euismod nisl. Nulla facilisi. Aliquam euismod lectus ac ipsum cursus, vel aliquam elit semper. Nullam elementum massa quis quam "

words = message.lower().replace(".", "").replace(",", "").split(" ")


wordCount = {
    "Lorem" : "1",
    "ipsum" : "2",
    "dolor" : "1",
    "sit" : "1",
    "amet" : "1", 
    "consectetur" : "1", 
    "adipiscing" : "1",
    "elit" : "2", 
    "Duis" : "1", 
    "et" : "1", 
    "euismod" : "2",
    "nisl" : "1", 
    "Nulla" : "1", 
    "facilisi" : "1",
    "Aliquam" : "2", 
    "lectus" : "1", 
    "ac" : "1",
    "curvus" : "1",
    "vel" : "1",
    "semper" : "1",
    "Nullam" : "1",
    "elementum" : "1",
    "massa" : "1",
    "quis" : "1",
    "quam" : "1"  





}




userInput=input('enter a word: ')

if userInput in wordCount:
    