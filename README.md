# **AI-Powered Knowledge Assistant (MVP) 🚀**  

This project is an AI-powered **Knowledge Assistant** that extracts keywords, generates summaries, and retrieves relevant information using **Retrieval-Augmented Generation (RAG)**. It integrates **transformers, FAISS, and embedding models** to enhance document understanding and response generation.  

🔗 **Live Deployment:** [Hugging Face Space](https://huggingface.co/spaces/rahuln2002/knowledge-assistant)  

---

## **📌 Features**
✅ **Summarization** – Extracts key insights from large text inputs  
✅ **Keyword Extraction** – Identifies important terms from input text  
✅ **Retrieval-Augmented Generation (RAG)** – Enhances response generation using retrieved knowledge  
✅ **Embeddings & FAISS** – Uses vector search for fast document retrieval  
✅ **Flask API Backend** – Handles requests efficiently  
✅ **Dockerized Deployment** – Fully containerized for seamless execution  

---

## **🛠️ Tech Stack**
- **Backend:** Python, Flask API  
- **Summarization Model:** `facebook/bart-large-cnn`  
- **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`  
- **RAG Generation Model:** `meta-llama/Llama-3-8b-chat-hf`  
- **Database:** FAISS-based vector storage  
- **Containerization:** Docker  
- **Deployment:** Hugging Face Spaces  

---

## **📌 API Endpoints**
| **Endpoint**  | **Method** | **Description** |
|--------------|-----------|----------------|
| `/` | GET, POST | Renders the web interface and processes input text for summarization, keyword extraction, or Q&A (RAG) |
| `/summarization` | POST | Summarizes input text based on a specified minimum length |
| `/extract_keywords` | POST | Extracts a specified number of keywords from the input text |
| `/rag` | POST | Processes a user query using the RAG pipeline for retrieval-augmented generation |

---

## **📊 RAG Pipeline**
- **Embeddings Model:** `sentence-transformers/all-MiniLM-L6-v2`  
- **FAISS Vector Storage:** Stores document embeddings for efficient retrieval  
- **LLM for Generation:** `meta-llama/Llama-3-8b-chat-hf` generates responses based on retrieved documents  

---

## **📝 Summarization Module**
- Uses **`facebook/bart-large-cnn`**  
- Automatically **truncates text beyond 1024 tokens**  
- Displays a warning if truncation happens  
- Saves output to a file  

---

## **🐳 Dockerfile Overview**
- Uses **Python 3.12.9-slim-bookworm** as the base image  
- Installs dependencies and required system packages  
- Downloads and stores the **summarization and embedding models** locally  
- Exposes port **7860** and runs the Flask API  

---

## **📌 Installation & Setup**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/knowledge-assistant.git
cd knowledge-assistant
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Application**
```sh
python app.py
```

---

## **🚀 Running with Docker**
### **Build the Docker Image**
```sh
docker build -t knowledge-assistant .
```

### **Run the Container**
```sh
docker run -p 7860:7860 knowledge-assistant
```

---

## **🛠️ Future Enhancements**
- ✅**Fine-tuning of Custom Models:** Replace current **pretrained models** with **custom fine-tuned** models for better accuracy and domain adaptability.  
- ✅**More NLP Features:** Extend capabilities beyond summarization, keyword extraction, and RAG to include **named entity recognition (NER), sentiment analysis, text classification, paraphrasing, and text generation**.  
- ✅**Enhanced RAG Pipeline:** Implement **multi-step retrieval, query expansion, and better chunking strategies** to improve response relevance.  
- ✅**Multilingual Support:** Extend support for multiple languages in summarization and keyword extraction.  
- ✅**Improved UI/UX:** Develop a more user-friendly frontend with interactive visualization for extracted keywords and RAG results.  
- ✅**Scalability Enhancements:** Optimize model loading, caching, and API performance for handling large-scale inputs and concurrent requests.  
- ✅**Integration with External Data Sources:** Enhance RAG by integrating APIs such as Wikipedia, Arxiv, and other knowledge repositories.  
- ✅**Model Optimization for Faster Inference:** Explore quantization, distillation, and other model compression techniques to improve latency and efficiency.  
- ✅**User Authentication & History Tracking:** Enable **user authentication** to allow users to track their history of queries and retrieved information.  

---

## **👨‍💻 Contributors**
- **Rahul Nihalani**  

---

## **📜 License**
This project is licensed under **MIT License**.