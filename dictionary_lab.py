Abbreviations = {
    'idk' : 'I dont know',
    'lmao' : 'Laughing my ass off', 
    'ily' : 'I love you',

}

userinput = input('enter an abbreviation')

print(Abbreviations)

if(userinput in Abbreviations):
    print(Abbreviations.get(userinput))
else:
    print('Sorry, that word is not in the Abbreviation list')

