# **🧠 AI Research Assistant**  

## **📌 Project Overview**  
This project is an **AI-powered research assistant** that extracts key information from PDF documents and generates concise summaries using **T5 Transformer models**.  

It includes:  
✅ **FastAPI Backend** – Handles file uploads & runs the model  
✅ **Streamlit Frontend** – Provides an interactive UI for users  

---

## **🚀 Features**  
✔ Upload a **research paper** (PDF) and get a **structured summary**  
✔ Uses **T5 Transformer model** for summarization  
✔ **FastAPI for backend** and **Streamlit for UI**  

---

## **⚙ Installation & Setup**  

### **🔹 1. Clone the Repository**  
```bash
git clone https://github.com/yourusername/AI-Research-Assistant.git
cd AI-Research-Assistant
```

### **🔹 2. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **🔹 3. Start FastAPI Backend**  
```bash
uvicorn app:app --reload
```

### **🔹 4. Run Streamlit Frontend**  
```bash
streamlit run streamlit_app.py
```

Your **FastAPI backend** will be at **http://127.0.0.1:8000**  
Your **Streamlit UI** will be at **http://127.0.0.1:8501**  

---

## **🛠️ Code Explanation**  

### **📄 1. PDF Text Extraction **  
The project uses `pymupdf` (or `fitz`) to extract text from PDFs:  

### **🤖 2. AI Model for Summarization **  
The model used is `T5ForConditionalGeneration` from Hugging Face:  
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration  

# Load tokenizer and model  
tokenizer = T5Tokenizer.from_pretrained("t5-small")  
model = T5ForConditionalGeneration.from_pretrained("t5-small")  

def summarize_text(text):  
    inputs = tokenizer("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)  
    summary_ids = model.generate(inputs.input_ids, max_length=150, min_length=50, length_penalty=2.0, num_beams=4)  
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)  
```

---

### **🚀 3. FastAPI Backend (`app.py`)**  
The FastAPI server processes uploaded PDFs and returns summaries:  

### **💻 4. Streamlit Frontend (`streamlit_app.py`)**  
Streamlit provides an easy-to-use UI for uploading PDFs:  

## **🛠️ Planned Improvements**  
### **1️⃣ Third-Person Summaries**  
- Summaries are currently **in the first person (e.g., "I found that...")**  
- Modify model prompt to generate **neutral third-person summaries (e.g., "The document states that...")**  

### **2️⃣ Reduce Latency**  
- Improve efficiency by **loading the model once and caching results**  

### **3️⃣ Bullet-Point Summaries**
- The model generates a single-paragraph summary
- Instead, return key points in bullet format
