#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge # ROS package for converting between ROS image messages & OpenCV
import cv2

def main():
    rospy.init_node('camera_sim_node', anonymous=True)
    img_publisher = rospy.Publisher('eyes/camera/raw_img', Image, queue_size=5)
    rate = Rospy.rate(10)

    bridge = CvBridge()

    while not rospy.is_shutdown():
        # read image from sim_imgs folder
        camera_img = cv2.cvtColor(cv2.imread('sim_imgs/sunflower.jpg'), cv2.COLOR_BGR2RGB)
        
        # convert to a img msg using cv_bridge
        ros_img = bridge.cv2_to_imgmsg(camera_img, encoding="rgb8")

        # publish image to 'eyes/camera/raw_img'
        image_pub.publish(ros_img)

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
