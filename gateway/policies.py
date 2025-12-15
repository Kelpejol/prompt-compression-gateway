class PolicyViolation(Exception):
    pass


def enforce_max_tokens(prompt: str, max_tokens: int, tokenizer):
    tokens = tokenizer.encode(prompt)
    if len(tokens) > max_tokens:
        raise PolicyViolation("Prompt exceeds max token limit")


def enforce_cost_limit(token_count: int, max_cost_tokens: int):
    if token_count > max_cost_tokens:
        raise PolicyViolation("Estimated cost too high")
