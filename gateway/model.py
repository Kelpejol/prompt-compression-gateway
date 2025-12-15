from pydantic import BaseModel

class CompressionRequest(BaseModel):
    prompt: str
    max_tokens: int = 2048
    compression_ratio: float = 0.5


class CompressionResponse(BaseModel):
    original_tokens: int
    compressed_tokens: int
    compressed_prompt: str
