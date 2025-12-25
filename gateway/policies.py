"""
Policy enforcement for token limits and compression rules.
"""
import tiktoken


class PolicyViolation(Exception):
    """Raised when a policy constraint is violated."""
    pass


# Initialize tokenizer for token counting
tokenizer = tiktoken.get_encoding("cl100k_base")


def enforce_token_limit(prompt: str, max_tokens: int) -> int:
    """
    Enforce token limit policy on a prompt.
    
    Args:
        prompt: The input prompt to check
        max_tokens: Maximum allowed tokens
        
    Returns:
        int: The actual token count
        
    Raises:
        PolicyViolation: If prompt exceeds token limit
    """
    tokens = tokenizer.encode(prompt)
    token_count = len(tokens)
    
    if token_count > max_tokens:
        raise PolicyViolation(
            f"Prompt exceeds token limit: {token_count} > {max_tokens}"
        )
    
    return token_count


def enforce_compression_ratio(
    original_prompt: str,
    compressed_prompt: str,
    target_ratio: float
) -> tuple[int, int]:
    """
    Verify compression achieved target ratio.
    
    Args:
        original_prompt: Original prompt text
        compressed_prompt: Compressed prompt text
        target_ratio: Target compression ratio (e.g., 0.5 = 50%)
        
    Returns:
        Tuple of (original_tokens, compressed_tokens)
        
    Raises:
        PolicyViolation: If compression ratio not met
    """
    original_tokens = len(tokenizer.encode(original_prompt))
    compressed_tokens = len(tokenizer.encode(compressed_prompt))
    
    actual_ratio = compressed_tokens / original_tokens if original_tokens > 0 else 1.0
    
    # Allow 10% tolerance
    if actual_ratio > target_ratio * 1.1:
        raise PolicyViolation(
            f"Compression ratio not met: {actual_ratio:.2f} > {target_ratio}"
        )
    
    return original_tokens, compressed_tokens
