from typing import List
from discord.ext import commands
import discord

##from asyncio.windows_events import NULL
from operator import indexOf
import os
from pickle import NONE
import discord
from discord.ext import commands
from discord import Embed
import time
import datetime
from datetime import timedelta
#from datetime import timezone
from datetime import datetime
import sqlite3
import random
import math
import itertools
from typing import Optional
from discord.utils import get
intents = discord.Intents.default()

intents.guilds = True

activity = discord.Activity(type=discord.ActivityType.watching, name="ETH-ing idk")
bot = commands.Bot(command_prefix = "+", intents = intents, activity=activity, status=discord.Status.online)

class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.green(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

bot.help_command = MyHelpCommand()



def checkbalance(userid):
    print("Lol")
    #check their balance and then return some value 

def rpscheckwin(userresponse, botresponse):
   
    
    if userresponse == "Rock":
        if botresponse == "Paper":
            return "You Lost."
        elif botresponse == "Scissors":
            return "You Won!"
        elif botresponse == "Rock":
            return "Tie."
    elif userresponse == "Paper":
        if botresponse == "Rock":
            return "You Won!"
        elif botresponse == "Scissors":
            return "You Lost."
        elif botresponse == "Paper":
            return "Tie."
    else:
        if botresponse == "Paper":
            return "You Won!"
        elif botresponse == "Scissors":
            return "Tie."
        elif botresponse == "Rock":
            return "You Lost."
        
def checkbalance(userid):
    print("Lol")

def response():
    

    rock = 1
    paper = 2
    scissors = 3

    number = random.randint(1,3)
    
    if number == 1:
        return "Rock"
    elif number == 2:
        return "Paper"
    else:
        return "Scissors"





    
@bot.command(aliases=['rps', 'rockpaperscissor'])
async def rockpaperscissors(ctx):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    view = Buttons(ctx.author)
    
    await ctx.send("Let's play Rock Paper Scissors!", view=view)

class Buttons(discord.ui.View):
    def __init__(self, user: discord.User, *, timeout: int = 180):
        super().__init__(timeout=timeout)
        self.user = user
        self.value = None
    
    async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user and interaction.user.id == self.user.id
    
    @discord.ui.button(label='Rock 🪨', style=discord.ButtonStyle.green,)
    async def Whitelist(self, button: discord.ui.Button, interaction: discord.Interaction):
        botanswer = response()
        await interaction.response.defer(ephemeral=True)
        await (interaction.followup).send('You Picked Rock! \n \n The Bot picked ' + str(botanswer) + '!', ephemeral=True)
        
        userresponse = "Rock"
        botresponse = botanswer
        print(botresponse)
        
        await (interaction.followup).send((rpscheckwin(userresponse, botanswer)), ephemeral=False)
        
        self.value = "Rock"
        self.stop()
    @discord.ui.button(label='Paper 🧻', style=discord.ButtonStyle.green)
    async def Staking(self, button: discord.ui.Button, interaction: discord.Interaction):
        botanswer = response()
        await interaction.response.defer(ephemeral=True)
        await (interaction.followup).send('You Picked Paper! \n \n The Bot picked ' + str(botanswer) + '!', ephemeral=True)
        
        userresponse = "Paper"
        botresponse = botanswer
        print(botresponse)
        
        await (interaction.followup).send((rpscheckwin(userresponse, botanswer)), ephemeral=False)
        
        self.value = "Paper"
        self.stop()
    @discord.ui.button(label='Scissors ✂️', style=discord.ButtonStyle.green)
    async def GetaMod(self, button: discord.ui.Button, interaction: discord.Interaction):
        botanswer = response()
        await interaction.response.defer(ephemeral=True)
        await (interaction.followup).send('You Picked Scissors! \n \n The Bot picked ' + str(botanswer) + '!', ephemeral=True)
        
        userresponse = "Scissors"
        botresponse = botanswer
        print(botresponse)
        
        await (interaction.followup).send((rpscheckwin(userresponse, botanswer)), ephemeral=False)
        
        self.value = "Scissors"
        self.stop()
    
          
   
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.response.send_message('Cancelling', ephemeral=True)
    
        self.value = "Cancel"


#Minefield stuff here!

class MineSafe(discord.ui.Button):
    def __init__(self,row):
        super().__init__(label = "❌", row = row ) # Define button params here
    async def callback(self, interaction: discord.Interaction):
    # Do stuff here like you would before. To get the button object, just use self.
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send('Safe! ⛳️', ephemeral=False)
        
        self.view.stop()
class MineDanger(discord.ui.Button):
    def __init__(self,row):
        super().__init__(label = "❌", row = row) # Define button params here
    async def callback(self, interaction: discord.Interaction):
# Repeat for button2, button3, etc
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send('You died! 💥', ephemeral=False)
        self.view.stop()

class MyView(discord.ui.View):
    def __init__(self, user: discord.User, *, timeout: int = 180):
        super().__init__(timeout=timeout)
        self.user = user
        self.value = None
    
    async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user and interaction.user.id == self.user.id



@bot.command(aliases=['mf', 'field'])
async def minefield(ctx):
    rows = [
    [MineDanger, MineDanger, MineDanger],
    [MineDanger, MineSafe, MineDanger],
    [MineDanger, MineDanger, MineDanger] ]
# Notice how I don't call the buttons, so that I can set the row later
    random.shuffle(rows)
    view = MyView(ctx.author)

    for rowcount, buttons in enumerate(rows):
        random.shuffle(buttons)
        for button in buttons:
            view.add_item(button(row = rowcount))
    
    
    await ctx.send("Minefield!", view=view)


@bot.command(aliases=['cf', 'coin'])
async def coinflip(ctx, coinside):
    coin = random.randint(0,1)
    #1 is heads
    #0 is tails
    if coin == 1:
        
        if str(coinside) == "heads":
        
            embed=discord.Embed(title="Flip a coin!", color=0x36ce78)
            embed.add_field(name="Heads!", value="You Won!", inline=False)
            embed.set_author(name=ctx.author.name)
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/a/a0/2006_Quarter_Proof.png")
            await ctx.send(embed=embed)

        else:
            embed=discord.Embed(title="Flip a coin!", color=0xb62f2f)
            embed.add_field(name="Heads!", value="You Lost!", inline=False)
            embed.set_author(name=ctx.author.name)
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/a/a0/2006_Quarter_Proof.png")
            await ctx.send(embed=embed)
    else:
        if str(coinside) == "tails":
        
            embed=discord.Embed(title="Flip a coin!", color=0x36ce78)
            embed.add_field(name="Tails!", value="You Won!", inline=False)
            embed.set_author(name=ctx.author.name)
            embed.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
            await ctx.send(embed=embed)

        else:
            embed=discord.Embed(title="Flip a coin!", color=0xb62f2f)
            embed.add_field(name="Tails!", value="You Lost!", inline=False)
            embed.set_author(name=ctx.author.name)
            embed.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
            
            await ctx.send(embed=embed)




@bot.command(aliases=['ws', 'wheel'])
async def wheelspin(ctx):

    #play rolling gif, it lands, then go with the rest
    #maybe time.sleep(length of gif)

    out = random.randint(1, 10000)

    if out >= 1 and out <= 64: 
        
                embed=discord.Embed(title="Wheel Spun!",description= "You won a player pass!", color=discord.Color.green())
                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
                await ctx.send(ctx.author.mention,embed=embed) 
                member = ctx.message.author
                role = discord.utils.get(member.guild.roles, name = "whitelist")
                await member.add_roles(role)
                #give role
    elif out >= 65 and out <= 3300: 
                
                
                
                embed=discord.Embed(title="Wheel Spun!",description= "You won 100 coins!", color=discord.Color.blue())
                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
                
                await ctx.send(ctx.author.mention,embed=embed) 
                
    elif out > 3300:
        
                embed=discord.Embed(title="Wheel Spun!",description= "You didn't win anything..", color=discord.Color.red())
                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
                await ctx.send(ctx.author.mention,embed=embed) 

bot.run("TOKEN")
