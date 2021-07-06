import random

import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")
client.remove_command("help")

filtered_words = ["nigga", "nigger", "n i g g e r", "N i g g e r", "Nigger", "n i g g a", "Nigga", "N i g g a"]

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('Moderating 1 server ;('))
	print("NotABot is ready")

@client.group(invoke_without_command = True)
async def help(ctx):
	em = discord.Embed(title = "Help", description = "Use >help <command> for extended information on a command.",color = ctx.author.color )

	em.add_field(name = "Moderation", value = "kick,ban,unban,mute,unmute,purge")
	em.add_field(name = "Fun", value = "_8ball")
	em.add_field(name = "Info", value = "whois")


	await ctx.send(embed = em)


@help.command()
async def kick(ctx):

	em = discord.Embed(title = "Kick", description = "Kicks a member from the guild",color = ctx.author.color)

	em.add_field(name = "**Syntax**", value = ">kick <member> [reason]")

	await ctx.send(embed = em)



@help.command()
async def ban(ctx):

	em = discord.Embed(title = "Ban", description = "Bans a member from the guild",color = ctx.author.color)

	em.add_field(name = "**Syntax**", value = ">Ban <member> [reason]")

	await ctx.send(embed = em)



@help.command()
async def unban(ctx):

	em = discord.Embed(title = "Unban", description = "Unbans a member from the guild",color = ctx.author.color)

	em.add_field(name = "**Syntax**", value = ">Unban <member_name> <discriminator>")

	await ctx.send(embed = em)



@help.command()
async def mute(ctx):

	em = discord.Embed(title = "Mute", description = "Mute's a member from the guild",color = ctx.author.color)

	em.add_field(name = "**Syntax**", value = ">Mute <member>")

	await ctx.send(embed = em)



@help.command()
async def unmute(ctx):

	em = discord.Embed(title = "Unmute", description = "Unmute's a member from the guild",color = ctx.author.color)

	em.add_field(name = "**Syntax**", value = ">Unmute <member>")

	await ctx.send(embed = em)



@help.command()
async def purge(ctx):

	em = discord.Embed(title = "Purge", description = "Deletes message/s")

	em.add_field(name = "**Syntax**", value = ">Purge <amount of messages you want deleted including your's>")

	await ctx.send(embed = em)




@help.command()
async def _8ball(ctx):

	em = discord.Embed(title = "8ball", description = "8 ball answers your questions its a god that answers all of your questions if they are right or not")

	em.add_field(name = "**Syntax**", value = ">8ball <question>")

	await ctx.send(embed = em)




@help.command()
async def whois(ctx):

	em = discord.Embed(title = "Whois", description = "Whois shows you the info about the server member like avatar id and things.")

	em.add_field(name = "**Syntax**", value = ">Whois <member.meniton>")

	await ctx.send(embed = em)

	

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
  responses = [
  discord.Embed(title='It is certain.'),
  discord.Embed(title='It is decidedly so.'),
  discord.Embed(title='Without a doubt.'),
  discord.Embed(title='Yes - definitely.'),
  discord.Embed(title='You may rely on it.'),
  discord.Embed(title='Most likely.'),
  discord.Embed(title='Outlook good.'),
  discord.Embed(title='Yes.'),
  discord.Embed(title='Signs point to yes.'),
  discord.Embed(title='Reply hazy, try again.'),
  discord.Embed(title='Ask again later.'),
  discord.Embed(title='Better not tell you now.'),
  discord.Embed(title='Cannot predict now.'),
  discord.Embed(title='Concentrate and ask again.'),
  discord.Embed(title="Don't count on it."),
  discord.Embed(title='My reply is no.'),
  discord.Embed(title='My sources say no.'),
  discord.Embed(title='Outlook not very good.'),
  discord.Embed(title='Very doubtful.')
    ]
  responses = random.choice(responses)
  await ctx.send(content=f'Question: {question}\nAnswer:', embed=responses)    

@client.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)              

@client.command()
async def hello(ctx):
	await ctx.send("Hello mother fu**er :)")

@client.command(aliases = ['c'])
@commands.has_permissions(manage_messages = True)
async def purge(ctx,amount = 2):
	await ctx.channel.purge(limit = amount)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
	await member.kick(reason = reason)
	await ctx.send(member.name + " has been kicked")

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason = reason)
	await ctx.send(member.name + " has been banned")

@client.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
			return



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing a required argument you fu*king retard :).  Do >help")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the permissions to run this command you idiot :).")
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have sufficient permissions!")
    else:
        print("error not caught")
        print(error) 

@client.command()
@commands.has_permissions(kick_members = True)
async def mute(ctx, member : discord.Member):
	muted_role = ctx.guild.get_role(860977839728754710)

	await member.add_roles(muted_role)

	await ctx.send(member.mention + " has been muted")

@client.command()
@commands.has_permissions(kick_members = True)
async def unmute(ctx, member : discord.Member):
	muted_role = ctx.guild.get_role(860977839728754710)

	await member.remove_roles(muted_role)

	await ctx.send(member.mention + " has been unmuted")



@client.event
async def on_message(msg):
	for word in filtered_words:
		if word in msg.content:
			await msg.delete()

	await client.process_commands(msg)


		
client.run("ODYxMTMzMTM1MjE0OTM2MDY0.YOFWug.UyB0Udr49dMOUeTGVF9tteWjlpg")