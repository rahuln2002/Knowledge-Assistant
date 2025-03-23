from knowledgeassistant.exception.exception import KnowledgeAssistantException
from knowledgeassistant.logging.logger import logging

from knowledgeassistant.entity.config_entity import KeywordExtractionConfig
from knowledgeassistant.utils.main_utils.utils import read_txt_file, write_txt_file

import sys
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

class KeywordExtraction:
    def __init__(self, keyword_extraction_config: KeywordExtractionConfig):
        try:
            self.keyword_extraction_config = keyword_extraction_config
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)
    
    def extract_keywords(self, input_text_path: str, keywords_count: str):
        try:
            vectorizer = CountVectorizer(stop_words='english', token_pattern=r'(?u)\b[a-zA-Z]+\b')
            transformer = TfidfTransformer()
            logging.info("Vectorizer and Transformer successfully setup")

            text = read_txt_file(file_path=input_text_path)
            word_count_matrix = vectorizer.fit_transform([text])
            tfidf_matrix = transformer.fit_transform(word_count_matrix)
            logging.info("Successfully calculated word count and their tfidf scores")

            feature_array = np.array([word for word in vectorizer.get_feature_names_out() if word.isalpha()])
            tfidf_sorting = np.argsort(tfidf_matrix.toarray()).flatten()[::-1]
            logging.info("Successfully extracted keywords and sorted in descending order of their tfidf scores")

            top_keywords = feature_array[tfidf_sorting][:keywords_count]
            content = "\n".join(top_keywords)
            write_txt_file(
                self.keyword_extraction_config.extracted_keywords_file_path,
                content,
                True
            )
            logging.info(f"Successfully extracted and wrote top {keywords_count} keywords from text")
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)
    
    def initiate_keyword_extraction(self, input_text_path: str, keywords_count: str):
        try:
            self.extract_keywords(
                input_text_path = input_text_path,
                keywords_count = keywords_count
            )
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)