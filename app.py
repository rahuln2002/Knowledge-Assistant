from flask import Flask, render_template, request
from knowledgeassistant.components.summarization import DataSummarization
from knowledgeassistant.entity.config_entity import DataSummarizationConfig, PipelineConfig
from knowledgeassistant.utils.main_utils.utils import write_txt_file, read_txt_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/assistant', methods=['POST'])
def assistant():
    pipeline_config = PipelineConfig()
    data_summarization_config = DataSummarizationConfig(pipeline_config)

    user_text = request.form['user_text']
    user_number = request.form['user_number']
    user_option = request.form['tasks']

    write_txt_file(
        data_summarization_config.input_text_file_path,
        user_text,
        replace = True
    )

    if user_option == "summarization":
        summarizer = DataSummarization(data_summarization_config=data_summarization_config)
        summarizer.initiate_data_summarization(
            input_text_path = data_summarization_config.input_text_file_path,
            min_length = int(user_number)
        )
    
    return render_template(
        "results.html",
        task = user_option,
        text = read_txt_file(
            file_path = data_summarization_config.summarized_text_file_path
        )
    )

if __name__ == '__main__':
    app.run(host='localhost', port=8080)