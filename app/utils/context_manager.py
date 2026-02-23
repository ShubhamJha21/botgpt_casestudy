# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 10:55:50 2026

@author: Shubham Jha
"""

from app.config import MAX_HISTORY_MESSAGES

def build_context(messages):
    # sliding window
    return messages[-MAX_HISTORY_MESSAGES:]