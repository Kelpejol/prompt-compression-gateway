from fastapi import FastAPI, HTTPException

from models import CompressionRequest, CompressionResponse
from policies import enforce_token_limit, PolicyViolation
from compressor import compress_prompt

app = FastAPI(
    title="Policy-Aware Prompt Compression Gateway",
    description="Enforces prompt policies before LLM execution",
)

@app.post("/compress", response_model=CompressionResponse)
def compress(req: CompressionRequest):
    try:
        original_tokens = enforce_token_limit(
            req.prompt,
            req.max_tokens
        )

        compressed = compress_prompt(
            req.prompt,
            req.compression_ratio
        )

        compressed_tokens = len(compressed.split())

        return CompressionResponse(
            original_tokens=original_tokens,
            compressed_tokens=compressed_tokens,
            compressed_prompt=compressed
        )

    except PolicyViolation as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result["compressed_prompt"]