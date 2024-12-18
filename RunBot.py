
# Debian
# pip install discord.py --break-system-packages
# pip install audioop-lts --break-system-packages 
# pip3 install web3 --break-system-packages

# Debian: /lib/systemd/system/apintio_bot_discord.service
# Learn: https://youtu.be/nvx9jJhSELQ?t=279s
"""
[Unit]
Description=Discord Bot
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python  /git/discord_bot/RunBot.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
"""
# Learn: https://youtu.be/nvx9jJhSELQ?t=368
# cd /lib/systemd/system/
# sudo systemctl enable apintio_bot_discord.service
# sudo systemctl start apintio_bot_discord.service
# sudo systemctl status apintio_bot_discord.service
# sudo systemctl stop apintio_bot_discord.service
# sudo systemctl restart apintio_bot_discord.service

import socket
import struct
import uuid
import discord
from discord.ext import commands
import os

from web3 import Web3
from hexbytes import HexBytes
from eth_account.messages import encode_defunct

# Linux Default
# Run  /git/discord_bot/RunBot.py
# Token: /token/discord_bot_token.txt
string_where_to_store_verified_user = "/git/metamask_users/discord"

def verify_signature_from_text(text, splitter="|"):
    splitted = text.split(splitter)
    if len(splitted) == 3:
        return verify_signature(splitted[0], splitted[1], splitted[2])
    return False

def verify_signature(message, public_address, signed_message):
    w3 = Web3(Web3.HTTPProvider(""))
    mesage= encode_defunct(text=message)
    address_recovered = w3.eth.account.recover_message(mesage,signature=HexBytes(signed_message))
    print(address_recovered+"\n+"+public_address)
    is_verified = address_recovered == public_address
    return is_verified
    
token_file_path = "/token/discord_bot_token.txt"

print("Path:", os.path.abspath(token_file_path))
if not os.path.exists(token_file_path):
    print("Creating a default file at that path")
    string_folder_path = os.path.dirname(token_file_path)
    if not os.path.exists(string_folder_path):
        os.makedirs(string_folder_path)
    with open(token_file_path, "w") as f:
        f.write("https://discord.com/developers/applications")

# Read the token from the file
with open(token_file_path, "r") as f:
    token_content = f.read().strip()

if not token_content or token_content.startswith("http"):
    # If the file is empty or contains the placeholder, prompt the user
    print("bot_token.txt is empty or contains a placeholder.")
    print("Please paste your bot token in:")
    print(token_file_path)
    print("You can get your bot token from https://discord.com/developers/applications")
    print("Then click on your bot, go to 'Bot' section, and click 'Copy' under Token.")
    print("Paste the token in bot_token.txt and rerun this program.")
    exit()

# Token is ready to use
token = token_content
print("Hello Discord Bot Relay Int")
print("Token (truncated):", token[:10], "...")

SERVER_ID = 1189765674554376192 

SALON_ID= list()
SALON_ID.append(1222573438187737100) ## TWITCH PLAY CHAT
SALON_ID.append(1223448265492795454) ## TWITCH PLAY CHAT CONFERENCE
SALON_ID.append(1318337581393514587) ## WORKING ON TWITCH
SALON_ID.append(1316424864160157756) ## APINT TO BOT

ADMIN_DISCORD_USER_ID= [191665082894254081]




INTERPRETER_IVP4="127.0.0.1"
INTERPRETER_PORT_TEXT=3614
INTERPRETER_PORT_INTEGER=3615



import discord
from discord.ext import commands

# Bot Setup
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.dm_messages = True
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)
admin_role_name = "Admin"  # Replace with your admin role name



@bot.command(name="hello")
async def hello_callback(ctx):
    await ctx.send(f"Hello {ctx.author} ({ctx.author.id})")
    

@bot.command(name="ping")
async def hello_callback(ctx):
    await ctx.send("pong")



@bot.event
async def on_command_error(ctx, error):
    message_back=""
    command_string = ctx.message.content
    print(f"Command: {command_string}")
    
    if len(command_string) > 2 and command_string[0] == "!" and command_string[1] == "s" :
        try_to_push_valide_text(command_string)
    else: 
        for c in command_string.split(" "):
            if len(c) > 2 and c[0] == "!" and c[1] == "i" :
                try_to_push_valide_integer(c)
       
    if len(message_back) > 0:
        await ctx.send(message_back)
    
# Check for Admin Role
def is_admin(ctx):
    if ctx.guild:  # Ensure the command is in a guild context
        return any(role.name == admin_role_name for role in ctx.author.roles)
    return False  # No roles exist in DM context


@bot.command()
async def listen(ctx, *, message):
    # if is_admin(ctx):
    #     await ctx.send(f"Listening to: {message}")
    await ctx.send(f"Listening to: {message}")


# Events
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")
    print("Bot is ready.")

dictionary_guid_to_sign = {
}
dictionary_guid_to_sign["Test"] = 0

