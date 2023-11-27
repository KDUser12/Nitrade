import requests
from application.packages.error_handling import ErrorHandling


class Update:
    """ Class for managing application updates. """

    @staticmethod
    def get_latest_version(current_version):
        """
        Get the latest version from the GitHub API.
        :param current_version: Current version of the application.
        :return: Result of the update check.
        """
        url = 'https://api.github.com/repos/KDUser12/Nitrade/releases/latest'

        try:
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()
            latest_version = data['tag_name']

            result = Update.check_for_update(current_version, latest_version)
            return result
        except requests.exceptions.RequestException as error:
            ErrorHandling.output("201", error)
            return f"An error occurred while using the GitHub API: {error}"

    @staticmethod
    def check_for_update(current_version, latest_version):
        """
        Check if there is an update available.
        :param current_version: Current version of the app.
        :param latest_version: Latest version available.
        :return: Message indicating if there is an update.
        """
        if current_version == latest_version:
            return "You are using the latest version of Nitrade"
        else:
            return ("Update available now! Click here to install the latest version of Nitrade: "
                    "https://github.com/KDUser12/Nitrade/releases")
