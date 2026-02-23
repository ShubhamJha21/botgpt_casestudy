# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 11:05:51 2026

@author: Shubham Jha
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import *
from app.services.conversation_service import create_conversation, add_message
from app.models import Conversation, Message

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/conversations")
def start_conversation(request: CreateConversationRequest, db: Session = Depends(get_db)):
    conv_id, reply = create_conversation(db, request.user_id, request.mode, request.first_message)
    return {"conversation_id": conv_id, "assistant_reply": reply}

@router.post("/conversations/{conversation_id}/messages")
def continue_chat(conversation_id: str, request: AddMessageRequest, db: Session = Depends(get_db)):
    reply = add_message(db, conversation_id, request.message)
    return {"assistant_reply": reply}

@router.get("/conversations/{conversation_id}")
def get_conversation(conversation_id: str, db: Session = Depends(get_db)):
    conversation = db.query(Conversation).filter(Conversation.id == conversation_id).first()
    if not conversation:
        raise HTTPException(status_code=404, detail="Not found")

    messages = db.query(Message).filter(Message.conversation_id == conversation_id).all()
    return {
        "id": conversation.id,
        "mode": conversation.mode,
        "messages": [{"role": m.role, "content": m.content} for m in messages]
    }

@router.delete("/conversations/{conversation_id}")
def delete_conversation(conversation_id: str, db: Session = Depends(get_db)):
    conversation = db.query(Conversation).filter(Conversation.id == conversation_id).first()
    if not conversation:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(conversation)
    db.commit()
    return {"message": "Deleted"}