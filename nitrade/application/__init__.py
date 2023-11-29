import json
import sys
from colorama import Style, Fore, init
from application.packages.update import Update
from application.packages.error_handling import ErrorHandling
from application.modules.local import Local
from application.modules.network import Network

JSON_FILE = "data/config.json"
UNKNOWN_COMMAND_MESSAGE = "Unknown command"
KEYBOARD_INTERRUPT_MESSAGE = "KeyboardInterrupt"


class console:
    """ Class representing the console interface of the Nitrade application. """

    def __init__(self):
        init()

        self.prompt = None
        self.json_content = self.load_json_file()
        self.update = Update.get_latest_version(self.json_content['version'])

        print(f'\033]2;Nitrade - {self.json_content["version"]}\007')

        self.print_welcome_message()

        print("[1] Local    [2] Network")
        print("[3] About    [5] Exit\n")
        self.command_input()

    @staticmethod
    def load_json_file():
        """ Loads the contents of the JSON file. """
        with open(JSON_FILE, "r") as file:
            content = json.load(file)
        return content

    def print_welcome_message(self):
        """ Displays the welcome message """
        print("┏━(" + Fore.RED + f"Welcome to Nitrade {self.json_content['version']}" + Style.RESET_ALL + ")")
        print("┃\n┃ You are currently on a Beta version of the program")
        print(f'┃ if you encounter a problem open an issue on github :\n'
              f'┃ >> {Fore.LIGHTBLUE_EX}https://github.com/KDUser12/Nitrade/issues/new{Style.RESET_ALL}\n┃')
        print("┗━(" + Fore.LIGHTBLACK_EX + f"{self.update}" + Style.RESET_ALL + ")\n")

    def command_input(self):
        try:
            while True:
                self.prompt = input("[>] Choose an option: ")
                self.command_manager()
        except KeyboardInterrupt:
            ErrorHandling.output("101", KEYBOARD_INTERRUPT_MESSAGE)

    def command_manager(self):
        """ Manage orders entered by the user. """
        commands = {
            "1": Local,
            "2": Network,
            "3": None,
            "4": sys.exit
        }

        command_function = commands.get(self.prompt, self.unknown_command)
        command_function()

    @staticmethod
    def unknown_command():
        """ Handles unknown commands. """
        ErrorHandling.output("301", UNKNOWN_COMMAND_MESSAGE)
