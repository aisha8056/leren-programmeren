from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

counter = 9
while counter > 0:
    robotArm.grab()
    for i in range(0, counter):
        robotArm.moveRight()
    counter -= 1
    robotArm.drop()
    for i in range(0, counter):
        robotArm.moveLeft()
    counter -= 1
robotArm.wait()


#Draai de volgorde van de blokken om.

#Je mag maximaal 15 regels code gebruiken inclusief de import, het laden van de robotarm en de wait