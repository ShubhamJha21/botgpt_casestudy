# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 02:45:17 2026

@author: Shubham Jha
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_start_conversation():
    response = client.post("/conversations", json={
        "user_id": "123",
        "mode": "open",
        "first_message": "Hello"
    })
    assert response.status_code == 200