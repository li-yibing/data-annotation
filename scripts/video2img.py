#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import cv2
import gradio as gr


def extract_frames(video_path, output_folder, frame_skip, prefix, start_index):
    # 创建输出文件夹，如果不存在的话
    os.makedirs(output_folder, exist_ok=True)

    # 打开视频文件
    video_capture = cv2.VideoCapture(video_path)
    success, image = video_capture.read()
    count = 0

    # 提取帧并保存为图像文件
    while success:
        if count % frame_skip == 0:  # 跳过间隔帧数
            index = start_index + count
            frame_name = f"{prefix}_{str(index).zfill(6)}.jpg"
            frame_path = os.path.join(output_folder, frame_name)
            cv2.imwrite(frame_path, image)
        success, image = video_capture.read()
        count += 1

    video_capture.release()


# Gradio界面函数
def video_to_frames(video_file, frame_skip, prefix, start_index):
    # 从视频文件路径中获取文件名（不包含扩展名）
    video_name = os.path.splitext(os.path.basename(video_file.name))[0]
    # 构建输出文件夹路径
    output_folder = os.path.join(os.path.dirname(video_file.name), video_name)

    extract_frames(video_file, output_folder, frame_skip, prefix, start_index)
    return f"Frames extracted successfully with prefix '{prefix}', start index {start_index}, and frame skip {frame_skip}!"


with gr.Blocks(title="视频转换为图像") as demo:
    gr.Markdown("📌 本工具将视频转换为图像。")
    with gr.Row():
        with gr.Column():
            block_video_file = gr.File(label="选择视频文件")
            block_frame_skip = gr.Number(label="间隔帧数", value=1, step=1)
            block_prefix = gr.Textbox(label="命名前缀", value="frame", info="图像文件的命名前缀")
            block_start_index = gr.Number(label="起始编号", value=0, step=1)
        with gr.Column():
            block_outputs = gr.Textbox(label="输出信息")
            generate_button = gr.Button(value="处理", variant="primary")

    generate_button.click(
        fn=video_to_frames,
        inputs=[block_video_file, block_frame_skip, block_prefix, block_start_index],
        outputs=block_outputs,
        api_name="generate"
    )

demo.launch(server_name="0.0.0.0", share=True)