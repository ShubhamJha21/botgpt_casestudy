# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 10:56:43 2026

@author: Shubham Jha
"""

import requests
from app.config import OLLAMA_URL, MODEL_NAME

def call_llm(messages):
    prompt = ""

    for msg in messages:
        prompt += f"{msg['role']}: {msg['content']}\n"

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]