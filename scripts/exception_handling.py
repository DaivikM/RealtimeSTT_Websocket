import sys

class ProjectException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _, _, exec_tb = error_details.exc_info()

        self.lineno = exec_tb.tb_lineno
        self.filename = exec_tb.tb_frame.f_code.co_filename

    def __str__(self):
        error_msg =  f'\nError occured in file: {self.filename}, \nline: {self.lineno}, \nError Msg: {self.error_message}'

        # Exit the program with a status code of 1
        sys.exit(1)

        return error_msg