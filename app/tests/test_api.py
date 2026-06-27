from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_confidence_api_ok(monkeypatch):
    fake_result = {
        "segments": [
            {"text": "I worked with Python and FastAPI", "avg_logprob": -0.03},
            {"text": "Ths iz noisyy exmple", "avg_logprob": -0.38},
        ]
    }
    def fake_transcribe(audio_file, logprob_threshold=-1.0):
        return fake_result
    monkeypatch.setattr("app.main.model.transcribe", fake_transcribe)
    response = client.post("/confidence", json={"audio_file": "dummy.wav"})
    assert response.status_code == 200
    data = response.json()
    assert data[0]["flag"] == "ok"
    assert data[1]["flag"] == "needs_review"
def test_confidence_api_error(monkeypatch):
    def fake_transcribe(audio_file, logprob_threshold=-1.0):
        raise RuntimeError("Audio file not found")
    monkeypatch.setattr("app.main.model.transcribe", fake_transcribe)
    response = client.post("/confidence", json={"audio_file": "missing.wav"})
    assert response.status_code == 500
    assert response.json()["detail"] == "Audio file not found"
