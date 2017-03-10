#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from leap_motion.msg import leap
from leap_motion.msg import leapros

pub = rospy.Publisher("/throttle", Float64)
pub1 = rospy.Publisher("/pitch" ,Float64)
pub2 = rospy.Publisher("/roll" ,Float64)

def callback(data):
    thr = data.palmpos.y
    pub.publish(thr)
    pit = data.palmpos.z
    pub1.publish(pit)
    rol = data.palmpos.x
    pub2.publish(rol)

def send_command():
    rospy.init_node("leap_to_arduino")
    rospy.Subscriber("leapmotion/data", leapros, callback)
    rospy.spin()

if __name__ == '__main__':
    send_command()

