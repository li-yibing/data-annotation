# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : cuhk2yolo.py
# Time       ：2024-07-01 21:56
# Author     ：ybli
# Description：将CUHKSYSU行人检测数据集标注样式转化为YOLO
# class id x_center y_center width height -> class x_center y_center width height
"""


import glob
import os
import re
from loguru import logger


def cuhk2yolo(src_dir, det_dir):
    # 确保目标目录存在，如果不存在则创建
    os.makedirs(det_dir, exist_ok=True)

    # 读取源目录下所有的标注文件
    label_files = glob.glob(os.path.join(src_dir, '*.txt'))
    success_count = 0
    for label_file in label_files:
        with open(label_file, "r") as f:
            yolo_format = ""
            for line in f:
                # 使用正则表达式分割字符串，\s+ 表示一个或多个空白字符
                words = re.split(r'\s+', line.strip())
                if len(words) < 6:  # 确保分割后的列表至少有6个元素
                    continue  # 如果不足6个元素，跳过这一行
                # 转换为YOLO格式
                yolo_format += f"{words[0]} {words[2]} {words[3]} {words[4]} {words[5]}\n"
            file_name = os.path.basename(label_file)
            yolo_file_path = os.path.join(det_dir, file_name)
            with open(yolo_file_path, 'w') as file_stream:
                file_stream.write(yolo_format)
                success_count += 1
    logger.debug(f"总共有{len(label_files)}条数据，成功{success_count}条。")
    return f"总共有{len(label_files)}条数据，成功{success_count}条。"


if __name__ == "__main__":
    src_dir = r"C:\Users\ybli\Desktop\labels"  # 使用原始字符串避免转义问题
    det_dir = r"C:\Users\ybli\Desktop\labels_yolo"
    cuhk2yolo(src_dir, det_dir)
