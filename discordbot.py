from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='a!')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@bot.event
async def on_ready():
await bot.change_presence(activity=discord.Game(f"a!help")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def botver(ctx):
    await ctx.send('あきかきbot 1.0')

@bot.command()
async def suyaxa(ctx):
    await ctx.send('( ˘ω˘ )')

@bot.command()
async def botURL(ctx):
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=805315041259814913&permissions=0&scope=bot<-をcopy')

@bot.command()
async def nube(ctx):
    await ctx.send('( ˘ω˘)ｽﾔｧなのにヌベスコとか常識はずれにもほどがあるでしょｗｗｗｗｗｗｗ')
    
@bot.command()
async def aki(ctx):
    await ctx.send('秋柿様')
    
bot.run(token)
