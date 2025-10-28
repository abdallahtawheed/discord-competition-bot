from email import message
from http import server
from sys import prefix
from discord.ext import commands
import discord
from discord.utils import get
import os
import numpy as np
import json

import snscrape
import pandas
import snscrape.modules.twitter as sntwitter
import pandas as pd

import re

# query = "love"
# tweets = []
# limit = 30

# string = "I love pie/4342341331321"

# m = re.search(('(\d{1,})'), string)
# if(m):
#   print(m.group(1))
# else:
#   print("not there dude")

# for tweet in sntwitter.TwitterSearchScraper(query).get_items():
#   # print(vars(tweets))
#   # break
#   if len(tweets) == limit:
#     break
#   else:
#     tweets.append([tweet.url,tweet.user.username,tweet.content])
# df = pandas.DataFrame(tweets,columns=["url","username","tweet"])
# print(df)

# query_id = 1601913091553636352
# scraper = sntwitter.TwitterTweetScraper(query_id).get_items()
# print(scraper)

# for i, tweet in enumerate(scraper, start = 1):
#                     print(i,tweet)


#                     #converts tweet json pulled from twitter back into json here
        
#                     json_obj_tweet = tweet.json()

#                     #converts json object to python dictionairy
                    
#                     py_dic_from_json_obj_tweet = json.loads(json_obj_tweet)

#                     # print(json.loads(json_obj_tweet))

#                     py_dic_content = py_dic_from_json_obj_tweet["content"]

  
#                     # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  
#                     print(py_dic_content)       

  
#                   	# Converting the scraped tweet into a json object
#                   	# tweet_json = json.loads(tweet.json())
#                   	#Printing out the content of a tweet
#                   	# print (f"\nScraped tweet: {tweet_json['content']}")
#                   	#Writing to file
  
# # file_data = np.loadtxt("combinations.txt",dtype = str)
# # print(file_data[0])



with open('combinations.txt', 'r') as f:
  words = f.read()
  permutations = words.splitlines()
print(permutations[0])

intents = discord.Intents.default()
intents.members = True

bot = discord.Client(intents=discord.Intents.all())

my_secret = os.environ['TOKEN']



member_id = []



# with open('roles_given.json','r') as f:
#   test = json.load(f)
#   print(test.get('num_roles_given'))






@bot.event
async def on_ready():
  print('ah, we finally logged in {0.user}'.format(bot))


