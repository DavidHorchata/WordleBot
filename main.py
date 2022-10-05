from json import load
import discord
import ProfanityChecker
from dotenv import load_dotenv
import os
import random


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    #print(f'{username}: {user_message} ({channel})')


    if message.author == client.user:
        return
    
    if channel != "wordle":
        return


    if user_message == "play":
        word_options = ["chess", "beach", "autos", "lurch", "batch"]    #add file to request 5 letter word from outside source or maybe add json file just use that instead
        word = random.choice(word_options)

        attempts = 5

        print(word) #server side only
        await message.channel.send("Game Start")



        while attempts != 0:

            attempts -= 1

            user_message = await client.wait_for("message", check=lambda message: message.channel.name == "wordle" and message.author != client.user)
            user_message = user_message.content


            while (len(user_message) != 5) or (user_message.find(' ') != -1) or (not user_message.isalpha()):

                await message.channel.send('Not a 5 letter word')
                user_message = await client.wait_for("message", check=lambda message: message.channel.name == "wordle" and message.author != client.user)
                user_message = user_message.content
                print(user_message)

        
            answer = []

            if user_message == word:
                await message.channel.send('Victory!')
                break
            else:
                for i in range(5):
                    if user_message[i] == word[i]:
                        answer.append(f" **{word[i]}** ")
                    elif user_message[i] in word:
                        answer.append(f" __{user_message[i]}__ ")
                    else:
                        answer.append(f" {user_message[i]} ")



            await message.channel.send("".join(answer))
        if attempts == 0:
            await message.channel.send('YOU LOSE GOOFY!')




load_dotenv()

    
client.run(os.getenv("TOKEN"))
