"""
These are basic functions that help
karel do basic tasks without putting
multiple commands like move()

instead of move() on 3 lines just do 
f_move(3)

paste this at the top of ur code hs editor

"""
def f_move(num=1): # repeated move function
    for i in range(1, num+1):
        move()

def f_left(num=1): # repeated left function
    for i in range(1, num+1):
        turn_left()
    
def f_right(num=1): # repeated right function
    for i in range(1, num+1):
        f_left(3)

def f_place(num=1): # repeated place ball func
    for i in range(1, num+1):
        put_ball()

def f_take(num=1): #repeated pickup func
    for i in range(1, num+1):
        take_ball()

def f_rotate(num=1): #repeated rotate (180)
    for i in range(1,num+1):
        f_left(2)
    
def f_backflip(num=1): #repeated 360
    for i in range(1, num+1):
        f_left(4)
