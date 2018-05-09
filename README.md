# pair-programming-switcher README
Python script to let students know when they should switch between driver and navigator

## Dependencies
* Python 3
* Zelle's Graphics library: http://mcsp.wartburg.edu/zelle/python/graphics.py
  * Put in the same directory as the pairProgramming.py script
* Uses threading and datetime

## Running
Run using `python3 pairProgramming.py`

## Customizing

Edit the constants near top of program


ROLE_INTERVAL=6 # time in the role, in minutes

DELAY=.5  # notify students of role change, in minutes

DRIVER="Driver"

DRIVER_DESC="controls keyboard, mouse"

NAVIGATOR="Navigator"

NAVIGATOR_DESC="reviews, questions, strategizes"

LABEL_FONT_SIZE=36

ROLE_FONT_SIZE=36

DESC_FONT_SIZE=16
