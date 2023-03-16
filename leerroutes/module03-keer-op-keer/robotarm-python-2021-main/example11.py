from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:

counter = 9

for move in range(9):
    robotArm.moveRight()

for move in range(9):
    robotArm.moveLeft()
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()

    else:
        robotArm.drop()





# for move in range(counter):
#     robotArm.moveLeft()
#     kleur = robotArm.scan()

#     if kleur == 'white':
#         robotArm.moveRight()
#         robotArm.drop()
#         robotArm.moveRight()
#     else:
#         robotArm.drop()
#         robotArm.moveRight()
robotArm.wait()


# # Na jouw code wachten tot het sluiten van de window:
# robotArm.wait()

# #Verplaats alle witte blokken één plek naar rechts. 

# #Let op, de blokken zijn iedere keer anders als je het programma start!