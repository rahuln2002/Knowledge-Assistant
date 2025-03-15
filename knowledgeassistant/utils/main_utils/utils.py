from knowledgeassistant.exception.exception import KnowledgeAssistantException
from knowledgeassistant.logging.logger import logging
import os
import sys

def write_txt_file(file_path: str, content: str, replace: bool = False):
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)
            logging.info(f"Successfully removed the file: {file_path}")
        dir_path = os.path.dirname(file_path)
        logging.info(f"Successfully create the file: {file_path}")
        os.makedirs(dir_path, exist_ok = True)
        with open(file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(content)
        logging.info("Successfully wrote content to text file")
    except Exception as e:
        raise KnowledgeAssistantException(e, sys)

def read_txt_file(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as txt_file:
            text = txt_file.read()
            logging.info("Successfully read the file")
            return text
    except Exception as e:
        raise KnowledgeAssistantException(e, sys)