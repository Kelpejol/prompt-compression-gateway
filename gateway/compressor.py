"""
Prompt compression using LLMLingua.
"""
from llmlingua import PromptCompressor


# Initialize compressor (lazy loaded)
_compressor = None


def get_compressor() -> PromptCompressor:
    """Get or initialize the prompt compressor."""
    global _compressor
    if _compressor is None:
        _compressor = PromptCompressor(
            model_name="microsoft/llmlingua-2-bert-base-multilingual-cased-meetingbank",
            device="cpu"  # Change to "cuda" if GPU available
        )
    return _compressor


def compress_prompt(prompt: str, ratio: float) -> str:
    """
    Compress a prompt using LLMLingua.
    
    Args:
        prompt: The prompt text to compress
        ratio: Compression ratio (0.0 to 1.0)
               Lower values = more compression
               
    Returns:
        str: The compressed prompt
        
    Example:
        >>> compress_prompt("This is a long prompt...", 0.5)
        "This long prompt..."
    """
    compressor = get_compressor()
    
    result = compressor.compress_prompt(
        prompt,
        compression_ratio=ratio,
        use_context_level_filter=True,
        use_token_level_filter=True,
    )
    
    return result["compressed_prompt"]
