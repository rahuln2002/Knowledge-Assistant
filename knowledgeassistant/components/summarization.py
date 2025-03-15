from knowledgeassistant.exception.exception import KnowledgeAssistantException
from knowledgeassistant.logging.logger import logging

from knowledgeassistant.entity.config_entity import DataSummarizationConfig
# from knowledgeassistant.entity.artifact_entity import DataSummarizationArtifact

from knowledgeassistant.utils.main_utils.utils import write_txt_file, read_txt_file

import sys
from transformers import pipeline

class DataSummarization:
    def __init__(self, data_summarization_config: DataSummarizationConfig):
        try:
            self.data_summarization_config = data_summarization_config
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)

    def summarize(self, input_text_path: str, min_length: int):
        try:
            pipe = pipeline("summarization", model="facebook/bart-large-cnn")
            logging.info("Summarization Pipeline Successfully Setup")
            summary = pipe(read_txt_file(input_text_path), min_length = min_length, do_sample = False)
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
            logging.info("Text successfully summarized")
            # data_summarization_artifact = DataSummarizationArtifact(
            #     text_file_path = self.data_summarization_config.input_text_file_path,
            #     summarized_text_file_path= self.data_summarization_config.summarized_text_file_path
            # )
            # return data_summarization_artifact
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)