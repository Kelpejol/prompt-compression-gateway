"""
Pydantic models for request/response validation.
"""
from pydantic import BaseModel, Field, field_validator


class CompressionRequest(BaseModel):
    """Request model for prompt compression."""
    
    prompt: str = Field(
        ...,
        min_length=1,
        description="The prompt text to compress"
    )
    max_tokens: int = Field(
        default=2048,
        ge=1,
        le=8192,
        description="Maximum allowed tokens before compression"
    )
    compression_ratio: float = Field(
        default=0.5,
        ge=0.2,
        le=0.9,
        description="Target compression ratio (0.2 = aggressive, 0.9 = minimal)"
    )
    
    @field_validator('prompt')
    @classmethod
    def prompt_not_empty(cls, v: str) -> str:
        """Validate prompt is not just whitespace."""
        if not v.strip():
            raise ValueError("Prompt cannot be empty or whitespace only")
        return v


class CompressionResponse(BaseModel):
    """Response model for compressed prompts."""
    
    original_tokens: int = Field(
        ...,
        description="Number of tokens in original prompt"
    )
    compressed_tokens: int = Field(
        ...,
        description="Number of tokens after compression"
    )
    compressed_prompt: str = Field(
        ...,
        description="The compressed prompt text"
    )
    
    @property
    def compression_ratio_achieved(self) -> float:
        """Calculate actual compression ratio achieved."""
        if self.original_tokens == 0:
            return 0.0
        return self.compressed_tokens / self.original_tokens
