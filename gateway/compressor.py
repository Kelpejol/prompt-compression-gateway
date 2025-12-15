from llmlingua import PromptCompressor

compressor = PromptCompressor(
    model_name="microsoft/llmlingua-2-bert-base-multilingual-cased-meetingbank"
)

def compress(prompt: str, ratio: float = 0.5):
    result = compressor.compress_prompt(
        prompt,
        compression_ratio=ratio
    )
    return result["compressed_prompt"]
