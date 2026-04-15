import anthropic
import os
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    return text


def chunk_text(text, chunk_size=500):

    words = text.split()
    chunks=[]
    current_chunk = [] 
    current_size = 0


    for word in words:
        current_chunk.append(word)
        current_size += 1

        if current_size >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk=[]
            current_size=0

        if current_chunk:
            chunks.append(" ".join(current_chunk))
        return chunks
    

def find_relevant_chunks(question, chunks, max_chunks=3):
    question_words = set(question.lower().split())
    scored_chunks = []
    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(question_words.intersection(chunk_words))
        scored_chunks.append((score,chunk))

    scored_chunks.sort(reverse=True)
    return [chunk for _, chunk in scored_chunks[ :max_chunks]] 

def answer_question(question, context):
    prompt = f"""Use the following document content to answer the question.
    Only use information from the document. If the answer isn't in the document, say "I couldn't find that information in the document."

Document content:
{context}

Question: {question}"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages = [{"role": "user", "content": prompt}]
    
    )
    return response.content[0].text


print(" AI Document Q&A")

print ("-" * 40)


pdf_path = input("Enter the path to your PDF file: ")

print("\n Reading document...")

text= read_pdf(pdf_path)
chunks = chunk_text(text)


print(f"Document loaded! ({len(chunks)} chunks created)\n")

while True:
    question = input("Ask a question (or quit to exit): ")
    if question.lower() == "quit":
        break
    relevant_chunks = find_relevant_chunks(question, chunks)
    context = "\n\n".join(relevant_chunks)
    answer = answer_question(question, context)

    print(f"\n Answer: {answer}\n")
    print("-"*40)