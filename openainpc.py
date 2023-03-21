import openai
import random
import nextcord
from nextcord.ext import commands
import config
# next cord documentation: https://docs.nextcord.dev/en/stable/

# this function is all chatGPT stuff


def bhaifai(statement):
    openai.api_key = config.openaikey
    MODEL = "gpt-3.5-turbo"
    # temperature is the variable that sets how complex the response can be the higher the number the higher the complexity
    temperature = 0.5
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are playing in a 5th edition dungeon and dragons game.  Your character is a Tortle Barbarian named Bhaif who is a sailor aboard a vessel in the astral sea.  Bhaif is extremely dumb and speaks/moves slowly when out of combat but is fiercly loyal if Comodore Krux tells him to do something he does it immediately without question or negotiation. As people speak to you or the dm asks you things you should answer as Bhaif relevant to each person who speaks to him, his companions are named Aynthea, Evendur, Korya, and Willow. During combat Bhaif usually starts turn one by raging which takes a bonus action keep in mind you need to follow the rules of 5e dungeons and dragons for a level 7 barbarian.  Your weapon of choice is a hammer. The DM will handle rolling dice for you."},
            {"role": "user", "content": statement}
            # {"role": "system", "content": "You are a dungeons and dragons dm creating non player characters in your world most of the time your non player characters dont have character classes but instead have occupations"},
            # {"role": "user", "content": "Create a backstory for a non-player character in my Dungeons and Dragons game who has the following characteristics:" + characteristics +
            #     ". This character should have an occupation that makes sense given their background and personality. Please avoid making them a blacksmith unless it's the most fitting occupation based on the provided information."}
        ],
        temperature=temperature,
    )
    return response['choices'][0]['message']['content']


def rule(question):
    openai.api_key = config.openaikey
    MODEL = "gpt-3.5-turbo"
    # temperature is the variable that sets how complex the response can be the higher the number the higher the complexity
    temperature = 0.5
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are the dungeon master for a fifth edition dungeons and dragons game, your players are all new and don't understand how to play the game. Answer their questions as completely and accurately as possible."},
            {"role": "user", "content": "Answer this question: " + question}
            # {"role": "system", "content": "You are a dungeons and dragons dm creating non player characters in your world most of the time your non player characters dont have character classes but instead have occupations"},
            # {"role": "user", "content": "Create a backstory for a non-player character in my Dungeons and Dragons game who has the following characteristics:" + characteristics +
            #     ". This character should have an occupation that makes sense given their background and personality. Please avoid making them a blacksmith unless it's the most fitting occupation based on the provided information."}
        ],
        temperature=temperature,
    )
    return response['choices'][0]['message']['content']


def getNpc(characteristics):
    openai.api_key = config.openaikey
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


bot = commands.Bot()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# guild id is the channel id I assume there is a way to set this dynamically but I just did it manually since there are only so many
# channels where I might use the bot


@bot.slash_command(description="Enter desired characteristics using commas between each. (e.g. race human, profession barber)", guild_ids=[639278542382694401, 348564060846948363, 934954222829584435, 878487240383295549])
async def npc(interaction: nextcord.Interaction, characteristics: str):
    # defer the response, so we can take a long time to respond, by default discord give you 3 seconds to send a response
    await interaction.response.defer()
    # call getNpc to generate the character this takes about 5-10 seconds usually sometimes longer
    npc = getNpc(characteristics)
    # followup must be used after defer since a response is already sent this updates the message to include the generated character
    await interaction.followup.send(npc + " \n\nCharacteristics specified: " + characteristics)


@bot.slash_command(description="Type a rules question", guild_ids=[639278542382694401, 348564060846948363, 934954222829584435, 878487240383295549])
async def rules(interaction: nextcord.Interaction, question: str):
    # defer the response, so we can take a long time to respond, by default discord give you 3 seconds to send a response
    await interaction.response.defer()
    # call getNpc to generate the character this takes about 5-10 seconds usually sometimes longer
    answer = rule(question)
    # followup must be used after defer since a response is already sent this updates the message to include the generated character
    await interaction.followup.send("Question asked: " + question + "\n\n" + answer)


@bot.slash_command(description="Please format statement like this <character name> says <statement directed towards Bhaif>", guild_ids=[639278542382694401, 348564060846948363, 934954222829584435, 878487240383295549])
async def bhaif(interaction: nextcord.Interaction, statement: str):
    # defer the response, so we can take a long time to respond, by default discord give you 3 seconds to send a response
    await interaction.response.defer()
    # call getNpc to generate the character this takes about 5-10 seconds usually sometimes longer
    answer = bhaifai(statement)
    # followup must be used after defer since a response is already sent this updates the message to include the generated character
    await interaction.followup.send("Statement Given: " + statement + "\n\n" + answer)
bot.run(config.botkey)
