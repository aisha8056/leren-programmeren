from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:

for step in range(7):
    robotArm.moveRight()
for box in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    if box < 7:
        for b in range(2):
            robotArm.moveLeft()





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait() 
