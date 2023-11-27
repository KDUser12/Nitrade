import datetime
from application.packages.error_handling.manager import error_code


class ErrorHandling:
    LOGFILE = "logs.txt"

    @staticmethod
    def _find_element(code):
        """ Finding the element corresponding to the error code. """
        for element in error_code:
            if code in element:
                return element.get(code)
        return None

    @staticmethod
    def output(code, error_message):
        """
        Error Management in the console
        :param code: Error code
        :param error_message: Error message
        """
        format_output = "[{}] : ERROR {} - {}"
        current_time = datetime.datetime.now()

        message = ErrorHandling._find_element(code)
        ErrorHandling.file(code, error_message)

        if code != "201":
            formatted_error = format_output.format(current_time, code, message)
            print(formatted_error)

    @staticmethod
    def file(code, error_message):
        """
        Handling errors in a log file.
        :param code: Error code
        :param error_message: Error message
        :return:
        """
        with open(ErrorHandling.LOGFILE, "a") as logfile:
            logfile.write(f"[{datetime.datetime.now()}] : ERROR {code} - {error_message}\n")
