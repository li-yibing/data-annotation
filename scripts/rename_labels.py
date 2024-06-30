import os
import xml.etree.ElementTree as ET
from loguru import logger


# 程序功能：修改XML文件中的标签名称
def rename_labels(input_path, src_name, det_name):
    rename_num = 0
    listdir = os.listdir(input_path)

    for file in listdir:
        if file.endswith('xml'):
            file_path = os.path.join(input_path, file)
            tree = ET.parse(file_path)
            root = tree.getroot()
            for item in root.findall('object'):
                for sku in item.findall('name'):
                    if sku.text == src_name:
                        sku.text = det_name
                        rename_num += 1
            tree.write(file_path, encoding='utf-8')


    return f"已完成{rename_num}次重命名标签，从{src_name}到{det_name}。"


if __name__ == '__main__':
    inputpath = R'C:\Users\ybli\Desktop\Datasets\ShiBing'  # 替换为你的XML文件夹路径
    label_count = rename_labels(inputpath)
