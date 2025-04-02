from knowledgeassistant.exception.exception import KnowledgeAssistantException
from knowledgeassistant.logging.logger import logging

from knowledgeassistant.entity.config_entity import DataSummarizationConfig
from knowledgeassistant.utils.main_utils.utils import write_txt_file, read_txt_file

import sys
import torch
from transformers import pipeline

class DataSummarization:
    def __init__(self, data_summarization_config: DataSummarizationConfig):
        try:
            self.data_summarization_config = data_summarization_config
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)

    def summarize(self, input_text_path: str, min_length: int):
        try:
            device = "cuda" if torch.cuda.is_available() else "cpu"
            pipe = pipeline("summarization", model="facebook/bart-large-cnn", device=0 if device == "cuda" else -1)
            logging.info("Summarization Pipeline Successfully Setup")

            text = read_txt_file(input_text_path)
            summary = pipe(text, min_length = min_length, do_sample = False)
            logging.info("Text successfully summarized")
            
            write_txt_file(self.data_summarization_config.summarized_text_file_path, summary[0].get("summary_text"))
            logging.info("Successfully wrote summarized text")
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)
    
    def initiate_data_summarization(self, input_text_path: str, min_length: int):
        try:
            self.summarize(
                input_text_path = input_text_path,
                min_length = min_length
            )
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)