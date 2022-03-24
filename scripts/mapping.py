#!/usr/bin/env python
import rospy
import random
from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ModelState
from math import pow, atan2, sqrt


class TurtleBot:

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot3_burger', anonymous=True)

        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('cmd_vel',
                                                  Twist, queue_size=10)
        self.rate = rospy.Rate(1)

    def move(self, velocity, rotation, iteration):
        vel_msg = Twist()

        for _ in range(iteration):
            # Linear velocity in the x-axis.
            vel_msg.linear.x = velocity[0]
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            vel_msg.angular.x = velocity[1]
            vel_msg.angular.y = 0
            vel_msg.angular.z = rotation

            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()           

try:
    x = TurtleBot()
    i = 0
    while not rospy.is_shutdown():
        randx = random.random() + 0.5
        x.move((0, 0), randx, 2)
        x.move((0, 0), 0, 1)
        x.move((0.2, 0), 0, 15)
        x.move((0, 0), 0, 1)
        x.move((-0.4, 0), 0, 1)
        x.move((0, 0), 0, 1)
        i+=1
        print("Iteration: %s"%(i))

    print("Done!")

except rospy.ROSInterruptException:
    pass