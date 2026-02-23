# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 17:42:05 2026

@author: Shubham Jha
"""

from fastapi import FastAPI
from app.database import Base, engine
from app.routes import conversations
from contextlib import asynccontextmanager

from app.services.rag_service import build_index
Base.metadata.create_all(bind=engine)

app = FastAPI(title="BOT GPT")

#  Lifespan handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    
    # ---- Startup logic ----
    print("Building RAG index...")

    chunks = [
        "Shubham Jha works as data scientist",
        "shubham works in ford motors",
        "They are used in LLMs like GPT."
    ]

    build_index(chunks)

    print("RAG index built successfully.")

    yield   # App runs here

    # ---- Shutdown logic (optional) ----
    print("Shutting down application...")


# Create app with lifespan
app = FastAPI(title="BOT GPT", lifespan=lifespan)
# 
# @app.on_event("startup")
# def startup_event():
#     chunks = [
#         "Transformers are deep learning models.",
#         "Attention mechanism helps focus on important words.",
#         "They are used in LLMs like GPT."
#     ]
#     build_index(chunks)


app.include_router(conversations.router)