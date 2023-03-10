from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

counter = 9
robotArm.speed = 3

while counter > 0:
    robotArm.grab()
    kleur = robotArm.scan()

    if kleur == "red":
        for i in range(counter):
            robotArm.moveRight()
        robotArm.drop()
        counter -= 1
        for i in range(counter):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
        counter -= 1

robotArm.wait()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait() 

#Verplaats alle rode blokken naar het einde.

#Let op, de blokken zijn iedere keer anders als je het programma start!
