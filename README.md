# Ground-Challenge

<div align=center>
<img src="fig/scenarios.jpg" width="800px">

</div>
<p align="center">Figure 1. Different scenarios</p>






## NOTICE
### We strongly recommend that the newly proposed SLAM algorithm be tested on our data, because our data has following features:
1. A  rich pool of sensory information including vision, lidar, IMU, GNSS,event, thermal-infrared images and so on
2. Various scenarios in real-world environments including lifts, streets, rooms, halls and so on.
3. Our dataset brings great challenge to existing SLAM algorithms including LIO-SAM and ORB-SLAM3. If your proposed algorihm outperforms SOTA systems on M2DGR, your paper will be much more convincing and valuable.


## ABSTRACT:

The research on visual SLAM (Simultaneous Localization and Mapping) algorithms has made great progress in recent years, and the centimeter-level accuracy has been achieved by state-of-the-art algorithms in some scenarios. However, there is still some way off towards their practical deployment in service robots. The reason is that existing SLAM algorithms is developed under the assumption that the robot moves in a certain way in a static, texture-filled environment. Nonetheless, some corner cases or sensor failures in real applications might easily fail these systems. Therefore, challenging datasets are vital for further SLAM development. In this paper, we introduce Ground-Challenge: a novel dataset collected by a ground robot with multiple sensors including a RGBD camera, an inertial measurement unit (IMU), a wheel odometer and a 3D LiDAR.
Our dataset comprises 21 trajectories (over 500G) in diverse scenarios such as aggressive motion, severe occlusion, poor exposure, changing illumination, few textures, rough roads, pure rotation, motion blur, and wheel suspension. Some state-of-the-art SLAM algorithms are tested on our dataset, and results show that these systems are seriously drifting and even failing on some sequences.

## MAIN CONTRIBUTIONS:
* We collected long-term challenging sequences for ground robots both indoors and outdoors with a complete sensor suite, which includes six surround-view fish-eye cameras, a sky-pointing fish-eye camera, a perspective color camera, an event camera, an infrared camera, a 32-beam LIDAR, two GNSS receivers, and two IMUs. To our knowledge, this is the first SLAM dataset focusing on ground robot navigation with such rich sensory information.
* We recorded trajectories in a few challenging scenarios like lifts, complete darkness, which can easily fail existing localization solutions. These situations are commonly faced in ground robot applications, while they are seldom discussed in previous datasets.
* We launched a comprehensive benchmark for ground robot navigation. On this benchmark, we evaluated existing state-of-the-art SLAM algorithms of various designs and analyzed their characteristics and defects individually.


