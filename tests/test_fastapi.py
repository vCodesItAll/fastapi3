from fastapi import FastAPI
from fastapi.testclient import TestClient

import pytest
import httpx

import sys
sys.path.insert(1, '/workspace/fastapi3/')
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}