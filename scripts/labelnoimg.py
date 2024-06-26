#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gradio as gr


def check_and_delete_labels(folder_path):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)
    # 获取所有.xml文件
    xml_files = [file for file in files if file.endswith('.xml')]
    # 获取所有.jpg, .jpeg和.png文件
    image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png'))]

    # 删除文件计数
    num = 0
    # 遍历所有.xml文件
    for xml_file in xml_files:
        # 检查是否存在相应的.jpg, .jpeg或.png文件
        # 根据.xml文件的扩展名来确定.jpg, .jpeg或.png文件的名称
        for image_ext in ('.jpg', '.jpeg', '.png'):
            image_file = xml_file.replace('.xml', image_ext)
            if image_file in image_files:
                break
        else:
            # 如果不存在任何对应的图像文件，则删除.xml文件
            num += 1
            os.remove(os.path.join(folder_path, xml_file))

    return f"处理完成，删除多余标签{num}个"


def interface(folder_path):
    check_and_delete_labels(folder_path)
    return "标签处理完成"


if __name__ == '__main__':
    iface = gr.Interface(fn=interface, inputs="text", outputs="text")
    iface.launch()
