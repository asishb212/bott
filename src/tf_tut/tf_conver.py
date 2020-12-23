#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

roll = math.radians(30)
pitch = math.radians(42)
yaw = math.radians(58)

print(roll,pitch,yaw)

quaterion=tf.transformations.quaternion_from_euler(roll,pitch,yaw)
print(quaterion)

rpy=tf.transformations.euler_from_quaternion(quaterion)
print(rpy)
