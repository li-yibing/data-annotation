import os
import logging

# 设置日志级别和格式
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def rename_files(folder_path, prefix):
    # 获取文件夹中的所有文件
    try:
        files = os.listdir(folder_path)
    except Exception as e:
        logging.error(f"Error reading directory: {e}")
        return "Error reading directory"

    # 获取所有.jpg, .jpeg, .png和.xml文件
    image_files = sorted([file for file in files if file.endswith(('.jpg', '.jpeg', '.png'))])
    xml_files = sorted([file for file in files if file.endswith('.xml')])

    if len(image_files) != len(xml_files):
        logging.error("The number of image files does not match the number of .xml files.")
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
            logging.info(f"Renamed {image_file} to {new_name + ext}")
        except Exception as e:
            logging.error(f"Error renaming file {image_file}: {e}")
            return f"Error renaming file {image_file}"

        # 重命名.xml文件
        try:
            new_xml_path = os.path.join(folder_path, new_name + '.xml')
            os.rename(os.path.join(folder_path, xml_file), new_xml_path)
            logging.info(f"Renamed {xml_file} to {new_name + '.xml'}")
        except Exception as e:
            logging.error(f"Error renaming file {xml_file}: {e}")
            return f"Error renaming file {xml_file}"

    return f"重命名完成,共{len(image_files)}条数据"


if __name__ == "__main__":
    folder_path = r"/Users/ybli/Desktop/TanKe"
    prefix = "TanKe"
    result = rename_files(folder_path, prefix)
    print(result)
