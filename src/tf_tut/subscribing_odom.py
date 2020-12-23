#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import time
from std_srvs.srv import Empty
import tf

def odom_callback(msg):
    print("odom msgd")
    print("x",msg.pose.pose.position.x)
    print("y",msg.pose.pose.position.y)
    print("z",msg.pose.pose.position.z)
    print("vx",msg.twist.twist.linear.x)
    print("vy",msg.twist.twist.linear.y)
    print("vz",msg.twist.twist.linear.z)
    print('qx=',msg.pose.pose.orientation.x)
    print('qy=',msg.pose.pose.orientation.y)
    print('qz=',msg.pose.pose.orientation.z)
    print('qw=',msg.pose.pose.orientation.w)

rospy.init_node('motion_pose',anonymous=True)
rospy.Subscriber("/odom",Odometry,callback=odom_callback)
rospy.spin()
