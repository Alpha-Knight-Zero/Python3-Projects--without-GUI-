import json
from difflib import get_close_matches

data=json.load(open("dictdata.json"))

def match(word):
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())):
        for c in range(len(get_close_matches(word,data.keys()))):
            print("Did you mean %s ?"%get_close_matches(word,data.keys())[c])
            decide=input("Press y for yes and n for no :")
            if decide.lower()=="y":
                return data[get_close_matches(word,data.keys())[c]]
    else:
        return "Sorry, This word was not found in the dictionaty."

word=input("Enter the word to search for :")
output=match(word)
if type(output)==list:
    c=1
    for x in output:
        print(c,".",x)
        c+=1
else:
    print(output)