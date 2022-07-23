# Reeborg's World Hurdle 3 Problem

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    while not wall_on_right():
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()
    
        

while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()


#Reeborg's World Maze Problem solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        move() 
