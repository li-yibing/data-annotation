#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gradio as gr

def check_and_delete_images(folder_path):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)
    # 获取所有.jpg文件
    jpg_files = [file for file in files if file.endswith('.jpg')]
    # 获取所有.xml文件
    xml_files = [file for file in files if file.endswith('.xml')]

    # 遍历所有.jpg文件
    for jpg_file in jpg_files:
        # 检查是否存在相应的.xml文件
        xml_file = jpg_file.replace('.jpg', '.xml')
        if xml_file not in xml_files:
            # 如果不存在，删除.jpg文件
            os.remove(os.path.join(folder_path, jpg_file))

    return "处理完成"

def interface(folder_path):
    check_and_delete_images(folder_path)
    return "图片处理完成"

iface = gr.Interface(fn=interface, inputs="text", outputs="text")
iface.launch()