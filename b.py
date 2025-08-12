import discord
import os
from discord.ext import commands
import requests

API_URL = 'http://127.0.0.1:5000/announce'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def 공지(ctx, *, 내용):
    data = {"message": 내용}
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            await ctx.send("인게임 공지가 성공적으로 전송되었어요!")
        else:
            await ctx.send("공지 전송에 실패했어요.")
    except Exception as e:
        await ctx.send(f"오류 발생: {e}")

@bot.event
async def on_ready():
    print(f'봇 로그인 성공: {bot.user}')

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
