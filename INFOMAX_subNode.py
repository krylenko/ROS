# (c) daniel ford, daniel.jb.ford@gmail.com

# pose subscriber ROS node for infomax robot controller

#!/usr/bin/env python
import roslib; roslib.load_manifest('policySim')
import rospy

#from std_msgs.msg import String
from gazebo.msg import ModelState

def callback(data):
    rospy.loginfo(rospy.get_name())
    print "X pos: ",data.pose.position.x; print "Y pos: ",data.pose.position.y; print "Z pos: ",data.pose.position.z 		

def listener():
    rospy.init_node('listener', anonymous=False)
#    rospy.init_node('listener', anonymous=True)	#for multiple listeners
    rospy.Subscriber('gazebo/set_model_state', ModelState, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
