import chunk
import chromadb
from google import genai
import os


# GOOGLE_API_KEY is qw5uvdw2ll7iwll7yjwx8cio7nu0r45qwl160vg
google_api_key = os.getenv("GOOGLE_API_KEY")
google_client = genai.Client()

EMBEDDING_MODEL = "gemini-embedding-exp-03-07"
LLM_MODEL = "gemini-2.5-flash-preview-05-20"

chromadb_client = chromadb.PersistentClient( path= os.path.join(os.path.dirname(__file__), "chroma.db")  )
chromadb_collection = chromadb_client.get_or_create_collection("xiaomingdou")


def embed(text:str, store:bool=False) -> list[float]:
    result = google_client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
        config = {
            "task_type": "RETRIEVAL_DOCUMENT" if store else "RETRIEVAL_QUERY"
        }
    )
    assert result.embeddings
    assert result.embeddings[0].values
    return result.embeddings[0].values

def create_db() -> None:
    for idx, c in enumerate(chunk.get_chunks()):
        print(f"Processing chunk {idx+1} of {len(chunk.get_chunks())}")
        embedding = embed(c, store=True)
        chromadb_collection.upsert(
            ids=str(idx),
            embeddings=embedding,
            documents=c
        )
def query_db(question: str) -> list[str]:
    question_embedding = embed(question, store=False)
    results = chromadb_collection.query(query_embeddings=question_embedding, n_results=3)
    assert results["documents"]
    return results["documents"][0]

if __name__ == '__main__':
    # create_db()
    question = "令狐冲领悟到了什么魔法？"
    chunks = query_db(question)
    prompt = "Please answer user's question according to context\n"
    prompt += f"Question: {question}\n"
    prompt += f"Context:  \n"
    for c in chunks:
        prompt += f"{c}\n"
        prompt += "------------------------\n"
    
    # print(prompt)
    result = google_client.models.generate_content(
        model = LLM_MODEL,
        contents = prompt
    )
    print(result)
#   content=Content(
#     parts=[
#       Part(
#         text="""根据上下文，令狐冲领悟到的**不是魔法**。

# 文中明确指出：“**这不是魔法**，这是他以独孤九剑的“意”与“势”，结合史莱姆的特性，催发出的能量爆发！他将其戏称为“破爆式”。”"""