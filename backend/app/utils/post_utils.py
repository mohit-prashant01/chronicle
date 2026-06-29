import math

def calculate_reading_time(content:str)->int:
    words=len(content.split())
    minutes=math.ceil(words/200)
    return max(1,minutes)