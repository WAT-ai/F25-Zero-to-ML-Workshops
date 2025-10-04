from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ✨ TODO: Replace this with YOUR favorite website!
# Examples:
# - Sports: "https://www.espn.com/nba/"
# - Movies/TV: "https://www.imdb.com/title/tt0944947/" (Game of Thrones)
# - Music: "https://www.billboard.com/charts/hot-100/"
WEBSITE_URL = "https://example.com"

print(f"📥 Loading content from: {WEBSITE_URL}")

# Load the website content
loader = WebBaseLoader(WEBSITE_URL)
documents = loader.load()

print(f"✅ Loaded {len(documents)} document(s)")

# Clean up whitespace from documents
import re
for doc in documents:
    # Replace multiple whitespace characters with a single space
    doc.page_content = re.sub(r'\s+', ' ', doc.page_content).strip()

print("🧹 Cleaned up excess whitespace")

# ✨ TODO: Experiment with these values!
# chunk_size: How big each text chunk should be (500-2000 works well)
# chunk_overlap: How much chunks overlap (helps maintain context)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# Split the documents into chunks
chunks = text_splitter.split_documents(documents)
print(f"📄 Split into {len(chunks)} chunks")

# Create embeddings
print("🔮 Creating embeddings...")
embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))

# Create and save the vectorstore
print("💾 Creating vectorstore...")
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("vectorstore")

print("🎉 Vectorstore created successfully!")
print("👉 Now run: streamlit run frontend.py")
