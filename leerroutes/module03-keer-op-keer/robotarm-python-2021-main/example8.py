from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()
for step in range(0, 7):# Loop through 7 times to grab 7 objects
    robotArm.grab()
    for box in range(0,8):# Move the object to the right 8 times
        robotArm.moveRight()
    robotArm.drop()
    for box in range(0,8):# Move the arm back to the left 8 times
        robotArm.moveLeft()
robotArm.wait()



   

#Verplaats de stapel naar de rechterkant.

#Je mag maximaal 11 regels code gebruiken inclusief de import, het laden van de robotarm en de wait
robotArm.wait() 