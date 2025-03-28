
# 	Ground-Challenge
## A Multi-sensor SLAM Dataset	Focusing on Corner Cases for Ground Robots



<div align=center>
   
[![Author](https://img.shields.io/badge/Author-Jie%20Yin-blue)](https://sjtuyinjie.github.io/)
[![Paper](https://img.shields.io/badge/Paper-GroundChallenge-yellow)](https://ieeexplore.ieee.org/document/10354969/)
[![Preprint](https://img.shields.io/badge/Preprint-Arxiv-purple)](https://arxiv.org/abs/2307.03890)
[![License](https://img.shields.io/badge/License-MIT-cyan)]()
[![News](https://img.shields.io/badge/News-orange)](https://mp.weixin.qq.com/s/jnfVFOXX6aiqGBX6pVdgIg)
   
<img src="fig/scenarios.jpg" width="800px">

</div>
<p align="center">Figure 1. Different corner cases for SLAM</p>


## Notice: 
### We strongly recommend that the newly proposed SLAM algorithm be tested on our Ground-Challenge benchmark, because our data has following features:

1. A rich pool of sensory information including RGBD, wheel, IMU and so on.
   
2. This benchmark includes diverse corner cases such as aggressive motion, severe occlusion, changing illumination, few textures, pure rotation, motion blur, wheel suspension, etc.

  
3. This benchmark brings great challenge to existing cutting-edge SLAM algorithms including VINS-Mono, [ORB-SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3), [VINS-RGBD](https://github.com/STAR-Center/VINS-RGBD), [VIW-Fusion](https://github.com/TouchDeeper/VIW-Fusion) and [TartanVO](https://github.com/castacks/tartanvo). If your proposed algorihm outperforms SOTA systems on this dataset, your paper will be much more convincing and valuable.



## License

The paper link is [here](https://arxiv.org/abs/2307.03890).If you use Ground-Challenge in an academic work, please cite:
~~~
@inproceedings{yin2023ground,
  title={Ground-challenge: A multi-sensor slam dataset focusing on corner cases for ground robots},
  author={Yin, Jie and Yin, Hao and Liang, Conghui and Jiang, Haitao and Zhang, Zhengyou},
  booktitle={2023 IEEE International Conference on Robotics and Biomimetics (ROBIO)},
  pages={1--5},
  year={2023},
  organization={IEEE}
}
~~~

## ABSTRACT:

We introduce Ground-Challenge: a novel dataset collected by a ground robot with multiple sensors including an RGB-D camera, an inertial measurement unit (IMU), a wheel odometer and a 3D LiDAR to support the research on corner cases of visual SLAM systems.
Our dataset comprises 36 trajectories with diverse corner cases such as aggressive motion, severe occlusion, changing illumination, few textures, pure rotation, motion blur, wheel suspension, etc. Some state-of-the-art SLAM algorithms are tested on our dataset, showing that these systems are seriously drifting and even failing on specific sequences.
We will release the dataset and relevant materials upon paper publication to benefit the research community.










## 1.SENSOR SETUP
### 1.1 Acquisition Platform
The ground robot is given below. The unit of the figures is centimeter.

<div align=center>
<img src="fig/robot.jpg" width="600px">
</div>

<p align="left">Figure 2. The data capture robot.</p>









### 1.2 Sensor parameters

All the sensors and track devices and their most important parameters are listed as below:

* **LIDAR** Velodyne VLP-16, 360 Horizontal Field of View (FOV),-30 to +10 vertical FOV,10Hz,Max Range 200 m,Range Resolution 3 cm, Horizontal Angular Resolution 0.2°.  

* **V-I Sensor**,Realsense d435i,RGB/Depth 640*480,69H-FOV,42.5V-FOV,15Hz;IMU 6-axix, 200Hz  
* **IMU**,Xsens Mti-300,9-axis,400Hz;  
* **Wheel Odometer**,AgileX,2D,25Hz;  

The rostopics of our rosbag sequences are listed as follows:

* LIDAR: `/velodyne_points` 

* V-I Sensor:  
`/camera/color/image_raw `,  
`/camera/depth/image_raw `,  
`/camera/imu`

* IMU: `/imu/data `
 
* Wheel Odometer: `/odom `

## 2.DATASET SEQUENCES


> [!TIP]
>  We are delighted to see that many users enjoy our Ground-Challenge dataset. However, **due to an overwhelming number of download requests, OneDrive has become unstable. If you encounter any issues, please wait for about 10 minutes and try again.**



An overview of Ground-Challenge is given in the table below:
Scenario|Darkroom|Occlusion|Office|Room|Wall|Motionblur|Hall|Loop|Roughroad|Corridor|Rotation|Static|Slope|TOTAL
--|:--|:--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:
Number |3|4|3|3|3|3|3|2|3|2|3|2|2|36
Dist/m |92.0|273.8|75.5|102.1|86.7|166.6|236.3|371.8|68.1|164.3|12.4|1.9|128.5|1780.0
Duration/s |203.6|334.2|164.0|154.7|189.3|145.5|302.4|332.7|186.3|198.1|183.2|92.6|195.0|2681.6
Size/GB|6.1|9.9|4.7|4.6|5.6|4.3|8.7|9.9|5.4|5.8|5.4|2.7|5.7|78.8


### 2.1 Visual Challenges

  <div align=center>
  
  
Sequence Name|Total Size|Duration|Features|Rosbag
--|:--|:--:|--:|--:
Darkroom1|2.9g|100s|slight light, going into a room|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EfJ_m0MD1upOphD5vnCoqSoBJ54_5D_vQQD0hpAwAq0qPg?e=1tmbgq)
Darkroom2|2.3g|76s|sharp turn|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EU4Ns3qCDO5PkjByuoANpf4BRWksqGt_pDnEnKXbbdz9Sw?e=AX5bp4)
Darkroom3|1.9g|64s|slight light|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EU2tnWCQitJOiRmNeHaCmtEBG2HssIMag9DRUrJOmYYxUQ?e=2dXfFr)
Occlusion1|2.9g|97s|moving feet, far features|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EfpLxjCNp8ZHvpFEnItwvhABQbwCsvcr1kmUtsnpM4fqiw?e=tA6KpT)
Occlusion2|3.2g|108s|hand occlusion|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EaAZkIssBohOkjpCyUzx_-8BrngUTuuOyJVz5IPGqdEhQg?e=Sv8uQi)
Occlusion3|2.6g|89s|hand occlusion|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/Ef9vHhDNZh5Drk5dwzL3dLgBX9-_1XkQxqrIpOHR7C57aw?e=FeA8Yo)
Occlusion4|1.2g|40s|complete occlusion|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EVFiMlWRhydNukCylXGganoB_w-DJ-7PzBB7Y_cXiWvBGw?e=WZtsNP)
Office1|1.3g|46s|exposure change|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EaBHPzN4EuBOu-X-l52sfQMBnsjYnksgxDbWVzOMy-sxIQ?e=splygr)
Office2|1.9g|66s|going into a dark room|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EcBQ7EME7JNKuXpcyoitWbcBc_okPBGVl_LJhUhtRF7lyg?e=G7FgMx)
Office3|1.5g|52s|office|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EVcZ-4q2s_RPqcpIX2LM70EBvUlGw9O8eiHzDjIadLko6A?e=NIf9jb)
Room1|1.3g|46s|exposure change|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EcrkgZ7gyv1KnpNWajEXzNIBFaJOZzODtIxtMSWgm45RxA?e=zAZlRJ)
Room2|1.9g|66s|going into a dark room|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EeHeiCiRCUVAj8pyOTAO0NcBfdhO_BQJUeUNMGfLTKXcbg?e=lLLkkp)
Room3|1.5g|52s|office|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/Eek7te0hlThHpdU61IdMWZsBxv4Sty-7ofFAFQZRa9HGPA?e=WWU85c)
Motionblur1|1.5g|52s|aggressive motion|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EVGUofZ_fd1IugqiyFQcV94BVL5qTyNA7HTOkZJNDKTiVw?e=CsRWmn)
Motionblur2|1.6g|54s|aggressive motion|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EeplJdHLC9tMkbN3rXqvc0oBuw5CaRlR7EuxYEBrNnJ9ig?e=lGybNv)
Motionblur3|1.2g|40s|aggressive motion|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EWMqyAlMP8hHmHTab36MkLIB3C_0X6N0n7ARrdSoPBvm1g?e=MBMXbJ)
Wall1|1.7g|59s|wall in a corridor|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EU15i59tJHxHgBmWZZwvMMkBaNVA37ulgy_Hrk8mP7jyOg?e=6c6hn7)
Wall2|2.0g|66s|wall in a big hall|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EcHTwIhL6Q9Ao9UEtYknrLgBRxK_AyToEPwyfZNrt2PDMg?e=AzPYe4)
Wall3|3.9g|65s|wall in a corridor|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/ERaf7TV8R2hBljLdGOIRnRQBGwba8YPYoaJrp4WvytByog?e=k175KG)
  </div>
  
