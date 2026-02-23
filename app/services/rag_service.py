# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 11:03:59 2026

@author: Shubham Jha
"""

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from app.config import TOP_K_RAG

model = SentenceTransformer("all-MiniLM-L6-v2")
index = None
documents = []

def build_index(text_chunks):
    global index, documents
    documents = text_chunks
    embeddings = model.encode(text_chunks)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

def retrieve(query):
    if index is None:
        return []

    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), TOP_K_RAG)

    return [documents[i] for i in indices[0]]