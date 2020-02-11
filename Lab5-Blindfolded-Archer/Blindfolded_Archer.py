import random as rand
import math

#All measurements in meters and seconds
gravitationConstant = 9.81 #for earth, can be set
dragCoefficient = 0 #can be set
timeStepSize = .00001 #can be set
time = 0
targetXPosition = rand.randint(1, 100) #can change params
targetAcceptanceRange = .5 #distance from center
xPosition = 0
yPosition = 1 #height of shooter, could be set
initialAngle = 45 #can be set
initialMagnitude = 10 #can be set
xVelocity = initialMagnitude * math.cos(math.radians(initialAngle))
yVelocity = initialMagnitude * math.sin(math.radians(initialAngle))
xAcceleration = 0
yAcceleration = -gravitationConstant

while yPosition > 0:
    xPosition = xPosition + (xVelocity * timeStepSize)
    yPosition = yPosition + (yVelocity * timeStepSize)
    xVelocity = xVelocity + (xAcceleration * timeStepSize)
    yVelocity = yVelocity + (yAcceleration * timeStepSize)
    xAcceleration = -dragCoefficient * xVelocity
    yAcceleration = -gravitationConstant + (-dragCoefficient * yVelocity)
    time = time + timeStepSize
