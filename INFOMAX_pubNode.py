# (c) daniel ford, daniel.jb.ford@gmail.com

# pose publisher ROS node for infomax robot controller

#!/usr/bin/env python
import roslib; roslib.load_manifest('policySim')
import rospy
from std_msgs.msg import String
from gazebo.msg import ModelState

# gazebo/set_model_state is the topic
# gazebo/ModelState is the message type

def talker():
        #pub = rospy.Publisher('rosout', String)
        pub = rospy.Publisher('gazebo/set_model_state', ModelState)
	msg = ModelState()
        rospy.init_node('falling')
        while not rospy.is_shutdown():

#str = "{model_name: table_model, pose: { position: { x: 0, y: 0, z: 10 }, orientation: {x: 0, y: 0.491983115673, z: 0, w: 0.870604813099 } }, twist: { linear: {x: 0.0 , y: 0 ,z: 0 } , angular: { x: 0.0 , y: 0 , z: 0.0 } } , reference_frame: world } }"

                msg.model_name = "table_model"
                msg.pose.position.x = 0
                msg.pose.position.y = 0
                msg.pose.position.z = 10
#                ModelState.linear.x = 0
#                ModelState.twist.linear.y = 0
#                ModelState.twist.linear.z = 0
#                ModelState.twist.angular.x = 0
#                ModelState.twist.angular.y = 0
#                ModelState.twist.angular.z = 0
                msg.reference_frame = "world"

#		x = 0.; y = 0.; z = 10.

                rospy.loginfo(ModelState)
                #pub.publish(String(str))
                pub.publish(msg)		#should publish x,y,z coords to Gazebo
        
	rospy.sleep(300.0)

if __name__ == '__main__':
        try:
                talker()
        except rospy.ROSInterruptException: pass
