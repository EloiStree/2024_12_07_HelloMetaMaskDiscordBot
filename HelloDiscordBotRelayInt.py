
# pip install discord.py
# pip install audioop-lts
import socket
import struct
import uuid
import discord
from discord.ext import commands
import os

# pip install web3
from web3 import Web3
from hexbytes import HexBytes
from eth_account.messages import encode_defunct

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
    


# Define the path to the bot token file
token_file_path = "bot_token.txt"

# Display the absolute path of the token file
print("Path:", os.path.abspath(token_file_path))

# Check if the token file exists; if not, create it with a placeholder URL
if not os.path.exists(token_file_path):
    print("Creating a default file at that path")
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
SALON_ID = 1222573438187737100 ## TWITCH PLAY CHAT
SALON_ID= 1223448265492795454 ## TWITCH PLAY CHAT CONFERENCE

# Bot Setup
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.dm_messages = True
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)
admin_role_name = "Admin"  # Replace with your admin role name


    
    
print("Signed:",verify_signature_from_text("c538b4d2-4a3b-4756-8471-dbe9dfbc96d2|0xFEEAcdE5d735B8b347D9BBF8fBd02FEd153b564A|0x79dc5d03c0ac6fda591997a03fa6fd1a4876f6308813115edd4d0b8b5aecee2b67f29f20157e6427566cfcc7b9d52362ff5005c9dd2628bdfe904c39bfab85d31b"))

# Check for Admin Role
def is_admin(ctx):
    if ctx.guild:  # Ensure the command is in a guild context
        return any(role.name == admin_role_name for role in ctx.author.roles)
    return False  # No roles exist in DM context


@bot.command()
async def listen(ctx, *, message):
    if is_admin(ctx):
        await ctx.send(f"Listening to: {message}")
    else:
        await ctx.send("You don't have permission to use this command.")


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


def push_integer_to_server(integer):
    ivp4 = "192.168.1.37"
    port = 7073
    index=1
    print(f"Pushing integer {integer} to server {ivp4}:{port}")
    byte = struct.pack("<ii", index, integer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(byte, (ivp4, port))
    sock.close()

def try_to_push_valide_integer(text):
    if text == "0":
        push_integer_to_server(0)
    else:
        try:
            integer = int(text)
            push_integer_to_server(integer)
            return True
        except ValueError:
            return False

# Event: Triggered when a message is sent in the server or as a DM
@bot.event
async def on_message(message):
    # Ignore bot's own messages to avoid an infinite loop
    
    if message.author == bot.user:
        return
    
    
    string_stripped = message.content.strip()
    author_id= message.author.id

    # Check if the message is in the specified server and channel
    if message.guild and message.channel.id == SALON_ID:
        print(f"Message received in channel {SALON_ID}: {message.content}")
        try_to_push_valide_integer(string_stripped)
        #await message.channel.send(f"Hello {message.author.mention}, I see your message: {message.content}")
    # Check if the message is a direct message to the bot
    elif message.guild is None:  # DMs do not have a guild attribute
        print(f"Direct message received from {message.author}: {message.content}")

        if has_guid(author_id):        
            print(f"User GUID {author_id}: {get_guid(author_id)}")

        
        if(message.content == "Hello"):
            await message.author.send("Hello! How can I help you?")

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
                    await message.author.send("Signature is verified")
                else:
                    await message.author.send("Signature is not verified")
            
            
    # Allow other commands to process
    await bot.process_commands(message)


bot.run(token)
