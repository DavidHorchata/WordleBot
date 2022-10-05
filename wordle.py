import random
'''


Tester file to test features of game seperate from messaging



'''


def game():
    word_options = ["chess", "beach", "autos", "lurch", "batch"]
    word = random.choice(word_options)

    attempts = 5

    print(word)

    while attempts:
        userWord = input()
        while len(userWord) != 5:
            print("Not a 5 letter word")
            userWord = input()
            
        answer = []

        if userWord == word:
            print("VICTORY")
            break
        else:

            #first check for exact positon
            for i in range(5):
                if userWord[i] == word[i]:
                    answer.append(f" **{word[i]}** ")
                elif userWord[i] in word:
                    answer.append(f" *{userWord[i]}* ")
                else:
                    answer.append(f" {userWord[i]} ")



        print("".join(answer))

        attempts -= 1

game()
#italics = in word but not right positon
#bold = in right position
    
