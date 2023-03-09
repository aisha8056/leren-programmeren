from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

teller = 9
robotArm.speed = 3
while teller < 10 and teller > 0:
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "red":
        for i in range(0, teller):
            robotArm.moveRight()
        robotArm.drop()
        teller -= 1
        for i in range(0, teller):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
        teller -= 1
robotArm.wait()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait() 
