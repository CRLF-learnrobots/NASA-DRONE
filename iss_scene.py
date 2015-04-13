#This scene can be imported into the Morse Simulator 
#https://www.openrobots.org/wiki/morse/

from morse.builder import *

env = Environment('iss')
env.set_camera_location([-5.0, 5.0, 3.0])
env.set_camera_rotation([1.0470, 0, -0.7854])

#Going to set variable for drone quadrotor robot
drone = drone()
robot.translate(2.0, 3.0, 4.0)
#Properties
drone.properties(NoGravity=True)

#Actuator
motion = MotionVW()
motion.translate(z=0.3)
drone.append(motion)

keyboard = Keyboard()
robot.append(keyboard)
keyboard.properties(ControlType = 'Position')

#Sensor
pose = Pose()
pose.translate(z=0.83)
drone.append(pose)

#Middlewares
pose.add_stream('socket')
pose.add_service('socket')
motion.add_service('socket')
