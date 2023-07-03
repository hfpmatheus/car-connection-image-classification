import os
import logging
from pathlib import Path

list_of_files = [
    ".github/workflows/.gitkeep",
    "app/__init__.py",
    "app/main.py",
    "app/templates/index.html",
    "artifacts/data/",
    "artifacts/model/",
    "src/__init__.py",
    "src/logger.py",
    "src/customized_exception.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/config/__init__.py",
    "src/pipelines/__init__.py",
    "src/entity/__init__.py",
    "src/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "notebooks/01_data-description.ipynb",
    "Dockerfile"
]

for file in list_of_files:
    if file.endswith("/"): # If the filename ends with slash, it's a directory path
        os.makedirs(file, exist_ok=True)

    else:
        filepath = Path(file)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)

        elif not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            with open(filepath, "w"):
                pass

# Creating logger and customized exception files
logger_path = Path("src/logger.py")
if not os.path.exists(logger_path):
    with open("src/logger.py", "w") as file:
        logger_content = """import logging
    import os
    from datetime import datetime

    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE)
    os.makedirs(logs_path, exist_ok=True)

    LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

    logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
        )
        """
        file.write(logger_content)

customized_exception_path = Path("src/customized_exception.py",)
if not os.path.exists(customized_exception_path):
    with open("src/customized_exception.py", "w") as file:
        customized_exception_content = """import sys
    from src.logger import logging

    def error_message_detail(error, error_detail:sys) -> str:
        _,_,exc_tb=error_detail.exc_info()
        filename=exc_tb.tb_frame.f_code.co_filename 

        error_message="Error occured in the python file named [{0}], on line number [{1}], error message: [{2}]".format(filename, exc_tb.tb_lineno, str(error))

        return error_message

    class CustomException(Exception):
        def __init__(self, error_message, error_detail:sys):
            super().__init__(error_message)
            self.error_message=error_message_detail(error_message, error_detail=error_detail)
            
        def __str__(self):
            return self.error_message
        """
        file.write(customized_exception_content)

