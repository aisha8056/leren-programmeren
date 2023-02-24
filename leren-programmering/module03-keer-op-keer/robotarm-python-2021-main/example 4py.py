from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:


for I in range(5):
    robotArm.grab()
    for y in range(2):
        robotArm.moveRight()
    robotArm.drop()
    for g in range(2):
        robotArm.moveLeft()
    
        
for t in range(2):
    robotArm.moveRight()

for repeat in range(5):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()

