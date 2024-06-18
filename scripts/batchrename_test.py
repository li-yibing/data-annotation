import os
import logging
import xml.etree.ElementTree as ET

# 设置日志级别和格式
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def rename_files(folder_path, prefix):
    # 获取文件夹中的所有文件
    try:
        files = os.listdir(folder_path)
    except Exception as e:
        logging.error(f"Error reading directory: {e}")
        return "Error reading directory"

    # 获取所有.jpg和.xml文件
    jpg_files = sorted([file for file in files if file.endswith('.jpg')])
    xml_files = sorted([file for file in files if file.endswith('.xml')])

    if len(jpg_files) != len(xml_files):
        logging.error("The number of .jpg files does not match the number of .xml files.")
        return "Error: The number of .jpg files does not match the number of .xml files."

    # 遍历所有.jpg和.xml文件
    for i in range(len(jpg_files)):
        jpg_file = jpg_files[i]
        xml_file = xml_files[i]

        # 构建新的文件名
        new_name = f"{prefix}_{str(i+1+2775).zfill(8)}"

        # 重命名.jpg文件
        try:
            os.rename(os.path.join(folder_path, jpg_file), os.path.join(folder_path, new_name + '.jpg'))
            logging.info(f"Renamed {jpg_file} to {new_name + '.jpg'}")
        except Exception as e:
            logging.error(f"Error renaming file {jpg_file}: {e}")
            return f"Error renaming file {jpg_file}"

        # 重命名.xml文件
        try:
            tree = ET.parse(os.path.join(folder_path, xml_file))
            root = tree.getroot()

            # 修改<filename>和<path>标签的值
            for filename in root.iter('filename'):
                filename.text = new_name + '.jpg'
            for path in root.iter('path'):
                path.text = new_name + '.jpg'

            # 保存修改后的.xml文件
            tree.write(os.path.join(folder_path, new_name + '.xml'))

            os.remove(os.path.join(folder_path, xml_file))
            logging.info(f"Renamed {xml_file} to {new_name + '.xml'}")
        except Exception as e:
            logging.error(f"Error renaming file {xml_file}: {e}")
            return f"Error renaming file {xml_file}"

    return "重命名完成"

folder_path = r"D:\labelimg_v1.8.1\labelimg_v1.8.1\ShiBing.v2i.voc\train"
prefix = "ShiBing"
result = rename_files(folder_path, prefix)
print(result)