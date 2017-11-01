#! /usr/bin/env python
# -*- encoding: UTF-8 -*-



from Tkinter import *
import sys
import argparse
import qi
from naoqi import ALProxy


def main(robotIP):
   PORT = 9559

   
   try:
        awarenessProxy = ALProxy("ALBasicAwareness", robotIP, PORT)
        print "worked"
   except Exception, e:
        print "Could not create proxy "
        print "Error was: ", e

   # things the robot can react to
   # try setting some to false and see what you prefer
   awarenessProxy.setStimulusDetectionEnabled("Sound", True)
   awarenessProxy.setStimulusDetectionEnabled("Movement", True)
   awarenessProxy.setStimulusDetectionEnabled("People", True)
   awarenessProxy.setStimulusDetectionEnabled("Touch", True)

   # levels of engagement may also be relevant
   
   # “Unengaged”: (Default mode) when the robot is engaged with a user, it can be distracted by any stimulus, and engage with another person.
   # “FullyEngaged”: as soon as the robot is engaged with a person, it stops listening to stimuli and stays engaged with the same person.
   #                 If it loses the engaged person, it will listen to stimuli again and may engage with a different person.
   # “SemiEngaged”: when the robot is engaged with a person, it keeps listening to the stimuli, and if it gets a stimulus,
   #                it will look in its direction, but it will always go back to the person it is engaged with. If it loses the person,
   #                it will listen to stimuli again and may engage with a different person.

   awarenessProxy.setEngagementMode("FullyEngaged")
    
if __name__ == "__main__":

    robotIp = "10.218.111.27"

    if len(sys.argv) <= 1:
        print "Usage python robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]
    main(robotIp)