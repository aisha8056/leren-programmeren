from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
for a in range(6):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight(2)
    
for b in range(6):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait() 

#Je mag maximaal 11 regels code gebruiken inclusief de import, het laden van de robotarm en de wait
#Verplaats iedere stapel één plek naar links.