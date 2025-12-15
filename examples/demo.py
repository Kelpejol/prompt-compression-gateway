import requests

prompt = """
You are an autonomous agent tasked with evaluating
a multi-layered system involving distributed execution,
policy enforcement, and failure recovery mechanisms.
"""

res = requests.post(
    "http://localhost:8000/compress",
    json={
        "prompt": prompt,
        "max_tokens": 512,
        "compression_ratio": 0.5
    }
)

print(res.json())
