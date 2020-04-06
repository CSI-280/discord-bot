import discord
from discord.ext import commands

###################### BOT RELATED STUFF ######################

extensions = [
    "cogs.basic",
    "cogs.errors",
    "cogs.utils",
    "cogs.games.tictactoe",
    "cogs.games.hangman"
]


def get_prefix(bot, message):
    """Gets the server prefix."""
    return "!"


bot = commands.Bot(command_prefix=get_prefix,
                   help_command=None)  # creates bot object

###################### QUEUES ######################

tictactoe_q = set()  # holds players current playing tictactoe


###################### HELP RELATED STUFF ######################

def get_help(p):
    """Places prefixes into a help dictionary."""
    return {
        "help": {
            "title": "Pandora's Bot Help",
            "description": (f"Table of Contents\n"
                            f"To go to another page please use `{p}help <page>`\n"
                            f"Example `{p}help 1`, `{p}help setup`"),
            "fields": {"1. Commands": "General, Non-game related commands",
                       "-----------------------------": "[Github](https://github.com/CSI-280/Pandoras-Bot)"}

        },
        "commands": {
            "title": "Pandora's Bot General Commands",
            "description": f"on a specific command you can use `{p}help <command>`",
            "fields": {
                "General Commands":
                    (f"`{p}howdy`: You've got a friend in me\n"
                     f"`{p}prefix`: Not yet implemented"),
            }

        }
    }
