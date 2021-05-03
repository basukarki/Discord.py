import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">")


@bot.event
async def on_ready():
    activity = discord.Game(name="Learning with basu", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('I am ready')


@bot.command()
async def learn(ctx):
    await ctx.send('**HELLO, IF YOU WANT TO LEARN PYTHON AND OTHER STUFF WITH LIVE CLASSES FOR FREE THEN CONTACT  <@692214510806892601>**')


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clean(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    await user.ban(reason=reason)
    await ctx.send(f"{user} has been ban due to {reason}")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    await user.kick(reason=reason)
    await ctx.send(f"{user} has been kick due to {reason}")


@bot.event
async def on_message(message):
    if message.content.startswith('learn'):
        embedVar = discord.Embed(
            title="ProgramingWithbasu", description="**HERE IN THIS SERVER YOU CAN LEARN PYTHON, C++, C#, JAVA, JS**", color=0x00ff00)
        await message.channel.send(embed=embedVar)


@bot.command()
async def info(ctx, member: discord.Member):
    embed = discord.Embed(
        title=member.name, discription=member.mention, Color=discord.Color.gold())
    embed.add_field(name='ID', value=member.id, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f"{user} has been unbanned sucessfully!")
        return

bot.run('ODM4NjA4NDY0NzAzNzgyOTMy.YI9k_g.ehHCn5cLuxKGpQ_KcDVeltLZGPk')
