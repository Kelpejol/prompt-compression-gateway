# 🚀 Prompt Compression Gateway

A production-ready API gateway that compresses LLM prompts and enforces token policies before execution.

## 🎯 Why This Exists

LLM prompts are getting longer and more expensive. This gateway helps by:
- 💰 **Cost Reduction** - Smart compression reduces token usage
- 🛡️ **Policy Enforcement** - Token limits before API calls
- ⚡ **Fast Processing** - Efficient compression with LLMLingua-2

## ✨ Features

- Intelligent prompt compression
- Configurable token limits
- REST API with FastAPI
- Docker support
- Comprehensive tests
- Clear documentation

## 🚀 Quick Start

### Installation

```bash
# Clone the repo
git clone https://github.com/kelpejol/prompt-compression-gateway.git
cd prompt-compression-gateway

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn gateway.main:app --reload
```

### Docker

```bash
docker-compose up -d
```

### First API Call

```bash
curl -X POST http://localhost:8000/compress \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "You are an AI assistant helping with code review.",
    "max_tokens": 512,
    "compression_ratio": 0.5
  }'
```

## 📖 API Documentation

### POST `/compress`

Compress a prompt with policy enforcement.

**Request:**
```json
{
  "prompt": "string",
  "max_tokens": 2048,
  "compression_ratio": 0.5
}
```

**Response:**
```json
{
  "original_tokens": 150,
  "compressed_tokens": 75,
  "compressed_prompt": "compressed text here"
}
```

**Interactive Docs:** Visit `http://localhost:8000/docs` after starting the server.

## 🏗️ Architecture

```
Client Request
     ↓
Token Policy Check
     ↓
LLMLingua Compression
     ↓
Compressed Output
```

## 🧪 Testing

```bash
# Run tests
pytest

# With coverage
pytest --cov=gateway

# Specific test file
pytest tests/test_api.py
```

## 🛠️ Development

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Format code
black gateway/ tests/

# Run linter
ruff check gateway/
```

## 📦 Deployment

### Using Docker

```bash
docker build -t prompt-gateway .
docker run -p 8000:8000 prompt-gateway
```

### Environment Variables

```bash
HOST=0.0.0.0
PORT=8000
MAX_TOKENS_DEFAULT=2048
COMPRESSION_RATIO_DEFAULT=0.5
```

See `.env.example` for all options.

## 🤝 Contributing

Contributions are welcome! Please check out [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LLMLingua](https://github.com/microsoft/LLMLingua) for compression
- [FastAPI](https://fastapi.tiangolo.com/) for the framework

## 📞 Support

- 🐛 [Report Issues](https://github.com/kelpejol/prompt-compression-gateway/issues)
- 💬 [Discussions](https://github.com/kelpejol/prompt-compression-gateway/discussions)
