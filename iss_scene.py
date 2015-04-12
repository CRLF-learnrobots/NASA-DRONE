#This scene can be imported into the Morse Simulator 
#https://www.openrobots.org/wiki/morse/

from morse.builder import *

env = Environment('<path>/<identifier>')

#Going to set variable for drone quadrotor robot
drone = Quadrotor()
morse.builder.morsebuilder.Robot.set_mass(1)
morse.builder.

#Properties
drone.properties(NoGravity=True)

#Actuator
motion = MotionVW()
motion.translate(z=0.3)
motionvw.rotate(.3, .3, .3)
drone.append(motion)

#Sensor
pose = Pose()
pose.translate(z=0.83)
atrv.append(pose)

#Middlewares
pose.add_stream('socket')
pose.add_service('socket')
motion.add_service('socket')