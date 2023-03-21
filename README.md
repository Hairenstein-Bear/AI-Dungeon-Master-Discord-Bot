# AI-Dungeon-Master-Discord-Bot
Discord bot written in python that makes a call to the chatGPT api and returns a custom generated output.

Current Features and commands:

"/npc":   Create NPC  Enter desired characteristics for best results seperate characteristic type with commas.
--------------------------------------------
"/rules":  Answer questions about the rules  Enter question about a feature or spell, still a work in progress it works but Chat GPT confuses rules sometimes
when they interact with each other especially in regards to action economy, perhaps with more training or more precise prompting before the query is sent it
could be more accurate.
--------------------------------------------
Play as a missing party member **very early work in progress** "/bhaif": the command is in reference to the PC who was late to the game but will eventually
be changed to something more relevant.  Eventually after logging characteristics, alliances, and personality in a config file chat gpt can respond how the 
player would normally respond to each situation.  
--------------------------------------------

Long term feature: Utilize Chat GPT and Discord API to have a continuous conversation and allow Chat GPT to guide a group of players through a AI generated DND
session. Early testing directly with Chat GPT current UI seems positive.  With the right prompting it can create a storyline its biggest problems funnily enough
is it forgets to only control the NPCs and tries to narrate the entire thing before accepting input.
