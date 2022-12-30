import os
import json

### Config

alt_chord = "ALT"
shift_chord = "SHEUFT"
super_chord = "WEUPB"
ctrl_chord = "KR-LT"

### Code

LONGEST_KEY = 5

# Chars abc...z + ABC...Z
chars = [chr(x) for x in list(range(65, 91)) + list(range(97, 123))]

nums = map(str, range(10))

allowed_chars = list(chars) + list(nums)

allowed_chords = nums

with open('/home/johannes/.local/share/plover/main.json', 'r') as f:
    main_dict = json.load(f)

# TODO: Lookup chords for allowed chars, and send the appropriate control
# TODO: Add arrow keys as allowed Chars
# TODO: Figure out best code structure such that I can check for all combinations of modifer keys
# TODO: Somehow check for conflicting strokes.
def lookup(outline):
  if len(outline) < 2:
      raise KeyError

  if outline[1] not in allowed_chords:
    raise KeyError

  os.system(f"notify-send '{outline}'")

  if len(outline) == 2:
      if outline[0] == ctrl_chord:
        return "{#Control_L(" + outline[1] + ")}"
      elif outline[0] == super_chord:
        return "{#Super_L(" + outline[1] + ")}"
      elif outline[0] == alt_chord:
        return "{#Meta_L(" + outline[1] + ")}"
      elif outline[0] == shift_chord:
        return "{#Shift_L(" + outline[1] + ")}"
  else:
    raise KeyError

