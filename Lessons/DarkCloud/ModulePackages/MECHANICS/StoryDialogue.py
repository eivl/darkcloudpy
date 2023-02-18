# speech system
def darkspeech(speaker: str, line: int):
  # docstring
  """ # darkspeech()
  Allows NPCS to speak and display the storyline within the game, Two parameters allow this. 'speaker' and 'line'.
  """
  
  # receive dialogue from file w/open() functionality
  with open(r'GenesisGir-Lessons-VOL.4\Lessons\DarkCloud\resources\STORY SCRIPTS\DarkCloudStoryScript.txt', 'r') as f:
    
    speech = f.readline(line) # contains string data from script
    dialogue = print(f"{speaker}: {speech}") # the dialogue from the speaker and data from script
    return dialogue
    pass
  pass