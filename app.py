from flask import Flask, render_template, request
from knowledgeassistant.components.summarization import DataSummarization
from knowledgeassistant.components.keywordextraction import KeywordExtraction
from knowledgeassistant.entity.config_entity import DataSummarizationConfig, PipelineConfig, DataInputConfig, KeywordExtractionConfig
from knowledgeassistant.utils.main_utils.utils import write_txt_file, read_txt_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/assistant', methods=['POST'])
def assistant():
    pipeline_config = PipelineConfig()
    data_input_config = DataInputConfig(pipeline_config)

    user_text = request.form['user_text']
    user_number = int(request.form['user_number'])
    user_option = request.form['tasks']

    input_text_path = data_input_config.input_text_file_path

    write_txt_file(
        input_text_path,
        user_text,
        replace = True
    )

    if user_option == "summarization":
        data_summarization_config = DataSummarizationConfig(pipeline_config)
        summarizer = DataSummarization(data_summarization_config)
        file_path = data_summarization_config.summarized_text_file_path
        summarizer.initiate_data_summarization(
            input_text_path = input_text_path,
            min_length = user_number
        )
    elif user_option == "keywords":
        keyword_extraction_config = KeywordExtractionConfig(pipeline_config)
        extractor = KeywordExtraction(keyword_extraction_config)
        file_path = keyword_extraction_config.extracted_keywords_file_path
        extractor.initiate_keyword_extraction(
            input_text_path = input_text_path,
            keywords_count = user_number
        )
    elif user_option == "Q&A":
        pass
    
    return render_template(
        "results.html",
        task = user_option,
        text = read_txt_file(
            file_path = file_path
        )
    )

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)