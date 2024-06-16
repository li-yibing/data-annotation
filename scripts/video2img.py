#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
视频转图像，支持设置间隔帧数与文件命名前缀
"""

import os
import cv2
import gradio as gr


def extract_frames(video_path, output_folder, frame_skip, prefix):
    """"""
    # 创建输出文件夹，如果不存在的话
    os.makedirs(output_folder, exist_ok=True)

    # 打开视频文件
    video_capture = cv2.VideoCapture(video_path)
    success, image = video_capture.read()
    index = 0
    count = 0

    # 提取帧并保存为图像文件
    while success:
        if count % frame_skip == 0:  # 跳过间隔帧数
            frame_name = f"{prefix}_{str(index).zfill(8)}.jpg"
            frame_path = os.path.join(output_folder, frame_name)
            cv2.imwrite(frame_path, image)
            index += 1
        success, image = video_capture.read()
        count += 1

    video_capture.release()

    # 创建压缩包
    zip_path = os.path.join(output_folder)
    return zip_path


# Gradio界面函数
def video_to_frames(video_file, output_folder, frame_skip, prefix):
    # 从视频文件路径中获取文件名（不包含扩展名）
    video_name = os.path.splitext(os.path.basename(video_file))[0]
    # 构建输出文件夹路径
    output_folder = os.path.join(os.path.dirname(output_folder), video_name)
    # 提取帧并返回路径
    file_path = extract_frames(video_file, output_folder, frame_skip, prefix)

    # 返回压缩包的下载链接
    return f"文件{video_name}转换完成。", file_path


with gr.Blocks(title="视频转换为图像") as demo:
    gr.Markdown("📌 本工具将视频转换为图像")
    with gr.Row():
        with gr.Column():
            block_video_file = gr.Text(label="选择视频文件")
            block_output_folder = gr.Textbox(label="选择保存路径", value="/Users/ybli/Pictures/images/")
            block_frame_skip = gr.Number(label="间隔帧数", value=10, step=1)
            block_prefix = gr.Textbox(label="命名前缀", value="frame", info="图像文件的命名前缀")
        with gr.Column():
            block_outputs = gr.Textbox(label="输出信息")
            zip_file = gr.TextArea(label="输出目录")
            generate_button = gr.Button(value="处理", variant="primary")

    generate_button.click(
        fn=video_to_frames,
        inputs=[block_video_file, block_output_folder, block_frame_skip, block_prefix],
        outputs=[block_outputs, zip_file],
        api_name="generate"
    )
    gr.Markdown("## 样例")
    gr.Examples(
        [
            [
                "/Users/ybli/Pictures/images/",
                "/Users/ybli/Desktop/"
            ],
        ],
        [block_output_folder],
    )


if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", share=True)
