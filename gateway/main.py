"""
Main FastAPI application for prompt compression gateway.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from gateway.models import CompressionRequest, CompressionResponse
from gateway.policies import enforce_token_limit, PolicyViolation
from gateway.compressor import compress_prompt

app = FastAPI(
    title="Prompt Compression Gateway",
    description="Enforce policies and compress LLM prompts",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "Prompt Compression Gateway",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {
        "status": "healthy",
        "service": "prompt-compression-gateway"
    }


@app.post("/compress", response_model=CompressionResponse)
async def compress(req: CompressionRequest):
    """
    Compress a prompt with policy enforcement.
    
    Args:
        req: Compression request with prompt and parameters
        
    Returns:
        CompressionResponse with token counts and compressed prompt
        
    Raises:
        HTTPException: If policy violation occurs
    """
    try:
        # Enforce token limit policy
        original_tokens = enforce_token_limit(
            req.prompt,
            req.max_tokens
        )

        # Compress the prompt
        compressed = compress_prompt(
            req.prompt,
            req.compression_ratio
        )

        # Count compressed tokens
        from gateway.policies import tokenizer
        compressed_tokens = len(tokenizer.encode(compressed))

        return CompressionResponse(
            original_tokens=original_tokens,
            compressed_tokens=compressed_tokens,
            compressed_prompt=compressed
        )

    except PolicyViolation as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Compression failed: {str(e)}")
