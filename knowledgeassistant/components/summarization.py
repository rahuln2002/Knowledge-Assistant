from knowledgeassistant.exception.exception import KnowledgeAssistantException
from knowledgeassistant.logging.logger import logging

from knowledgeassistant.entity.config_entity import DataSummarizationConfig
from knowledgeassistant.utils.main_utils.utils import write_txt_file, read_txt_file

import sys
from transformers import pipeline, AutoTokenizer

class DataSummarization:
    def __init__(self, data_summarization_config: DataSummarizationConfig):
        try:
            self.data_summarization_config = data_summarization_config
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)

    def summarize(self, input_text_path: str, min_length: int):
        try:
            model = "facebook/bart-large-cnn"
            
            tokenizer = AutoTokenizer.from_pretrained(model)

            pipe = pipeline("summarization", model=model, tokenizer=model)
            logging.info("Summarization Pipeline Successfully Setup")

            text = read_txt_file(input_text_path)

            tokens = tokenizer.encode(text, truncation=True, max_length=1024, return_tensors="pt")

            if len(tokens[0]) >= 1024:
                logging.warning("Input text exceeded 1024 tokens. It has been truncated.")
                truncated_text = tokenizer.decode(tokens[0], skip_special_tokens=True)
                frontend_message = "Your input text exceeded the limit of 1024 tokens and has been truncated."
            else:
                truncated_text = text
                frontend_message = ""

            summary = pipe(truncated_text, min_length=min_length, max_length=142, do_sample=False)
            logging.info("Text successfully summarized")

            write_txt_file(self.data_summarization_config.summarized_text_file_path, summary[0].get("summary_text"))
            logging.info("Successfully wrote summarized text")

            return {
                "summary": summary[0].get("summary_text"),
                "warning": frontend_message
            }

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