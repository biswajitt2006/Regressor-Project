import sys
from logger import logging  # Make sure this logger is correctly configured

def error_message_detail(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)  # ✅ Corrected
        self.error_message = error_message_detail(error_message, error_details=error_details)
        
    def __str__(self):
        return self.error_message


if __name__=="__main__" :
    logging.info("Logging has started")
    
    try :
        a=1/0
    except CustomException as e :
        logging.info("Error has occured")
        raise CustomException(e,sys)
        