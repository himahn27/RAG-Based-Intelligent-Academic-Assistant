from vector_db import load_vector_store
from web_search import search_web
from groq import Groq
from config import GROQ_API_KEY, SIMILARITY_THRESHOLD

client = Groq(api_key=GROQ_API_KEY)


# ----------------------------
# STRICT GENERATION FUNCTION
# ----------------------------
def generate_answer(context, question, source="documents"):
    """
    Generates answer strictly from given context.
    Prevents hallucination using strict prompt + temperature=0.
    """

    if source == "documents":
        instruction = """
You are a strict academic assistant.

IMPORTANT RULES:
- Answer ONLY using the provided document context.
- If the answer is not clearly present, say:
  "The answer is not available in the uploaded documents."
- Do NOT guess.
- Do NOT use prior knowledge.
- Do NOT add extra information.
"""
    else:
        instruction = """
You are a knowledgeable assistant.

RULES:
- Use the provided web search results as your primary source.
- You may summarize and combine information from multiple results.
- Provide a clear and direct answer.
- If no useful information exists in the web results, say:
  "The information is not available from web search results."
- Do NOT invent facts.
"""
    prompt = f"""
{instruction}

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()


# ----------------------------
# MAIN QUERY PROCESSOR
# ----------------------------
def process_query(question):

    vectordb = load_vector_store()

    # Retrieve top 3 documents (no score filtering)
    docs = vectordb.similarity_search(question, k=3)

    # ----------------------------
    # STEP 1: TRY DOCUMENTS
    # ----------------------------
    if docs:

        context = ""

        for doc in docs:
            source = doc.metadata.get("source", "Unknown")
            context += f"Source: {source}\n"
            context += doc.page_content + "\n\n"

        doc_answer = generate_answer(context, question, source="documents")

        # If model successfully answered from docs
        if "not available" not in doc_answer.lower():
            return f"📄 Answer from Documents:\n\n{doc_answer}"

    # ----------------------------
    # STEP 2: TRY WEB SEARCH
    # ----------------------------
    web_results = search_web(question)

    if not web_results:
        return "❌ The answer is not available in uploaded documents and no web results were found."

    web_context = ""

    for r in web_results:
        web_context += f"Title: {r.get('title', '')}\n"
        web_context += f"Content: {r.get('body', '')}\n"
        web_context += f"Source: {r.get('href', '')}\n\n"

    web_answer = generate_answer(web_context, question, source="web")

    if "not verified" in web_answer.lower():
        return "❌ The answer could not be found in documents or verified from web results."

    return f"🌐 Answer from Web:\n\n{web_answer}"