@bot.event
async def on_message(message):
  if(message.content == "I need hints"):
    await message.channel.send("If you want to receive hints, you need credits. To receive credits, comment on the Twitter announcement of the Easter Egg, tagging 4 friends. Then copy the URL and send it here. It should look be in this format: https://twitter.com/yourprofile/status/XXXXXXXXXXXX")
  if message.author == bot.user:
    return
    
    #ctx. = await self.bot.get_context(message)
    # msg = message.content
    # for word in badwords:
    #     if word in msg:
    #         await message.delete()
    #         await ctx.send("Dont use that word!")
    # await ctx.process_message(message)

  
  if (message.content == "f68b03fca9ae46e35fd5dc5788f38d3acbd1220dd90931d4d02bc524577f9075"):
    server = bot.get_guild(1045721344882511882)
    user = message.author
    print(user.id)
    member = server.get_member(user.id)
    print(member)
    role = get(server.roles, name="Mystery")
    if role not in member.roles:
      await member.add_roles(role, atomic=True)
      await message.channel.send(
      'You now have the mystery role. You cannot talk about the mystery role. If you mention it in the Sprawl Discord, you will lose the mystery role forever.')
    else:
      await message.channel.send("you already have that role!")
  else:
    for word in permutations:
      with open('roles_given.json', 'r') as f:
        
        number_given = json.load(f)
        num = number_given['number_roles_given']
        
        if word in message.content:
          if(num < 200):
            server = bot.get_guild(1045721344882511882)
            user = message.author
            # print(user.id)
            member = server.get_member(user.id)
            # print(member)
            role = get(server.roles, name="newrole")
            if role not in member.roles:
              
            # with open('roles_given.json', 'r') as f:
            #   roles_given = json.load(f)
            #   roles_given['number_roles_given'] = roles_given.get('num_roles_given') + 1
            #   print(roles_given.get('num_roles_given'))
      
              with open('roles_given.json', 'r') as f:
                num_given = json.load(f)
                num = num_given['number_roles_given'] 
                num_given['number_roles_given'] = num + 1
                print(num_given['number_roles_given'] )
              with open('roles_given.json', 'w') as f:
                json.dump(num_given,f)
                
              #   member_json =json.dump(member_id,f)
              #   print(member_json)
              # with open('hints.json','r') as f:
              #   memberids = json.load(f)
              #   memberids['memberid'] = memberids.get('memberid')
              #   print(memberids['memberid1'])
                
    
              #grants them the role
              
              role = get(server.roles, name="newrole")
              await member.add_roles(role, atomic=True)
          
              await message.channel.send(
                "Congratulations, you found the Easter Egg! You now have the whitelist role. Make sure to submit your wallet in the submit wallet channel. Please don't share the master key with other Sprawl Citizens.")

            else:
              await message.channel.send("you already have that role!")
          #in case the number of roles is already at or more than 200
  
            
          else:
            await message.channel.send("Sorry, the max whitelist allocation has been reached")
        # await message.process_message(message)
  
    #regex check before it scrapes the tweets and counts the characters
    
    reg_check = re.search("(https:\/\/twitter\.com\/)",message.content)
    if(reg_check):
      # print("yep it worked")
  
      real_tweet = re.search("([0-9]{19})",message.content)
  
      tweet_id = real_tweet.group(1)
      # print(tweet_id)
        
      scraper = sntwitter.TwitterTweetScraper(tweet_id).get_items()
      # print(scraper)
      
      for i, tweet in enumerate(scraper, start = 1):
                          # print(i,tweet)
      
        
                          # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
      
                          #converts tweet json pulled from twitter back into json here
              
                          json_obj_tweet = tweet.json()
      
        
                          # print(json_obj_tweet)
      
        
                          # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
      
                          #converts json object to python dictionairy
                          
                          py_dic_from_json_obj_tweet = json.loads(json_obj_tweet)
      
      
        
                          # print(json.loads(json_obj_tweet))
      
        
                          # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
      
        
                          py_dic_content = py_dic_from_json_obj_tweet["content"]
      
        
                          # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
                          # print(py_dic_content)       
      
        
                        	# Converting the scraped tweet into a json object
                        	# tweet_json = json.loads(tweet.json())
                        	#Printing out the content of a tweet
                        	# print (f"\nScraped tweet: {tweet_json['content']}")
                        	#Writing to file
  
      #sends the failure message to the user
      # print(py_dic_content)
      hint_credits_check = re.search("(@(.)+){4,}",py_dic_content)
      if(hint_credits_check):
        
        user_id = message.author.id


        
        
        with open('hints.json', 'r') as f:
          hints = json.load(f)
          # if `str(member.id)` isn't in `hints`, then return 5
          hints[str(user_id)] = hints.get(str(user_id), 5)
        with open('hints.json', 'w') as f:
          json.dump(hints, f)
        #   print(hints)



          

        await  message.channel.send('You have tagged 4 friends, you have earned 4 hint credits. Type "Hint" to receive 1 Hint per key.')

        
      else:
        await message.channel.send("Sorry, I'm not able to verify that you tagged 4 friends. Please make sure it's in the correct format, like so: https://twitter.com/yourprofile/status/XXXXXXXXXXXX. If you need help, open a ticket on Discord")
    
    else:
      if message.content == "Hint" or message.content == "Hint.":
        
        with open('hints.json', 'r') as f:
          user_id = message.author.id
          
          hints = json.load(f)
          # if `str(member.id)` isn't in `hints`, then return 5
          hints[str(user_id)] = hints.get(str(user_id), 0)

        #   print(hints)

          
          if(hints[str(user_id)] == 5):

            
            await message.channel.send("Boudica's belt has been used more than one to strangle snitches, I would keep my mouth shut if I were you.")
            

            with open('hints.json', 'w') as f:  
                hints[str(user_id)] = hints.get(str(user_id), 0) -1
                json.dump(hints, f)
            
            
          elif(hints[str(user_id)] == 4):

            await message.channel.send("Taxis are core of importance for The Sprawl. Everyone needs to get around but not everyone has a car, right? Well, if you don't have much money to buy a car, you might want to participate the Sprawl quizes, you might earn some cash! We announce them every week on Twitter")            
            
            with open('hints.json', 'w') as f:  
                hints[str(user_id)] = hints.get(str(user_id), 0) -1
                json.dump(hints, f)
              
          elif(hints[str(user_id)] == 3):

            await message.channel.send("Of course Robin had to steal the attention for Black Block's team photo. Stylish footwear is of the utmost importance for good fashion.")            
            
            with open('hints.json', 'w') as f:  
                hints[str(user_id)] = hints.get(str(user_id), 0) -1
                json.dump(hints, f)
            
          elif(hints[str(user_id)] == 2):

            await message.channel.send("Rumours say that Seraph, the wittiest thief in the Sprawl, was around the basketball court when the City Pass was announced. What was he doing there?")            
            
            with open('hints.json', 'w') as f:  
                hints[str(user_id)] = hints.get(str(user_id), 0) -1
                json.dump(hints, f)
              
          elif(hints[str(user_id)] == 1):

            await message.channel.send("You have received all the hints I have been programmed to give. Search hard enough, and you will find each key! Good luck.")            
            
            with open('hints.json', 'w') as f:  
                hints[str(user_id)] = hints.get(str(user_id), 0) -1
                json.dump(hints, f)

          elif(hints[str(user_id)] == 0):

            await message.channel.send("You have received all the hints I have been programmed to give. Search hard enough, and you will find each key! Good luck.")            
            
            print("this one was triggered")

          else:
            ()

      
      
      else:
          ()
    
    #checks if they put the secret code for the mystery role
    
  
       

bot.run(my_secret)