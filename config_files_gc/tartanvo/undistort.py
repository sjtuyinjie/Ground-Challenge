# coding:utf-8
# !/usr/bin/python

# Extract images from a bag file.

# PKG = 'beginner_tutorials'
import roslib  # roslib.load_manifest(PKG)
import rosbag
import rospy
import cv2
import numpy as np
import os
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
from matplotlib import pyplot as plt
# Reading bag filename from command line or roslaunch parameter.
# import os
import sys



path='/media/car/YJ06/ground-challenge/bag/'  # bag包路径, /结尾
filename='loop2'
topic_names={'rgb_topics':['/camera/color/image_raw'], 'depth_topics':[]}
# cameras=['camera1','camera2']


cam_rgb_path=[path+'/rgbd/'+filename+'/rgb/']
cam_depth_path=[path+'/rgbd/'+filename+'/depth/']

# for camPath in cam_rgb_path:
#     print(camPath)
if os.path.exists(path+filename+'.bag'):
    for path_dir in cam_rgb_path:
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
    for path_dir in cam_depth_path:
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
else:
    print('bag file not exist!!')
    sys.exit()

file=open(cam_rgb_path[0]+"/time.txt", "w")
print(cam_rgb_path[0]+"/time.txt")

# 相机内参和畸变系数
camera_matrix = np.array([[620.97277909374247, 0, 311.75896455154810],
                          [0, 622.12293397677581, 247.18077836114819],
                          [0, 0, 1]])
dist_coeffs = np.array([0.14865749308203452, -0.46815685578576460, 0.0016205585303208318, -0.0089101576735577930, 0])
seqnum=0
class ImageCreator():
    def __init__(self):
        self.bridge = CvBridge()
        print("Waiting......")
        
        global seqnum

        with rosbag.Bag(path+filename+'.bag','r') as bag:  # 要读取的bag文件；
            for topic, msg, t in bag.read_messages():
                for i in range(len(topic_names['rgb_topics'])):
                    if topic == topic_names['rgb_topics'][i]:  # 图像的topic；
                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
                            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)  # 转换为灰度图
                            # 应用去畸变
                            undistorted_image = cv2.undistort(cv_image, camera_matrix, dist_coeffs)
                        except CvBridgeError as e:
                            print(e)
                        timestr = "%.9f" % msg.header.stamp.to_sec()
                        image_name = "{:06d}.png".format(seqnum)
                        seqnum += 1
                        # 保存去畸变后的图像
                        cv2.imwrite(cam_rgb_path[i] + image_name, undistorted_image)
                        seqstr=''
                        if(seqnum<10):
                            seqstr="00000"+str(seqnum)
                        elif (seqnum<100):
                            seqstr="0000"+str(seqnum)
                        elif (seqnum<1000):
                            seqstr="000"+str(seqnum)
                        elif (seqnum<10000):
                            seqstr="00"+str(seqnum)
                        elif (seqnum<100000):
                            seqstr="0"+str(seqnum)
                        # with open(cam_rgb_path[0]+"/time.txt", "w")as timestamp_file_rgb:
                        file=open(cam_rgb_path[0]+"/time.txt", "a")
            
                        file.write(seqstr+','+timestr+"\n") 




file.close()

if __name__ == '__main__':
    # rospy.init_node(PKG)
    try:
        image_creator = ImageCreator()
        print("done")
    except rospy.ROSInterruptException:
        pass