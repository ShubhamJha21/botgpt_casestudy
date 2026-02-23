# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 11:04:37 2026

@author: Shubham Jha
"""

from sqlalchemy.orm import Session
from app.models import Conversation, Message
from app.services.llm_service import call_llm
from app.services.rag_service import retrieve
from app.utils.context_manager import build_context

def create_conversation(db: Session, user_id: str, mode: str, first_message: str):
    conversation = Conversation(user_id=user_id, mode=mode)
    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    user_msg = Message(conversation_id=conversation.id, role="user", content=first_message)
    db.add(user_msg)
    db.commit()

    reply = generate_reply(db, conversation, first_message)

    return conversation.id, reply

def generate_reply(db: Session, conversation: Conversation, user_message: str):
    messages = db.query(Message).filter(Message.conversation_id == conversation.id).all()

    formatted = [{"role": m.role, "content": m.content} for m in messages]

    if conversation.mode == "rag":
        retrieved = retrieve(user_message)
        context_text = "\n".join(retrieved)
        formatted.append({"role": "system", "content": f"Context:\n{context_text}"})

    formatted = build_context(formatted)

    assistant_reply = call_llm(formatted)

    assistant_msg = Message(conversation_id=conversation.id, role="assistant", content=assistant_reply)
    db.add(assistant_msg)
    db.commit()

    return assistant_reply

def add_message(db: Session, conversation_id: str, message: str):
    conversation = db.query(Conversation).filter(Conversation.id == conversation_id).first()

    user_msg = Message(conversation_id=conversation_id, role="user", content=message)
    db.add(user_msg)
    db.commit()

    reply = generate_reply(db, conversation, message)

    return reply