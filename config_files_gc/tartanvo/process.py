#coding:utf-8
# 假设pose.txt和time.txt文件已经存在，下面是读取这两个文件，然后合并它们内容的Python脚本示例。

# 首先定义pose.txt和time.txt的路径
name='corridor1'
pose_file_path = name+'_pose.txt'
time_file_path = name+'_time.txt'
result_file_path = name+'.txt'

# 读取pose.txt文件
with open(pose_file_path, 'r') as pose_file:
    pose_lines = pose_file.readlines()

# 读取time.txt文件
with open(time_file_path, 'r') as time_file:
    time_lines = time_file.readlines()

# 合并时间到pose行，并准备写入新文件
result_lines = []
for pose_line, time_line in zip(pose_lines, time_lines):
    time = time_line.split(',')[1].strip()  # 提取时间数据
    result_line = f"{time} {pose_line.strip()}\n"  # 合并时间和pose数据
    result_lines.append(result_line)

# 写入结果到result.txt
with open(result_file_path, 'w') as result_file:
    result_file.writelines(result_lines)

result_file_path  # 输出结果文件的路径以供下载或检查
