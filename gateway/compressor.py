from llmlingua import PromptCompressor

compressor = PromptCompressor(
    model_name="microsoft/llmlingua-2-bert-base-multilingual-cased-meetingbank"
)

def compress_prompt(prompt: str, ratio: float):
    result = compressor.compress_prompt(
        prompt,
        compression_ratio=ratio
    )
    return result["compressed_prompt"]