## Video
[![ICRA2022 Presentation](cover.png)](https://www.youtube.com/watch?v=73enWUwxJ1k)



For Chinese users, try [![bilibili](cover.png)](https://www.bilibili.com/video/BV1q3411G7iF/)









## 1.LICENSE
This work is licensed under MIT license. International License and is provided for academic purpose. If you are interested in our project for commercial purposes, please contact us on 1195391308@qq.com for further communication. 

If you face any problem when using this dataset, feel free to propose an issue. And if you find our dataset helpful in your research, simply give this project a 
. 

The paper has been accepted by both [RA-L](https://www.ieee-ras.org/publications/ra-l/) and [ICRA 2022](https://icra2022.org/). A preprint version of the paper in [Arxiv](https://arxiv.org/abs/2112.13659) and [IEEE RA-L](https://ieeexplore.ieee.org/document/9664374).If you use M2DGR in an academic work, please cite:
~~~
@ARTICLE{9664374,
  author={Yin, Jie and Li, Ang and Li, Tao and Yu, Wenxian and Zou, Danping},
  journal={IEEE Robotics and Automation Letters}, 
  title={M2DGR: A Multi-sensor and Multi-scenario SLAM Dataset for Ground Robots}, 
  year={2021},
  volume={},
  number={},
  pages={1-1},
  doi={10.1109/LRA.2021.3138527}}
~~~



## 2.SENSOR SETUP
### 2.1 Acquisition Platform
Physical drawings and schematics of the ground robot is given below. The unit of the figures is centimeter.

<div align=center>
<img src="fig/robot.jpg" width="600px">
</div>

<p align="left">Figure 2. The data capture robot.</p>









### 2.2 Sensor parameters

All the sensors and track devices and their most important parameters are listed as below:

* **LIDAR** Velodyne VLP-16, 360 Horizontal Field of View (FOV),-30 to +10 vertical FOV,10Hz,Max Range 200 m,Range Resolution 3 cm, Horizontal Angular Resolution 0.2°.  

* **V-I Sensor**,Realsense d435i,RGB/Depth 640*480,69H-FOV,42.5V-FOV,15Hz;IMU 6-axix, 200Hz  
* **IMU**,Xsens Mti-300,9-axis,400Hz;  


The rostopics of our rosbag sequences are listed as follows:

* LIDAR: `/velodyne_points` 

* V-I Sensor:  
`/camera/color/image_raw `,  
`/camera/depth/image_raw `,  
`/camera/imu`

* IMU: `/imu/data `
 

## 3.DATASET SEQUENCES


**At this stage, we only release part of our data for evaluation. The complete dataset will be made public once this paper is accepted. **



An overview of M2DGR is given in the table below:
Scenario|Darkroom|Occlusion|Office|Room|Wall|Motionblur|Hall|Loop|Roughroad|Corridor|Rotation|Static|TOTAL
--|:--|:--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:
Number |3|4|3|3|3|3|3|2|3|2|3|2|34
Dist/m |92.01|273.77|75.51|102.1|86.68|166.56|236.33|371.76|68.06|164.28|12.38|1.85|1651.29
Duration/s |203.63|334.15|164|154.72|189.31|145.54|302.36|332.73|186.28|198.08|183.16|92.58|2486.54
Size/GB|6.1|9.9|4.7|4.6|5.6|4.3|8.7|9.9|5.4|5.8|5.4|2.7|73.1


### 3.1 Visual Challenges


  
  
 <div align=center>
<img src="fig/" width="400px">
<p align="center">Figure 4. Outdoor Sequences:all trajectories are mapped in different colors.</p>


Sequence Name|Total Size|Duration|Features|Rosbag|GT
--|:--|:--:|--:|--:|--:
Darkroom1|2.9g|100s|slight light, going into a room|[Rosbag](bag)|[GT](gt)
Darkroom2|2.3g|76s|sharp turn|[Rosbag](bag)|[GT](gt)
Darkroom3|1.9g|64s|slight light|[Rosbag](bag)|[GT](gt)
Occlusion1|2.9g|97s|moving feet, far features|[Rosbag](bag)|[GT](gt)
Occlusion2|3.2g|108s|hand occlusion|[Rosbag](bag)|[GT](gt)
Occlusion3|2.6g|89s|hand occlusion|[Rosbag](bag)|[GT](gt)
Occlusion4|1.2g|40s|complete occlusion|[Rosbag](bag)|[GT](gt)
Office1|1.3g|46s|exposure change|[Rosbag](bag)|[GT](gt)
Office2|1.9g|66s|going into a dark room|[Rosbag](bag)|[GT](gt)
Office3|1.5g|52s|office|[Rosbag](bag)|[GT](gt)
Room1|1.3g|46s|exposure change|[Rosbag](bag)|[GT](gt)
Room2|1.9g|66s|going into a dark room|[Rosbag](bag)|[GT](gt)
Room3|1.5g|52s|office|[Rosbag](bag)|[GT](gt)
Motionblur1|1.5g|52s|aggressive motion|[Rosbag](bag)|[GT](gt)
Motionblur2|1.6g|54s|aggressive motion|[Rosbag](bag)|[GT](gt)
Motionblur3|1.2g|40s|aggressive motion|[Rosbag](bag)|[GT](gt)
Wall1|1.7g|59s|wall in a corridor|[Rosbag](bag)|[GT](gt)
Wall2|2.0g|66s|wall in a big hall|[Rosbag](bag)|[GT](gt)
Wall3|3.9g|65s|wall in a corridor|[Rosbag](bag)|[GT](gt)
  </div>
  
### 3.2 Wheel Failure
<div align=center>

<img src="https://github.com/sjtuyinjie/mypics/blob/main/forgithub/lift.jpg" width="400px">

<p align="left">Figure 5. Lift Sequences:The robot hang around a hall on the first floor and then went to the second floor by lift.A laser scanner track the trajectory outside the lift</p>
  

Sequence Name|Total Size|Duration|Features|Rosbag|GT
--|:--|:--:|--:|--:|--:
Hall1|2.6g|91s|slippery ground, a reflective surface|[Rosbag](bag)|[GT](gt)
Hall2|3.2g|110s|slippery ground, a reflective surface|[Rosbag](bag)|[GT](gt)
Hall3|2.9g|101s|slippery ground, walking human|[Rosbag](bag)|[GT](gt)
Loop1|4.1g|97s|moving feet, far features|[Rosbag](bag)|[GT](gt)
Loop2|5.8g|137s|hand occlusion|[Rosbag](bag)|[GT](gt)
Roughroad1|2.2g|75s|rough road|[Rosbag](bag)|[GT](gt)
Roughroad2|1.5g|52s|rough road|[Rosbag](bag)|[GT](gt)
Roughroad3|1.8g|59s|rough road|[Rosbag](bag)|[GT](gt)
</div>



  

  
### 3.3 Specific Motion Patterns
  <div align=center>
  
Sequence Name|Total Size|Duration|Features|Rosbag|GT
--|:--|:--:|--:|--:|--:
Corridor1|2.9g|100s|zigzag, long corridor|[Rosbag](bag)|[GT](gt)
Corridor2|2.9g|98s|straight forward, long corridor|[Rosbag](bag)|[GT](gt)
Rotation1|1.6g|53s|moving feet, far features|[Rosbag](bag)|[GT](gt)
Rotation2|2.1g|73s|hand occlusion|[Rosbag](bag)|[GT](gt)
Rotation3|1.7g|57s|rough road|[Rosbag](bag)|[GT](gt)
Static1|1.6g|56s|rough road|[Rosbag](bag)|[GT](gt)
Static2|1.1g|37s|rough road|[Rosbag](bag)|[GT](gt)
</div>

## 4. CONFIGURERATION FILES
For convenience of evaluation, we provide configuration files of some well-known SLAM systems as below:

[A-LOAM](https://github.com/sjtuyinjie/toolkit/blob/main/config_files/aloam/aloam_velodyne_HDL_32.launch),

[LeGO-LOAM](https://github.com/sjtuyinjie/toolkit/blob/main/config_files/legoloam/run.launch),

[LINS](https://github.com/sjtuyinjie/toolkit/blob/main/config_files/lins/exp_port.yaml),

[LIO-SAM](https://github.com/sjtuyinjie/toolkit/blob/main/config_files/liosam/params.yaml),

[VINS-MONO](https://github.com/sjtuyinjie/toolkit/blob/main/config_files/vins/mytest.launch),

[ORB-Pinhole](https://github.com/sjtuyinjie/toolkit/blob/main/config_files/orb3/paperd435i.yaml),

[ORB-Fisheye](https://github.com/sjtuyinjie/toolkit/blob/main/config_files/orb3/paperleft.yaml),

[ORB-Thermal](https://github.com/sjtuyinjie/toolkit/blob/main/config_files/orb3/paperthermal.yaml),

[CUBMAPSLAM](https://github.com/sjtuyinjie/toolkit/blob/main/config_files/cubemapslam/runCubemapstreet_06.sh)

## 5.DEVELOPMENT TOOLKITS
### 5.1 Extracting Images
* For rosbag users, first make image view
~~~
roscd image_view
rosmake image_view
sudo apt-get install mjpegtools
~~~

open a terminal,type roscore.And then open another,type
~~~
rosrun image_transport republish compressed in:=/camera/color/image_raw raw out:=/camera/color/image_raw respawn="true"
~~~
* For non-rosbag users,just take advantage of following script  [export_tum](https://github.com/sjtuyinjie/toolkit/blob/main/export_tum.py),[export_euroc](https://github.com/sjtuyinjie/toolkit/blob/main/export_euroc.py) and [get_csv](https://github.com/sjtuyinjie/toolkit/blob/main/img2csv.py) to get data in formats of Tum or EuRoC.

### 5.2 Evaluation
We use open-source tool [evo](https://github.com/MichaelGrupp/evo) for evalutation.
To install evo,type
~~~
pip install evo --upgrade --no-binary evo
~~~
To evaluate monocular visual SLAM,type
~~~
evo_ape tum street_07.txt your_result.txt -vaps
~~~
To evaluate LIDAR SLAM,type
~~~
evo_ape tum street_07.txt your_result.txt -vap
~~~
To test GNSS based methods,type
~~~
evo_ape tum street_07.txt your_result.txt -vp
~~~

### 5.3 Calibration
For camera intrinsics,visit [Ocamcalib](http://sites.google.com/site/scarabotix/ocamcalib-toolbox) for omnidirectional model.
visit [Vins-Fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion) for pinhole and MEI model.
use [Opencv](https://opencv.org/) for Kannala Brandt model

For IMU intrinsics,visit [Imu_utils](https://github.com/gaowenliang/imu_utils)

For extrinsics between cameras and IMU,visit [Kalibr](https://github.com/ethz-asl/kalibr)
For extrinsics between Lidar and IMU,visit [Lidar_IMU_Calib](https://github.com/APRIL-ZJU/lidar_IMU_calib) 
For extrinsics between cameras and Lidar, visit [Autoware](https://github.com/Autoware-AI/autoware.ai) 
### 5.4 Getting RINEX files
For GNSS based methods like [RTKLIB](http://www.rtklib.com/),we usually need to get data in the format of RINEX. To make use of GNSS raw measurements, we use [Link](https://github.com/TakahashiJinxu/ublox2rinex) toolkit.

### 5.5 ROS drivers for UVC cameras 
We write a ROS driver for UVC cameras to record our thermal-infrared image. 
[UVC ROS driver](https://github.com/sjtuyinjie/toolkit/tree/main/thermal_ws/src)


## 6.FUTURE PLANS
In the future, we plan to update and extend our project from time to time, striving to build a comprehensive SLAM benchmark similar to the KITTI dataset for ground robots.
### If you have any suggestions or questions, do not hesitate to propose an issue. And if you find our dataset helpful in your research, a simple star is the best affirmation for us.

## 7.ACKNOWLEGEMENT
This work is supported by NSFC(62073214). Authors from SJTU hereby express our appreciation.

