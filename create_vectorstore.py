#!/usr/bin/env python3
"""
Script to create a FAISS vectorstore from Corona_NLP_test.csv
This vectorstore can be used in langchain_notebook_3.ipynb exercises
"""

import os
import pandas as pd
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
CSV_PATH = "Corona_NLP_test.csv"
OUTPUT_DIR = "faiss_index"
BATCH_SIZE = 100  # Process embeddings in batches to avoid rate limits


def main():
    """Create FAISS vectorstore from CSV data"""

    # Check if API key is available
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with: OPENAI_API_KEY=your-key-here")
        return

    print(f"✅ API key loaded: {api_key[:12]}...")

    # Load CSV
    print(f"\n📊 Loading data from {CSV_PATH}...")
    try:
        # Handle CSV with potential embedded quotes and commas
        df = pd.read_csv(CSV_PATH, escapechar="\\", on_bad_lines="skip")
        print(f"✅ Loaded {len(df)} rows")
        print(f"Columns: {df.columns.tolist()}")
    except FileNotFoundError:
        print(f"❌ Error: {CSV_PATH} not found")
        return
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        return

    # Convert to LangChain documents
    print("\n📝 Converting to documents...")
    documents = []
    for idx, row in df.iterrows():
        # Skip rows with missing tweets
        if pd.isna(row["OriginalTweet"]) or str(row["OriginalTweet"]).strip() == "":
            continue

        # Create document with tweet text and metadata
        doc = Document(
            page_content=str(row["OriginalTweet"]),
            metadata={
                "sentiment": (
                    str(row["Sentiment"]) if pd.notna(row["Sentiment"]) else "Unknown"
                ),
                "location": (
                    str(row["Location"]) if pd.notna(row["Location"]) else "Unknown"
                ),
                "tweet_date": (
                    str(row["TweetAt"]) if pd.notna(row["TweetAt"]) else "Unknown"
                ),
                "row_id": idx,
            },
        )
        documents.append(doc)

    print(f"✅ Created {len(documents)} documents")

    # Initialize embeddings
    print("\n🔢 Initializing embeddings model...")
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key=api_key)

    # Create vectorstore
    print(f"\n🚀 Creating FAISS vectorstore (this may take a minute)...")
    try:
        vectorstore = FAISS.from_documents(documents=documents, embedding=embeddings)
        print("✅ Vectorstore created successfully")
    except Exception as e:
        print(f"❌ Error creating vectorstore: {e}")
        return

    # Save vectorstore
    print(f"\n💾 Saving vectorstore to {OUTPUT_DIR}...")
    try:
        vectorstore.save_local(OUTPUT_DIR)
        print(f"✅ Vectorstore saved to {OUTPUT_DIR}/")
    except Exception as e:
        print(f"❌ Error saving vectorstore: {e}")
        return

    # Test the vectorstore
    print("\n🧪 Testing vectorstore with sample query...")
    test_query = "funny comments"
    results = vectorstore.similarity_search(test_query, k=3)
    print(f"\nTop 3 results for '{test_query}':")
    for i, doc in enumerate(results, 1):
        print(f"\n{i}. {doc.page_content[:100]}...")
        print(f"   Sentiment: {doc.metadata['sentiment']}")

    print("\n✅ All done! Vectorstore is ready to use in langchain_notebook_3.ipynb")
    print(f"\nTo load it in your notebook:")
    print(f"```python")
    print(f"vectorstore = FAISS.load_local(")
    print(f"    '{OUTPUT_DIR}',")
    print(f"    embeddings,")
    print(f"    allow_dangerous_deserialization=True")
    print(f")")
    print(f"```")


if __name__ == "__main__":
    main()
