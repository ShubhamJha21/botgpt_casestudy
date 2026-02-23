# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 10:54:39 2026

@author: Shubham Jha
"""

from pydantic import BaseModel
from typing import List

class CreateConversationRequest(BaseModel):
    user_id: str
    mode: str
    first_message: str

class AddMessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    role: str
    content: str

class ConversationDetailResponse(BaseModel):
    id: str
    mode: str
    messages: List[MessageResponse]