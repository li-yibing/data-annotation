from scripts.batchrename import rename_files

if __name__ == '__main__':
    folder_path = r"/Users/ybli/Desktop/MinYongChengYongChe"
    prefix = "MinYongChengYongChe"
    result = rename_files(folder_path, prefix)
    print(result)
