import openai
import io
import time
import random
import asyncio
import nextcord
from nextcord.ext import commands
# or .all() if you ticked all, that is easier


def getNpc(characteristics):
    openai.api_key = "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"
    MODEL = "gpt-3.5-turbo"
    temperature = random.uniform(.5, 1.0)
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a dungeons and dragons dm creating non player characters in your world most of the time your non player characters dont have character classes but instead have occupations"},
            {"role": "user", "content": "Create a backstory for a non-player character in my Dungeons and Dragons game who has the following characteristics:" + characteristics +
                ". This character should have an occupation that makes sense given their background and personality. Please avoid making them a blacksmith unless it's the most fitting occupation based on the provided information."}
        ],
        temperature=temperature,
    )
    return response['choices'][0]['message']['content']


botkey = "MTA4NTIyNzk4OTAxMDIzMTM1Ng.GiaMjN.gVWnrXBFC1-Wa2FV3cEnh2jxH3E5DZIo9wn8XQ"
bot = commands.Bot()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.slash_command(guild_ids=[639278542382694401, 348564060846948363, 934954222829584435, 878487240383295549])
async def npc(interaction: nextcord.Interaction, characteristics: str):
    """Say hi to a user"""
    # defer the response, so we can take a long time to respond
    await interaction.response.defer()
    # do something that takes a long time
    npc = getNpc(characteristics)
    # followup must be used after defer since a response is already sent
    await interaction.followup.send(npc)

bot.run(botkey)
