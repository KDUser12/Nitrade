import requests


class Update:

    @staticmethod
    def get_latest_version(current_version):
        url = f'https://api.github.com/repos/KDUser12/Nitrade/releases/latest'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            latest_version = data['tag_name']
            Update.check_for_update(current_version, latest_version)
        else:
            return None

    @staticmethod
    def check_for_update(current_version, latest_version):
        if current_version == latest_version:
            return "You are using the latest version of Nitrade"
        else:
            return "Click here to install the latest version of Nitrade: https://github.com/KDUser12/Nitrade/releases"
