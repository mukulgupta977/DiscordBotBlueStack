from discord.ext import commands
from ResponseHandler.responseHandler import ResponseHandler
import __init__

TOKEN = 'NjkwMTUyNDQ3NzI5MDc0MTc4.XnNVmw.oT_-MlJA8_sWbu5gvv5xWjBsF88'

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Bot is connected to Discord Server and is Ready!!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        if message.content:
            await message.channel.send(ResponseHandler.handle_request(message))
    except Exception as e:
        print("Error occurred for message " + message.content
              + " by user " + str(message.author)
              + "\nError Detail ")
        print(e)
        return await message.channel.send("Something went wrong")

client.run(TOKEN)
