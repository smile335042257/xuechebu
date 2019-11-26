import yaml


def build_login_data():
    with open('./data/login_data.yaml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        # print(data.values())
        data_list = []
        for i in data.values():
            data_list.append((i.get('name'),
                              i.get('pwd')))
        print(data_list)
        return data_list


# import os
#
# # 封装项目路径(动态获取绝对路径)
# file_path = os.path.abspath(__file__)  # 获取当前文件的路径
# pro_path = os.path.dirname(file_path)  # 获取项目路径
