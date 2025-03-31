import os
from datetime import datetime
from knowledgeassistant.constant import pipeline

class PipelineConfig:
    def __init__(self, timestamp = datetime.now()):
        timestamp = timestamp.strftime("%d_%m_%Y_%H_%M_%S")
        self.pipeline_name = pipeline.PIPELINE_NAME
        self.artifact_name = pipeline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(
            self.artifact_name,
            timestamp
        )
        self.timestamp: str = timestamp

class DataInputConfig:
    def __init__(self, pipeline_config: PipelineConfig):
        self.input_text_file_path: str = os.path.join(
            pipeline_config.artifact_dir,
            pipeline.INPUT_TEXT_DIR,
            pipeline.INPUT_TEXT_FILE_NAME
        )

class DataSummarizationConfig:
    def __init__(self, pipeline_config: PipelineConfig):
        self.data_summarization_dir: str = os.path.join(
            pipeline_config.artifact_dir,
            pipeline.DATA_SUMMARIZATION_DIR_NAME
        )
        self.summarized_text_file_path: str = os.path.join(
            self.data_summarization_dir,
            pipeline.SUMMARIZED_TEXT_DIR,
            pipeline.SUMMARIZED_TEXT_FILE_NAME
        )

class KeywordExtractionConfig:
    def __init__(self, pipeline_config: PipelineConfig):
        self.keyword_extraction_dir: str = os.path.join(
            pipeline_config.artifact_dir,
            pipeline.KEYWORD_EXTRACTION_DIR_NAME
        )
        self.extracted_keywords_file_path: str = os.path.join(
            self.keyword_extraction_dir,
            pipeline.EXTRACTED_KEYWORDS_DIR,
            pipeline.EXTRACTED_KEYWORDS_FILE_NAME
        )

class RAGConfig:
    def __init__(self, pipeline_config: PipelineConfig):
        self.RAG_dir: str = os.path.join(
            pipeline_config.artifact_dir,
            pipeline.RAG_DIR_NAME
        )
        self.rag_generated_text_path: str = os.path.join(
            self.RAG_dir,
            pipeline.RAG_DIR,
            pipeline.RAG_FILE_NAME
        )