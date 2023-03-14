import openai
import random
import nextcord
from nextcord.ext import commands
# next cord documentation: https://docs.nextcord.dev/en/stable/

# this function is all chatGPT stuff


def getNpc(characteristics):
    openai.api_key = "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"
    MODEL = "gpt-3.5-turbo"
    # temperature is the variable that sets how complex the response can be the higher the number the higher the complexity
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


# discord api key to identify the bot
botkey = "MTA4NTIyNzk4OTAxMDIzMTM1Ng.GTZKt0.aB5C3kzfPD3uYehwfuOgAn8LlmPsV2SrZ8YEVk"
bot = commands.Bot()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# guild id is the channel id I assume there is a way to set this dynamically but I just did it manually since there are only so many
# channels where I might use the bot


@bot.slash_command(guild_ids=[639278542382694401, 348564060846948363, 934954222829584435, 878487240383295549])
async def npc(interaction: nextcord.Interaction, characteristics: str):
    # defer the response, so we can take a long time to respond, by default discord give you 3 seconds to send a response
    await interaction.response.defer()
    # call getNpc to generate the character this takes about 5-10 seconds usually sometimes longer
    npc = getNpc(characteristics)
    # followup must be used after defer since a response is already sent this updates the message to include the generated character
    await interaction.followup.send(npc)

bot.run(botkey)
