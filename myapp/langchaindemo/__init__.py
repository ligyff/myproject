import os

os.environ["OPENAI_API_KEY"] = ''


def load_openai_api_key():
    print('加载load----------------------')
    os.environ["OPENAI_API_KEY"] = ''


print('--------------------------------------------------')