### 2.2 Wheel Challenge

   <div align=center>

Sequence Name|Total Size|Duration|Features|Rosbag
--|:--|:--:|--:|--:
Hall1|2.6g|91s|slippery ground, a reflective surface|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EbRe8o9pakFCvmjSKEgOEc0BglOJgScs0IbHFcxr84Fxig?e=WjkQQM)
Hall2|3.2g|110s|slippery ground, a reflective surface|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EYSOrLJ0yRdLrUwH2HIej0kB53Lnwf7TuouMDO-TY-Pkrw?e=dlwBMs)
Hall3|2.9g|101s|slippery ground, walking human|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/ES5vEb2oe1hAqMVQY3LfgqMBXPlNazdu9B__0R0j3cwyhg?e=yTNLH7)
Loop1|4.1g|97s|moving feet, far features|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EU9mhOpXfEJBm-M0cwbhTwsBL_WvjwkO-GcTzPnmwa-OkQ?e=qPPqGR)
Loop2|5.8g|137s|hand occlusion|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/ER_ZcyUZN3dNiwkxT-NeqEoBbphpoCbLnsf5ARp52ARdjA?e=Z3quXF)
Roughroad1|2.2g|75s|rough road|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EX-Yic1OhN1GjrcGoaE2mu0BTua8w3C8PvRzMa0rsm84pQ?e=fb4Kb4)
Roughroad2|1.5g|52s|rough road|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EV-gMKCrnbFFmGLU5FV32loB-OMys7O3dZ25InJR0aH-0Q?e=Xp8Fmy)
Roughroad3|1.8g|59s|rough road|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EcJemetJZMBPnJwlXNwCySkBTGhc5QXRlTo0fOEFF0uWfQ?e=KuX3EH)

