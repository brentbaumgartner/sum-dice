# sum-dice (Discord Bot) by Brent Alan

import discord
from discord.ext import commands
from flask import Flask, abort
import threading
import random
import asyncio

intents = discord.Intents.all()

app = Flask(__name__)
bot = commands.Bot(command_prefix='!', intents=intents)

YOUR_SERVER_ID = serveridhere  # Replace with your server ID

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.command(name='roll')
async def roll(ctx, num_dice: int = 1):
    # Check if the message is from the desired server
    if ctx.guild.id != YOUR_SERVER_ID:
        abort(401)  # Unauthorized access
        return
    
    if num_dice < 1 or num_dice > 6:
        await ctx.send("Please choose a number of dice between 1 and 6.")
        return
    
    results = [random.randint(1, 6) for _ in range(num_dice)]
    
    # Determine the response message based on the number of dice rolled
    if num_dice == 1:
        response_message = f'🎲 Roll: {results[0]}'
    else:
        rolls_string = ", ".join(str(result) for result in results)
        total_sum = sum(results)
        response_message = f'🎲 Rolls: {rolls_string} / Sum = {total_sum}'
    
    await ctx.send(response_message)

@bot.event
async def on_message(message):
    # Check if the message starts with '!roll'
    if message.content.startswith('!roll'):
        # Process the message as a command
        await bot.process_commands(message)

# Flask route for a health check
@app.route('/')
def index():
    return 'Sum Dice is running!'

def run_flask():
    app.run(port=5001)

# Run the Flask app in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

async def keep_alive():
    while True:
        await asyncio.sleep(60 * 30)  # Keep alive every 30 minutes
        print("Keep alive")

async def reconnect():
    while True:
        await asyncio.sleep(10)  # Attempt to reconnect every 10 seconds
        if bot.is_closed():
            try:
                print('Bot disconnected from Discord. Reconnecting...')
                await bot.start('secrettokenhere') # Replace with your secret token
                print('Reconnected successfully!')
                break  # Break out of the loop if reconnection is successful
            except Exception as e:
                # Print and log any exceptions during reconnection
                print(f"Error during reconnection: {e}")

async def main():
    await asyncio.gather(
        keep_alive(),
        reconnect()
    )                

# Run the Discord bot
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    bot.run('secrettokenhere') # Replace with your secret token
