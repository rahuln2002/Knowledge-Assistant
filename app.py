from flask import Flask, render_template, request
from knowledgeassistant.components.summarization import DataSummarization
from knowledgeassistant.components.keywordextraction import KeywordExtraction
from knowledgeassistant.components.RAG import RAG
from knowledgeassistant.entity.config_entity import DataSummarizationConfig, PipelineConfig, DataInputConfig, KeywordExtractionConfig, RAGConfig
from knowledgeassistant.utils.main_utils.utils import write_txt_file, read_txt_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pipeline_config = PipelineConfig()
        data_input_config = DataInputConfig(pipeline_config)

        user_text = request.form['user_text']
        user_option = request.form['tasks']
        result_text = ""

        if user_option == "Q&A":
            user_question = request.form['user_question']
        else:
            user_number = int(request.form['user_number'])

        input_text_path = data_input_config.input_text_file_path
        write_txt_file(input_text_path, user_text, replace=True)

        if user_option == "summarization":
            data_summarization_config = DataSummarizationConfig(pipeline_config)
            summarizer = DataSummarization(data_summarization_config)
            file_path = data_summarization_config.summarized_text_file_path
            summarizer.initiate_data_summarization(input_text_path=input_text_path, min_length=int(user_number))
        elif user_option == "keywords":
            keyword_extraction_config = KeywordExtractionConfig(pipeline_config)
            extractor = KeywordExtraction(keyword_extraction_config)
            file_path = keyword_extraction_config.extracted_keywords_file_path
            extractor.initiate_keyword_extraction(input_text_path=input_text_path, keywords_count=int(user_number))
        elif user_option == "Q&A":
            rag_config = RAGConfig(pipeline_config)
            rag = RAG(rag_config)
            file_path = rag_config.rag_generated_text_path
            rag.initiate_rag(input_text_path=input_text_path, query=user_question)

        result_text = read_txt_file(file_path=file_path)

        return render_template("index.html", task=user_option, text=result_text, user_text=user_text)

    return render_template("index.html", task=None, text=None, user_text=None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7860)