</div>



  

  
### 2.3 Specific Movement Patterns
  <div align=center>
  
Sequence Name|Total Size|Duration|Features|Rosbag
--|:--|:--:|--:|--:
Corridor1|2.9g|100s|zigzag, long corridor|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/Ed4KpGMgT2RMgzqt0HU0fw8BOvtgx18YnkdJQVekzwfe8g?e=5S9uLK)
Corridor2|2.9g|98s|straight forward, long corridor|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EcWKsukr7nNLrqKloXY3UAIBKakA6ppET_SGJZT-VCYO5Q?e=Ccp0fd)
Rotation1|1.6g|53s|moving feet, far features|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EeYXHDYMNYNDoMocs1YBj34B3TvYSQtDqV8JjAel37uL9Q?e=upMCTa)
Rotation2|2.1g|73s|hand occlusion|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/ET-YIfqH2n1Fv0mlx2nO3QEBScAuV01IGn_GqgTQyHFcpA?e=X9zdoB)
Rotation3|1.7g|57s|rough road|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EX1DtN9we2lDlhTPkG4NaZsBSyOkPGuqfgJxz2o0WwxjFQ?e=EBweG6)
Static1|1.6g|56s|rough road|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EbAEddIfZqhFglNNf5urVmcB9lFue_HuhJ1_bxwNnxvCGQ?e=eCSfal)
Static2|1.1g|37s|rough road|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EUy-egIJ3vVMu0Kpc8Q92AcB8UU6x_FvogsvFrclhIme2g?e=WtYGQl)
Slope1|2.8g|96s|slope|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/ETR6Sbd7PltEvzggPaa0DdoBwgo3PbsUWNjwBTnckX5MTA?e=sgfRI5)
Slope2|2.9g|99s|slope|[Rosbag](https://sjtueducn-my.sharepoint.com/:u:/g/personal/594666_sjtu_edu_cn/EQ6TUsSfrBdAiAljY8o2HLEBj62PzAp2g0c4XKcQtvHg0A?e=iKrk3m)
</div>

## 3. Configuration Files
We provide configuration files for several cutting-edge baseline methods, including [VINS-RGBD](https://github.com/sjtuyinjie/Ground-Challenge/tree/main/config_files_gc/vinsrgbd),[TartanVO](https://github.com/sjtuyinjie/Ground-Challenge/tree/main/config_files_gc/tartanvo),[VINS-Mono](https://github.com/sjtuyinjie/Ground-Challenge/tree/main/config_files_gc/vinsmono) and [VIW-Fusion](https://github.com/sjtuyinjie/Ground-Challenge/tree/main/config_files_gc/viwfusion).


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=sjtuyinjie/Ground-Challenge&type=Timeline)](https://star-history.com/#Ashutosh00710/github-readme-activity-graph&Timeline)

