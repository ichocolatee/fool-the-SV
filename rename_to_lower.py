import os
def rename_to_lowercase(directory):
    # 获取当前目录下的所有文件和文件夹
    contents = os.listdir(directory)
    
    # 遍历当前目录下的所有内容
    for item in contents:
        item_path = os.path.join(directory, item)
        
        # 如果是文件夹，则递归调用rename_to_lowercase函数
        if os.path.isdir(item_path):
            rename_to_lowercase(item_path)
        
    # 遍历当前目录下的所有内容并进行重命名
    for item in contents:
        item_path = os.path.join(directory, item)
        
        # 将文件或文件夹名称改为小写字母
        new_item = item.lower()
        new_item_path = os.path.join(directory, new_item)
        
        # 如果名称有变化，则重命名
        if item != new_item:
            os.rename(item_path, new_item_path)
            print(f'Renamed: {item_path} -> {new_item_path}')

# 指定要操作的文件夹路径
directory_path = '/root/data2/SRS/learning-to-fool-the-speaker-recognition-master/data/TIMIT/TIMIT_lower/train'

# 调用函数进行重命名
rename_to_lowercase(directory_path)
