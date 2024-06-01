#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gradio as gr

def check_and_delete_labels(folder_path):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)
    # 获取所有.xml文件
    xml_files = [file for file in files if file.endswith('.xml')]
    # 获取所有.jpg文件
    jpg_files = [file for file in files if file.endswith('.jpg')]

    # 遍历所有.xml文件
    for xml_file in xml_files:
        # 检查是否存在相应的.jpg文件
        jpg_file = xml_file.replace('.xml', '.jpg')
        if jpg_file not in jpg_files:
            # 如果不存在，删除.xml文件
            os.remove(os.path.join(folder_path, xml_file))

    return "处理完成"

def interface(folder_path):
    check_and_delete_labels(folder_path)
    return "标签处理完成"

iface = gr.Interface(fn=interface, inputs="text", outputs="text")
iface.launch()