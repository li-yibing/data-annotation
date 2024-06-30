import os
import xml.etree.ElementTree as ET
from collections import defaultdict
from loguru import logger


# 程序功能：统计XML文件中不同类别的出现次数
def count_labels(input_path):
    label_count = defaultdict(int)
    listdir = os.listdir(input_path)

    for file in listdir:
        if file.endswith('xml'):
            file_path = os.path.join(input_path, file)
            tree = ET.parse(file_path)
            root = tree.getroot()
            for object1 in root.findall('object'):
                for sku in object1.findall('name'):
                    if sku.text == "HuoPaoChe":
                        print(file)
                    label_count[sku.text] += 1
        else:
            pass

    return label_count


if __name__ == '__main__':
    inputpath = R'C:\Users\ybli\Desktop\Datasets\ShiBing'  # 替换为你的XML文件夹路径
    label_count = count_labels(inputpath)

    # 打印每种类别及其出现的次数
    for label, count in label_count.items():
        logger.info(f'类别: {label} - 数量: {count}')
