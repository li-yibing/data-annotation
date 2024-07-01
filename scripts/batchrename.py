import os
import xml.etree.ElementTree as ET
from loguru import logger
import random


def rename_files(folder_path, prefix, shuffle=False):
    # 获取文件夹中的所有文件
    try:
        files = os.listdir(folder_path)
    except Exception as e:
        logger.error(f"读取文件夹错误: {e}")
        return "读取文件夹错误"
    if shuffle:
        logger.debug("打乱数据顺序")
        # 使用列表推导式筛选出所有图像文件和XML文件
        image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png'))]
        xml_files = [file for file in files if file.endswith('.xml')]
        # 随机打乱图像文件列表
        random.shuffle(image_files)
        # 根据图像文件的新顺序，创建一个新的XML文件列表
        xml_files = [xml_files[image_files.index(image)] for image in image_files]
    else:
        # 获取所有.jpg, .jpeg, .png和.xml文件
        image_files = sorted([file for file in files if file.endswith(('.jpg', '.jpeg', '.png'))])
        xml_files = sorted([file for file in files if file.endswith('.xml')])

    if len(image_files) != len(xml_files):
        logger.error("The number of image files does not match the number of .xml files.")
        return "Error: The number of image files does not match the number of .xml files."

    # 遍历所有.jpg和.xml文件，从1开始计数
    for i, (image_file, xml_file) in enumerate(zip(image_files, xml_files), start=1):

        # 构建新的文件名，不包括扩展名
        new_name = f"{prefix}_{str(i).zfill(8)}"

        # 重命名图像文件
        _, ext = os.path.splitext(image_file)
        try:
            new_image_path = os.path.join(folder_path, new_name + ext)
            os.rename(os.path.join(folder_path, image_file), new_image_path)
            logger.info(f"Renamed {image_file} to {new_name + ext}")
        except Exception as e:
            logger.error(f"Error renaming file {image_file}: {e}")
            return f"Error renaming file {image_file}"

        # 重命名.xml文件
        try:
            tree = ET.parse(os.path.join(folder_path, xml_file))
            root = tree.getroot()

            # 修改<filename>和<path>标签的值
            for filename in root.iter('filename'):
                filename.text = new_name + ext
            for path in root.iter('path'):
                path.text = new_name + ext

            # 保存修改后的.xml文件
            tree.write(os.path.join(folder_path, new_name + '.xml'))

            os.remove(os.path.join(folder_path, xml_file))
            logger.info(f"Renamed {xml_file} to {new_name + '.xml'}")
        except Exception as e:
            logger.error(f"Error renaming file {xml_file}: {e}")
            return f"Error renaming file {xml_file}"

    return f"重命名完成,共{len(image_files)}条数据"


if __name__ == "__main__":
    folder_path = r"/Users/ybli/Desktop/TanKe"
    prefix = "TanKe"
    result = rename_files(folder_path, prefix)
    print(result)
