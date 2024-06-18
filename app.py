#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gradio as gr

from scripts.video2img import video_to_frames
from scripts.imgnolabel import check_and_delete_images
from scripts.labelnoimg import check_and_delete_labels


with gr.Blocks(title="数据集处理") as demo:

    with gr.Tab(label="视频转图像"):
        gr.Markdown("## 视频转图像")
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

    with gr.Tab(label="删除多余图像"):
        gr.Markdown("## 删除多余图像")
        with gr.Row():
            filename = gr.Text(label="数据集文件夹")
            result = gr.Text(label="处理结果", show_label=True, visible=True)
        with gr.Row():
            predict_button = gr.Button(value="处理", variant='primary')
        predict_button.click(fn=check_and_delete_images, inputs=filename, outputs=result)


    with gr.Tab(label="删除多余标签"):
        gr.Markdown("## 删除多余标签")
        with gr.Row():
            filename = gr.Text(label="数据集文件夹")
            result = gr.Text(label="处理结果", show_label=True, visible=True)
        with gr.Row():
            predict_button = gr.Button(value="处理", variant='primary')
        predict_button.click(fn=check_and_delete_labels, inputs=filename, outputs=result)

demo.launch(server_name="127.0.0.1", share=True)
