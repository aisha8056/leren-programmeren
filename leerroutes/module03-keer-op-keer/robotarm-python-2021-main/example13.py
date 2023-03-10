from RobotArm import RobotArm

robotArm = RobotArm('exercise 13')

# Jouw python instructies zet je vanaf hier:

robot = RobotArm()
robot.randomLevel(1, 7)

step = 1
while t < 9:
    robot.grab()
    color = robot.scan()
    if color == "":
        robot.wait()
    for i in range(t):
        robot.moveRight()
    robot.drop()
    for i in range(t):
        robot.moveLeft()
    step += 1

robot.wait()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait() 

#Verdeel alle blokken over de lege plaatsen, zodra er geen blokken meer zijn moet de arm stoppen.
