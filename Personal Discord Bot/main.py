import discord
from discord.ext import commands
from googlesearch import search

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Login as bot : {bot.user.name}')

@bot.command()
async def chao(message):

    if message.author == bot.user:
        return
    user_name = message.author.display_name
    greeting_message = f"Hello, **{user_name}**!"
    await message.send(greeting_message)

@bot.command()
async def helper(ctx):
    user_name = ctx.author.display_name
    help_message = f"""
    **!chao** -> Sends the hello message.
    **!google** -> Does a Google search.
    **!info** -> Shows user info.
    **!helper** -> Shows the help command.
    I hope these are enough **{user_name}**.
    """
    await ctx.send(help_message)

@bot.command()
async def google(ctx, *, query):
    search_results = list(search(query, num_results=1))

    if search_results:
        first_result = search_results[0]
        await ctx.send(f"Here is the result of your search : {first_result}")
    else:
        await ctx.send("Sorry, no search results found.")

@bot.command()
async def info(ctx, member: discord.Member):
    roles = member.roles[1:]
    role_names = [role.name for role in roles]
    guild = member.guild
    user_info = f"**USERNAME** : {member.name}\n**TAGS** : {member.discriminator}\n**ID** : {member.id}\n**ROLES** : {', '.join(role_names)}\n**HOSTING** : {guild.name} (ID: {guild.id})"
    await ctx.send(user_info)

bot.run('MTE1MzI2NDcyNTUyMjY1MzIyNA.GmX9wL.3gJIe6gshpkQGyXZsc3jsfN0GJ6R4HNGbpqu3Q') 
