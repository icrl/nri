# -*- encoding: UTF-8 -*-

''' PoseInit: Small example to make Nao go to an initial position. '''

import argparse
from naoqi import ALProxy

def initPos(robotIP, PORT):

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("Sit", 0.5)

    # Go to rest position
    motionProxy.rest()

if __name__ == "__main__":
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    '''
    initPos("10.218.107.156", 9559)