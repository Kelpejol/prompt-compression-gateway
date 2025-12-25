"""
Tests for the FastAPI application.
"""
import pytest
from fastapi.testclient import TestClient
from gateway.main import app



client = TestClient(app)


class TestHealthEndpoint:
    """Tests for health check endpoint."""
    
    def test_health_returns_200(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"


class TestRootEndpoint:
    """Tests for root endpoint."""
    
    def test_root_returns_info(self):
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "version" in data


class TestCompressionEndpoint:
    """Tests for compression endpoint."""
    
    def test_compress_success(self):
        """Test successful compression."""
        response = client.post("/compress", json={
            "prompt": "This is a test prompt that should be compressed successfully.",
            "max_tokens": 512,
            "compression_ratio": 0.5
        })
        assert response.status_code == 200
        data = response.json()
        assert "original_tokens" in data
        assert "compressed_tokens" in data
        assert "compressed_prompt" in data
        assert data["compressed_tokens"] < data["original_tokens"]
    
    def test_compress_with_defaults(self):
        """Test compression with default values."""
        response = client.post("/compress", json={
            "prompt": "Short prompt."
        })
        assert response.status_code == 200
    
    def test_compress_empty_prompt_fails(self):
        """Test that empty prompts are rejected."""
        response = client.post("/compress", json={
            "prompt": "",
            "max_tokens": 512
        })
        assert response.status_code == 422
    
    def test_compress_exceeds_token_limit(self):
        """Test policy violation for excessive tokens."""
        long_prompt = "word " * 10000
        response = client.post("/compress", json={
            "prompt": long_prompt,
            "max_tokens": 100
        })
        assert response.status_code == 400
        assert "token limit" in response.json()["detail"].lower()
    
    def test_compress_invalid_ratio(self):
        """Test invalid compression ratio."""
        response = client.post("/compress", json={
            "prompt": "Test prompt",
            "compression_ratio": 1.5  # Invalid: > 1.0
        })
        assert response.status_code == 422
    
    def test_compress_ratio_too_low(self):
        """Test compression ratio below minimum."""
        response = client.post("/compress", json={
            "prompt": "Test prompt",
            "compression_ratio": 0.1  # Invalid: < 0.2
        })
        assert response.status_code == 422


class TestInputValidation:
    """Tests for input validation."""
    
    def test_missing_prompt_field(self):
        """Test request without prompt field."""
        response = client.post("/compress", json={
            "max_tokens": 512
        })
        assert response.status_code == 422
    
    def test_invalid_max_tokens_type(self):
        """Test invalid max_tokens type."""
        response = client.post("/compress", json={
            "prompt": "Test",
            "max_tokens": "not_a_number"
        })
        assert response.status_code == 422
    
    def test_negative_max_tokens(self):
        """Test negative max_tokens value."""
        response = client.post("/compress", json={
            "prompt": "Test",
            "max_tokens": -100
        })
        assert response.status_code == 422
