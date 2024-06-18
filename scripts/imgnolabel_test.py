import os

from loguru import logger


def check_and_delete_images(folder_path):
    # 获取文件夹中的所有文件
    try:
        files = os.listdir(folder_path)
    except Exception as e:
        logger.error(f"Error reading directory: {e}")
        return "Error reading directory"

    # 获取所有.jpg文件
    jpg_files = [file for file in files if file.endswith('.jpg')]
    # 获取所有.xml文件
    xml_files = [file for file in files if file.endswith('.xml')]

    # 遍历所有.jpg文件
    for jpg_file in jpg_files:
        # 检查是否存在相应的.xml文件
        xml_file = jpg_file.replace('.jpg', '.xml')
        if xml_file not in xml_files:
            # 如果不存在，删除.jpg文件
            try:
                os.remove(os.path.join(folder_path, jpg_file))
                logger.info(f"Deleted {jpg_file}")
            except Exception as e:
                logger.error(f"Error deleting file {jpg_file}: {e}")
                return f"Error deleting file {jpg_file}"

    return "处理完成"


folder_path = r"C:\Users\zhaotong\Desktop\img_test"
result = check_and_delete_images(folder_path)
print(result)
