from setuptools import setup, find_packages

setup(
    name="prompt-compression-gateway",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "llmlingua==0.2.1",
        "fastapi==0.104.1",
        "uvicorn[standard]==0.24.0",
        "tiktoken==0.5.1",
        "pydantic==2.5.0",
        "python-multipart==0.0.6",
    ],
    python_requires=">=3.9",
)
