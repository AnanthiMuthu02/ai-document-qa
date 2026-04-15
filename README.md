# 📄 AI Document Q&A — RAG Application

An AI-powered tool that lets you upload any PDF document and ask questions about it in plain English — built using **RAG (Retrieval-Augmented Generation)** and the **Claude API by Anthropic**.

---

## 💡 What It Does

Instead of reading through long documents yourself, simply upload a PDF and ask questions. The AI finds the most relevant sections and answers your question using only the content from your document.

**Example use cases:**
- Ask questions about your own CV
- Query a research paper or report
- Extract key information from any PDF

---

## 🧠 What is RAG?

RAG (Retrieval-Augmented Generation) is one of the most in-demand AI concepts in software engineering today. Instead of relying on the AI's general knowledge, RAG grounds answers in YOUR specific document.

```
📄 PDF → ✂️ Split into chunks → 🔍 Find relevant chunks → 🤖 Claude answers
```

**3 simple steps:**
1. **Split** — Document is broken into 500-word chunks
2. **Search** — Most relevant chunks are found for your question
3. **Answer** — Claude reads only those chunks and answers accurately

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Claude API** (Anthropic) — `claude-sonnet-4-6`
- **pypdf** — PDF text extraction
- **python-dotenv** — secure API key management

---

## 🚀 How to Run It

### 1. Clone the repo
```bash
git clone https://github.com/AnanthiMuthu02/ai-document-qa.git
cd ai-document-qa
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install anthropic python-dotenv pypdf
```

### 4. Set up your API key
Create a `.env` file in the root folder:
```
ANTHROPIC_API_KEY=your-api-key-here
```
Get your key at [platform.claude.com](https://platform.claude.com)

### 5. Run the app
```bash
python app.py
```

---

## 💬 Example Output

```
📄 AI Document Q&A
----------------------------------------
Enter the path to your PDF file: /Users/ananthimuthu/cv.pdf

⏳ Reading document...
✅ Document loaded! (4 chunks created)

Ask a question (or 'quit' to exit): What are my technical skills?

💡 Answer: Based on the document, your technical skills include
PHP, Laravel, CakePHP, Python, Node.js, ReactJS, JavaScript,
HTML5, CSS3, REST APIs, SQL Server, MySQL, Git, and CI/CD pipelines.

----------------------------------------
Ask a question (or 'quit' to exit): What projects have I worked on?

💡 Answer: According to the document, you have worked on a
Financial Analytics Tool, an ML Data Processing Platform,
an HR Management System, and a Disease Prediction Web App
for your MSc thesis.

----------------------------------------
Ask a question (or 'quit' to exit): quit
```

---

## 🔑 Key Concepts Learned

| Concept | Description |
|--------|-------------|
| RAG | Retrieval-Augmented Generation — grounding AI answers in documents |
| Chunking | Splitting large text into manageable pieces |
| Semantic Search | Finding relevant content based on meaning |
| Prompt Engineering | Instructing Claude to answer only from the document |
| PDF Processing | Extracting and handling text from PDF files |

---

## 🔒 Security Note

Never commit your `.env` file. This repo includes a `.gitignore` that automatically excludes it.

---

## 👩‍💻 Author

**Ananthi Muthu**
Backend & Full Stack Software Engineer | Dublin, Ireland
[LinkedIn](https://www.linkedin.com/in/ananthi-muthu-76b3101a8/) | [GitHub](https://github.com/AnanthiMuthu02)

---


