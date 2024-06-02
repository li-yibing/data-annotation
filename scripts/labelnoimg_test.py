import os
import logging

# 设置日志级别和格式
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def check_and_delete_labels(folder_path):
    # 获取文件夹中的所有文件
    try:
        files = os.listdir(folder_path)
    except Exception as e:
        logging.error(f"Error reading directory: {e}")
        return "Error reading directory"

    # 获取所有.xml文件
    xml_files = [file for file in files if file.endswith('.xml')]
    # 获取所有.jpg文件
    jpg_files = [file for file in files if file.endswith('.jpg')]

    # 遍历所有.xml文件
    for xml_file in xml_files:
        # 检查是否存在相应的.jpg文件
        jpg_file = xml_file.replace('.xml', '.jpg')
        if jpg_file not in jpg_files:
            # 如果不存在，删除.xml文件
            try:
                os.remove(os.path.join(folder_path, xml_file))
                logging.info(f"Deleted {xml_file}")
            except Exception as e:
                logging.error(f"Error deleting file {xml_file}: {e}")
                return f"Error deleting file {xml_file}"

    return "处理完成"

folder_path = r"D:\数据集\项目\同步的数据集\火炮车\HuoPaoChe.v4i.voc\train"
result = check_and_delete_labels(folder_path)
print(result)