from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:

for counter in range(1, 5):
    for i in range(counter):
        robotArm.grab()
        for j in range(4):
            robotArm.moveRight()
        robotArm.drop()
        for j in range(4):
            robotArm.moveLeft()
    robotArm.moveRight()

robotArm.wait()


#Verplaats alle stapels vijf stappen naar rechts.

#Je mag maximaal 12 regels code gebruiken inclusief de import, het laden van de robotarm en de wait
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait() 
