#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gradio as gr


def check_and_delete_images(folder_path):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)
    # 获取所有.jpg, .jpeg和.png文件
    image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png'))]
    # 获取所有.xml文件
    xml_files = [file for file in files if file.endswith('.xml')]
    # 删除文件计数
    num = 0
    # 遍历所有图像文件
    for image_file in image_files:
        # 检查是否存在相应的.xml文件
        # 根据图像文件的扩展名来确定.xml文件的名称
        if image_file.lower().endswith(('.jpg', '.jpeg')):
            xml_file = image_file.replace('.jpg', '.xml').replace('.jpeg', '.xml')
        elif image_file.lower().endswith('.png'):
            xml_file = image_file.replace('.png', '.xml')
        else:
            continue

        if xml_file not in xml_files:
            num += 1
            # 如果不存在，删除图像文件
            os.remove(os.path.join(folder_path, image_file))

    return f"处理完成，删除多余图像{num}个"


def interface(folder_path):
    check_and_delete_images(folder_path)
    return "图片处理完成"


if __name__ == '__main__':
    iface = gr.Interface(fn=interface, inputs="text", outputs="text")
    iface.launch()
