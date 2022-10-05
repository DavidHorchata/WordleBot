import json

def checkWord(word):    
    word_file = open("words.json")
    word_str = word_file.read()
    word_file.close()

    wordList = json.loads(word_str)

    if word in wordList:
        return True
    else:
        return False

