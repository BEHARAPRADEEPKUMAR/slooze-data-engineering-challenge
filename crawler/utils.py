import time
import random

def polite_delay(seconds):
    """Wait politely to avoid blocking"""
    time.sleep(seconds + random.uniform(0.5, 1.5))
