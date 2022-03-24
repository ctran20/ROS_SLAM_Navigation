#!/usr/bin/env python
import rospy
import actionlib
import roslib
import tf
from nav_msgs.msg import Odometry
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

rospy.init_node('turtlebot3_burger')

def move_to_point(point):
	client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
	client.wait_for_server()

	goal = MoveBaseGoal()

	# Set coordinate
	goal.target_pose.header.frame_id = "odom"
	goal.target_pose.header.stamp = rospy.Time.now()
	goal.target_pose.pose.position.x = point[0]
	goal.target_pose.pose.position.y = point[1]
	quaternion = tf.transformations.quaternion_from_euler(0.0, 0.0, 0.0)

	goal.target_pose.pose.orientation.x = quaternion[0]
	goal.target_pose.pose.orientation.y = quaternion[1]
	goal.target_pose.pose.orientation.z = quaternion[2]
	goal.target_pose.pose.orientation.w = quaternion[3]

	client.send_goal(goal)
	wait = client.wait_for_result()
	if not wait:
		rospy.logerr("Action server not available!")
		rospy.signal_shutdown("Action server not available!")
	else:
		return client.get_result()

def main():
	print("Heading to Point A...")
	move_to_point((3.45, -4.55))
	print("Heading to Point B...")
	move_to_point((-7.35, -2.2))
	print("Heading to Point C...")
	move_to_point((-7.2, 4.6))
	print("Heading to Point D...")
	move_to_point((4.35,5.3))
	print("Finished!")

main()