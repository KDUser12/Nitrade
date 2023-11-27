import json
from application.packages.update import Update

JSONFILE = "data/config.json"


def json_file():
    with open(JSONFILE, "r") as file:
        content = json.load(file)
    return content


class console:
    def __init__(self):
        self.json_content = json_file()
        print(f'\033]2;Nitrade - {self.json_content["version"]}\007')

        test = Update.get_latest_version(self.json_content['version'])

        print(f"┏━(Welcome to Nitrade {self.json_content['version']})")
        print("┃\n┃ You are currently on a Beta version of the program")
        print("┃ if you encounter a problem open an issues on github :")
        print("┃ >> https://github.com/KDUser12/Nitrade/issues/new")
        print(f"┗━({test}")

    def prompt_handle(self):
        while True:
            self.prompt = input("[>] Choose an option: ")
