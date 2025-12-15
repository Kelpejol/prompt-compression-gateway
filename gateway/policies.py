import tiktoken

class PolicyViolation(Exception):
    pass


tokenizer = tiktoken.get_encoding("cl100k_base")


def enforce_token_limit(prompt: str, max_tokens: int):
    tokens = tokenizer.encode(prompt)
    if len(tokens) > max_tokens:
        raise PolicyViolation("Prompt exceeds token limit")
    return len(tokens)
def enforce_compression_ratio(original_prompt: str, compressed_prompt: str, ratio: float):
    original_tokens = len(tokenizer.encode(original_prompt))
    compressed_tokens = len(tokenizer.encode(compressed_prompt))
    if compressed_tokens > original_tokens * ratio:
        raise PolicyViolation("Compression ratio not met")
    return original_tokens, compressed_tokens