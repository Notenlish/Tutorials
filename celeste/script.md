
# PARTS
1 - basic project setup
2 - creating the particle class
3 - Updating particles to move and to repeat 
4 - Sin and cos

##  Basic Script
Hello everyone!

today we are going to create wind                              [Start showing wind from Celeste]
similiar to the wind in Celeste using pygame and python
Let's start with the project

## Installing dependencies
In order to get started, we need to install pygame-ce which is a version of pygame that has all the features of regular pygame, has some speed improvements and has some extra features.

To install it, we need to open the terminal and type `pip uninstall pygame` and then `pip install pygame-ce`
If It asks you to install some dependencies, type `y` and press enter
Also, you might need to prefix these commands with `python -m` or `python3 -m`

## Part 1 - Basic project setup
Now that we have installed pygame-ce, we can initialize our project
I'm going to create a file named main.py
lets import pygame
 

# TODO when writing the code
* After Installing pygame-ce theres nothing that
* explain why we add -100 and +100 in the particle border things(its because if we do it right at the border since our particles have a radius thats bigger than 1 it will seem like they immediately disappear. 
To prevent this I'm going to add -100 or +100 to these calculations.



use `black` for formatting
use `isort` for import order formatting
define stuff that will be added to the class in the class init too(yani self.dt'ı sadece loopda değil __init__'de de tanımla
pygame.display.update()  should be in main loop it shouldnt be abstracted away in the draw func
class parameter type hints
keyword arguments when creating a class instance


# I should mention in yt comments:
cmd: 
`(python(3) -m) pip uninstall pygame`
`(python(3) -m) pip install pygame-ce`

for _ in range():
    _ is used when we dont care about the variable
    for example in this case we dont care about the variable so we use _ instead of a variable name
