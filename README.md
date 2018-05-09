# pair-programming-switcher README
Python script to let students know when they should switch between driver and navigator, both visually and audibly.  The program displays a screen, telling the students what their roles should be--either driver or navigator--depending on if they're sitting on the left or right of their partner. Every ROLE_INTERVAL (currently 6 because my intro course works on small problems) minutes, the script will beep twice and notify students that they should switch roles.  The switch roles screen displays for 30 seconds (another constant).  Then, the screen displays the new roles for the students.

## Dependencies
* Python 3
* Zelle's Graphics library: http://mcsp.wartburg.edu/zelle/python/graphics.py
  * Put in the same directory as the pairProgramming.py script
* Uses threading and datetime

## Running
Run using `python3 pairProgramming.py`

## Customizing

**Edit the constants near top of program**


ROLE_INTERVAL=6 # time in the role, in minutes

DELAY=.5  # notify students of role change, in minutes

DRIVER="Driver"

DRIVER_DESC="controls keyboard, mouse"

NAVIGATOR="Navigator"

NAVIGATOR_DESC="reviews, questions, strategizes"

LABEL_FONT_SIZE=36

ROLE_FONT_SIZE=36

DESC_FONT_SIZE=16
