# Pair Programming Timer
# Tells students about their role and when to switch roles.
# by Sara Sprenkle, 02/2018

from graphics import *
from time import sleep
from threading import Timer, active_count
from datetime import *

ROLE_INTERVAL=6 # time in the role, in minutes
DELAY=.5  # notify students of role change, in minutes
DRIVER="Driver"
DRIVER_DESC="controls keyboard, mouse"
NAVIGATOR="Navigator"
NAVIGATOR_DESC="reviews, questions, strategizes"
LABEL_FONT_SIZE=36
ROLE_FONT_SIZE=36
DESC_FONT_SIZE=16

def main():
    win = GraphWin("Pair Programming!", 650, 400)
    win.setBackground("white")
    
    # rectangle
    rectangle = Rectangle( Point(0, 0), Point( win.getWidth()/2, win.getHeight()))
    rectangle.setFill("yellow")
    rectangle.setOutline("pink")
    rectangle.draw(win)
    
    # left label
    leftPoint = Point( win.getWidth()/4, 100)
    leftText = Text( leftPoint, "Left")
    leftText.setStyle("bold")
    leftText.setSize(LABEL_FONT_SIZE)
    leftText.setFace("arial")
    leftText.setTextColor(color_rgb( 100, 100, 100) )
    leftText.draw(win) 
    
    # left description - starts as driver
    leftdPoint = Point( win.getWidth()/4, 250)
    leftdText = Text( leftdPoint, DRIVER )
    leftdText.setStyle("bold")
    leftdText.setSize(ROLE_FONT_SIZE)
    leftdText.setFace("arial")
    leftdText.draw(win)

    leftd2Point = Point(win.getWidth()/4, 300)
    leftd2Text = Text( leftd2Point, DRIVER_DESC )
    leftd2Text.setSize(DESC_FONT_SIZE)
    leftd2Text.setFace("arial")
    leftd2Text.draw(win)
    
    # right label
    rightText = leftText.clone()
    rightText.move(win.getWidth()/2, 0)
    rightText.setText("Right")
    rightText.draw(win) 
    
    # right description - starts as navigator
    rightdText = leftdText.clone()
    rightdText.move(win.getWidth()/2,0)
    rightdText.setText(NAVIGATOR)
    rightdText.draw(win)

    rightd2Text = leftd2Text.clone()
    rightd2Text.move(win.getWidth()/2,0)
    rightd2Text.setText(NAVIGATOR_DESC)
    rightd2Text.draw(win)
    
    
    # switching information
    switchNote = Rectangle( Point(0,0), Point(win.getWidth(), win.getHeight()) )
    switchNote.setFill("black")
    
    switchText = Text( Point(win.getWidth()/2, win.getHeight()/2), "SWITCH ROLES!")
    switchText.setFace("arial")
    switchText.setSize(LABEL_FONT_SIZE)
    switchText.setStyle("bold")
    switchText.setTextColor("white")
    
    # use to alternate between screens
    count = 0
    
    while True:
        t = Timer( ROLE_INTERVAL * 60, datetime.now)
        t.start()
        t.join()
        print(datetime.now())
        
        print("Switching!")
    
        switchNote.draw(win)
        switchText.draw(win)
        beep()

        
        t = Timer( DELAY * 60, print, [count])
        t.start()
        t.join()
        
        # Switch the roles displayed
        
        if count % 2 == 0:
            rightdText.setText(DRIVER)
            rightd2Text.setText(DRIVER_DESC)
            leftdText.setText(NAVIGATOR)
            leftd2Text.setText(NAVIGATOR_DESC)
            rectangle.move(win.getWidth()/2, 0)
        else:
            rightdText.setText(NAVIGATOR)
            rightd2Text.setText(NAVIGATOR_DESC)
            leftdText.setText(DRIVER)
            leftd2Text.setText(DRIVER_DESC)
            rectangle.move(-win.getWidth()/2, 0)
    
        switchNote.undraw()
        switchText.undraw()
        
        count += 1
    
    win.getMouse()
    win.close()

def beep():
    """ Plays two beeps in succession. """
    for x in range(2):
        print('\a')
        sleep(.3)

main()