def has_guid(author_id):
    return author_id in dictionary_guid_to_sign
def get_guid(author_id):
    return dictionary_guid_to_sign[author_id]


def is_admin(author_id):
    return author_id in ADMIN_DISCORD_USER_ID

def push_integer_to_server(integer):
    ivp4 = INTERPRETER_IVP4
    port = INTERPRETER_PORT_INTEGER
    index=0
    print(f"Pushing integer {integer} to server {ivp4}:{port}")
    byte = struct.pack("<ii", index, integer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(byte, (ivp4, port))
    sock.close()
    
def push_index_integer_to_server(index, integer):
    ivp4 = INTERPRETER_IVP4
    port = INTERPRETER_PORT_INTEGER
    
    print(f"Pushing integer {index} {integer} to server {ivp4}:{port}")
    byte = struct.pack("<ii", index, integer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(byte, (ivp4, port))
    sock.close()


def try_to_push_valide_text(text:str):
    print("Pushing text as short cut")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(text.encode() , (INTERPRETER_IVP4, INTERPRETER_PORT_TEXT))
    sock.close()

def try_to_push_valide_integer(text):
    if len(text) >2 and text[0] == "!" and text[1] == "i" :
        text = text[2:]
       
    if text.find(".") >= 0:
        ts= text.split(".")
        try :
            index = int(ts[0])
            integer = int(ts[1])
            push_index_integer_to_server(index, integer)
            return True
        except ValueError:
            return False
    else :
        if text == "0":
            push_integer_to_server(0)
        else:
            try:
                integer = int(text)
                push_integer_to_server(integer)
                return True
            except ValueError:
                return False

def record_author_as_meta_mask_user_verified(author_id, public_address):
    print(f"Recorded user {author_id} as verified with public address {public_address}")
    if not os.path.exists(string_where_to_store_verified_user):
        os.makedirs(string_where_to_store_verified_user)
    with open(f"{string_where_to_store_verified_user}/{author_id}.txt", "w") as f:
        f.write(public_address)
    print("Path:", os.path.abspath(f"{string_where_to_store_verified_user}/{author_id}.txt"))
    
    

def is_salong_id_observed(salon_id):
    return salon_id in SALON_ID    

# Event: Triggered when a message is sent in the server or as a DM
@bot.event
async def on_message(message):
    
    if message.author == bot.user:
        return
    string_stripped = message.content.strip()
    author_id= message.author.id

    # Allow other commands to process
    await bot.process_commands(message)
    
    # Check if the message is in the specified server and channel
    if message.guild and is_salong_id_observed(message.channel.id):
            print(f"Message received in channel {message.channel.id}: {message.content}")
            #try_to_push_valide_integer(string_stripped)
            #await message.channel.send(f"Hello {message.author.mention}, I see your message: {message.content}")
    # Check if the message is a direct message to the bot
    elif message.guild is None:  # DMs do not have a guild attribute
        print(f"Direct message received from {message.author}: {message.content}")

        if has_guid(author_id):        
            print(f"User GUID {author_id}: {get_guid(author_id)}")
            

        
        if(message.content == "Hello" or message.content == "!Hello"):
            await message.author.send("Hello! How can I help you?")
            
        if(string_stripped == "!IsAdmin"):
            bool_is_admin = is_admin(author_id)
            if bool_is_admin:
                await message.author.send("You are an admin.")
            else:
                await message.author.send("You are not an admin.")
        if (string_stripped == "!WhoAdmin"):
            string_admins_list=  "Admins are: " + str(ADMIN_DISCORD_USER_ID)
            await message.author.send(string_admins_list)
            

        try_to_push_valide_integer(string_stripped)
        if (message.content == "MetaMask" or message.content == "metamask" or message.content == "🦊"):
            # Generate GUID 
            guid = uuid.uuid4()
            text = "Please sign the given message from here:\n"
            text += "https://eloistree.github.io/SignMetaMaskTextHere/index.html?q="
            text += str(guid)
            dictionary_guid_to_sign[author_id] = guid
            await message.author.send(text)
          
        elif has_guid(author_id) :
            string_message_text= message.content.strip()
            string_guid= str(get_guid(author_id))
            if string_message_text.find(string_guid) == 0 and string_message_text.find("|") >0:
                print("Start with guid:",string_message_text.find(string_guid))
                print("Splitter found:",string_message_text.find("|"))
                #if string_message_text.find(string_guid) == 0 and  string_message_text.find("|") >0:
                if verify_signature_from_text(string_message_text):
                    split_message = string_message_text.split("|")
                    
                    await message.author.send("Signature is verified")
                    record_author_as_meta_mask_user_verified(author_id,split_message[1])
                    #Add it to the database or file system
                else:
                    await message.author.send("Signature is not verified")
                dictionary_guid_to_sign[author_id] = ""
            
            
    # Allow other commands to process
    await bot.process_commands(message)


bot.run(token)
