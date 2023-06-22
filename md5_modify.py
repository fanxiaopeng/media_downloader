import os


def change_file_md5(file_path):
    with open(file_path, 'a') as f:
        f.write('#1198')

def findfiles(path):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 循环判断每个元素是否是文件夹还是文件，是文件夹的话，递归
    for index, file in enumerate(file_list):
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        srcFile = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(srcFile):
            findfiles(srcFile)
        else:
            change_file_md5(srcFile)
            new_name = str(index) + '_' + file
            dstFile = os.path.join(path, new_name)
            os.rename(srcFile, dstFile)


if __name__ == "__main__":
    findfiles('/home/ubuntu/media_downloader/ok')
