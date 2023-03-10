from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:

for step in range(0, 5): #how many times arm will move right
    robotArm.moveRight()#if step is lower than 4 it'll then do the code underneath
    for box in range(0, 6):#how many times itll pick up a box 
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    if step < 4:
        robotArm.moveRight()
    
robotArm.wait()



#Verplaats iedere stapel één plek naar links.