"""
🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂

                      ░██████╗████████╗░█████╗░██████╗░██╗░░░██╗  ███████╗██╗░░░██╗███████╗███╗░░██╗████████╗░██████╗
                      ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝  ██╔════╝██║░░░██║██╔════╝████╗░██║╚══██╔══╝██╔════╝
                      ╚█████╗░░░░██║░░░██║░░██║██████╔╝░╚████╔╝░  █████╗░░╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░╚█████╗░
                      ░╚═══██╗░░░██║░░░██║░░██║██╔══██╗░░╚██╔╝░░  ██╔══╝░░░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░░╚═══██╗
                      ██████╔╝░░░██║░░░╚█████╔╝██║░░██║░░░██║░░░  ███████╗░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░██████╔╝
                      ╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═════╝░

This script holds all the functions/methods that contain the story-mode events that happen within the program 'darkcloud.py' and the storyline and events are created inside this
module and are imported to other modules mainly the 'mainmenu.py' to be called upon with the corrosponding function calls.

🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂
"""

# import modules
from ModulePackages.SOUND.DarkPlayer import DarkPlayer
from ModulePackages.MECHANICS.StoryDialogue import * # speech functionality
from ModulePackages.NPCS.npcs import * # NPCS

# defined story mode events for 'darkcloud.py'
def ceromonyevent():
  # docstring
  """ # ceromonyevent()
  """

  # render the cerononial OST theme song for the ceromonial event
  DarkPlayer.dark_player_ost(filepath=r"GenesisGir-Lessons-VOL.4\Lessons\DarkCloud\resources\Audio Resources\MUSIC\Ceremony.wav")
  
  # Western Dictator Dialogue
  darkspeech(WESTERN_DICTATOR, 4)
  pass