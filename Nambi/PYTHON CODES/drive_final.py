#!/usr/bin/env python
import rospy
from arm.msg import Pwm
from sensor_msgs.msg import Joy
import sys
import math


class Arm:
	def __init__(self):
		rospy.init_node("Drive_Publisher")
		self.pub = rospy.Publisher("setup",Pwm,queue_size=1)
		#self.pub = rospy.Publisher('robotic_arm', Pwm,queue_size=1)  

		self.rate = rospy
		rospy.Subscriber("j0", Joy, self.joyCallback)
		self.setup = Pwm()

	def main(self):
		r = rospy.Rate(4)
		while not rospy.is_shutdown():
			self.pub.publish(self.setup)
			print(self.setup)
			print('\n ------- \n')
			r.sleep()

	""" def inverseKinematics(self):
		length1 = 34
		length2 = 38

		rad_angle2 = math.acos(((x**2)+ (y**2) - (length1**2) - (length2**2)) / (2*length1*length2))
		rad_angle1= math.atan(y / x) - math.atan((length2*(math.sin(rad_angle2))) / (length1+ length2*(math.cos(rad_angle2))))

		self.set.shoulder_angle= (rad_angle1*180)/math.pi
		self.set.elbow_angle= (rad_angle2*180)/math.pi	
 """
	""" def ForwardKinematics(self):
		length1 = 34
		length2 = 38

		rad_angle1 = (self.set.shoulder_angle*math.pi)/180
		rad_angle2 = (self.set.elbow_angle*math.pi)/180
		x = length1 * math.cos(rad_angle1) +length2 * math.cos(rad_angle1 + rad_angle2)
		y = length1 * math.sin(rad_angle1) +length2 * math.sin (rad_angle1 + rad_angle2)
       """

	def joyCallback(self, msg):

		#rt/bt
		# if(abs(msg.axes[2]) > 0):
		# 	self.set.base = 200 - (200.0*msg.axes[2])
		# else:
		# 	self.set.base = 0
		
		# if(abs(msg.axes[5]) > 0):
		# 	self.set.base = - int(200 - (200.0*msg.axes[5]))
		# else:
		# 	self.set.base = 0	

		


		global x
		x = 38
		global y 
		y = 34

		
		# left side axis up/down for elbow
		if(abs(msg.axes[1]) > 0.2):
			self.setup.elbow_angle = int(200.0*msg.axes[1])
		        self.setup.shoulder_angle = int(200.0*msg.axes[1])
		elif(abs(msg.axes[1]) < -0.2):
			self.setup.elbow_angle = int(200.0*msg.axes[1])
		        self.setup.shoulder_angle = int(200.0*msg.axes[1])

        # left side axis left/right for shoulder
		elif(abs(msg.axes[2]) > 0.2):
			self.setup.elbow_angle = int(200.0*msg.axes[2])
		        self.setup.shoulder_angle = int(-200.0*msg.axes[2])
		elif(abs(msg.axes[2]) < -0.2):
			self.setup.elbow_angle = int(200.0*msg.axes[2])
		        self.setup.shoulder_angle = int(-200.0*msg.axes[2])
		else:
			self.setup.elbow_angle = 0
	                self.setup.shoulder_angle = 0
	

'''
        # Computing angle 2 Elbow up/down 
		numerator = ((length1 + length2)**2) - ((x**2) + (y**2))
		denominator = ((x**2) + (y**2)) - ((length1 - length2)**2)
		angle2UP = math.degrees(math.atan(math.sqrt(numerator/denominator)))
		angle2DOWN = angle2UP * -1
		#self.set.shoulder_angle
        #self.set.elbow_angle
        # Angle 1 Elbow up
		numerator = (length2 * math.sin(math.radians(angle2UP)))
		denominator = ((length1 + length2) * math.cos(math.radians(angle2UP)))
		angle1UP = math.degrees(math.atan2(numerator, denominator))
        # Angle 1 Elbow down
		numerator = (length2 * math.sin(math.radians(angle2DOWN)))
		denominator = ((length1 + length2) * math.cos(math.radians(angle2DOWN)))
		angle1DOWN = math.degrees(math.atan2(numerator, denominator))
		print("Angle 1 Elbow up: " + str(angle1UP))
		print("Angle 1 Elbow down: " + str(angle1DOWN))
		print("Angle 2 Elbow up: " + str(angle2UP))
		print("Angle 2 Elbow down: " + str(angle2DOWN))		
'''    
			
if __name__ == '__main__':
	x = Arm()
	x.main()
	rospy.spin()

