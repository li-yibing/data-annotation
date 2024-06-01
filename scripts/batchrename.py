#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gradio as gr

def rename_files(folder_path, prefix):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)
    # 获取所有.jpg和.xml文件
    target_files = [file for file in files if file.endswith('.jpg') or file.endswith('.xml')]

    # 对文件进行排序，确保.jpg和.xml文件的顺序一致
    target_files.sort()

    # 遍历所有目标文件
    for i, file in enumerate(target_files):
        # 构建新的文件名
        new_name = f"{prefix}_{str(i+1).zfill(8)}{os.path.splitext(file)[1]}"
        # 重命名文件
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

    return "重命名完成"

def interface(folder_path, prefix):
    rename_files(folder_path, prefix)
    return "文件重命名完成"

iface = gr.Interface(fn=interface, inputs=["text", "text"], outputs="text")
iface.launch()