from Gamepad import XboxController
from MotorControl import MotorControl
import time

## Define Pins
LEFT_PWM = 12
LEFT_FORWARD = 16
LEFT_BACKWARD = 21
LEFT_ACTIVE = 20

RIGHT_PWM = 13
RIGHT_FORWARD = 19
RIGHT_BACKWARD = 6
RIGHT_ACTIVE = 26


if __name__ == '__main__':
    joy = XboxController()
    LeftMotor = MotorControl(LEFT_PWM, LEFT_FORWARD, LEFT_BACKWARD, LEFT_ACTIVE)
    RightMotor = MotorControl(RIGHT_PWM, RIGHT_FORWARD, RIGHT_BACKWARD, RIGHT_ACTIVE)

    active = False
    aButtonLastState = 0
    aButtonClicked = False
    xButtonLastState = 0
    xButtonClicked = False
    controlMode = 0
    directionLeft = 0
    leftDirectionLastButtonState = 0
    leftDirectionButtonclicked = False
    directionright = 0
    rightDiretionLastButtonState = 0
    rightDiretionButtonClicked = False
    while True:
        array = joy.readControl()
        
        aButton = array[6] #return [leftTrigger, leftStick, directionLeft, rightTrigger, rightStick, directionRight, a, x]
        if aButtonLastState == 0 and aButton == 1:
            aButtonClicked = True
        elif aButtonLastState == 1  and aButton ==0 : 
            aButtonClicked == False

        if not active and aButtonClicked:
            active = True
        elif active and aButtonClicked:
            active = False

        aButtonLastState = aButton

        xButton = array[7]
        if xButtonLastState == 0 and xButton == 1:
            xButtonClicked = True 
        elif xButtonLastState == 1 and xButton == 0:
            xButtonClicked = False

        if controlMode == 0 and xButtonClicked:
            controlMode = 1
        elif controlMode == 1 and xButtonClicked:
            controlMode = 0
        xButtonLastState = xButton

        if controlMode == 0:
            leftDirection = array[2]
            if leftDirectionLastButtonState == 0 and leftDirection == 1:
                leftDirectionButtonclicked = True
            else :
                leftDirectionButtonclicked = False
            
            leftDirectionLastButtonState = leftDirection

            if directionLeft == 0 and leftDirectionButtonclicked:
                directionLeft = 1
            elif directionLeft == 1 and leftDirectionButtonclicked:
                directionLeft = 0

            rightDirection = array[5]
            if rightDiretionLastButtonState == 0 and rightDirection == 1:
                rightDiretionButtonClicked = True
            else:
                rightDiretionButtonClicked = False
            
            rightDiretionLastButtonState = rightDirection

            if directionright == 0 and rightDiretionButtonClicked:
                directionright = 1
            elif directionright == 1 and rightDiretionButtonClicked:
                directionright = 0
        else:
            directionLeft = 0
            directionright = 0

        if active and controlMode == 0:
            
            LeftMotor.setDirection(directionLeft)
            speedLeft = array[0]
            LeftMotor.setSpeed(speedLeft)

            RightMotor.setDirection(directionright)
            speedRight = array[3]
            RightMotor.setSpeed(speedRight)

            if speedLeft > .05 :
                LeftMotor.startMotor()
            else:
                LeftMotor.stopMotor

            if speedRight > 0.05: 
                RightMotor.startMotor()
            else:
                RightMotor.stopMotor()
        time.sleep(2)
        