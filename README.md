# Confidence-Score-Extractor
* Overview
  Confidence Score Extractor is a speech and audio processing application designed to evaluate transcript reliability.
  The system runs Whisper on audio samples, extracts per-segment confidence/log-probability values, and flags unreliable segments through a FastAPI REST API.

Features:
* Extract per-segment confidence scores
* Flag unreliable transcript segments (needs_review)
* Support for configurable confidence thresholds
* Word-level vs segment-level confidence handling
* REST API using FastAPI
* Request validation with Pydantic
* Logging support
* Unit and API testing with Pytest
* Docker container support

Project Structure:
 *Confidence-Score-Extractor
│
├── app
│   └── main.py              # FastAPI app with /confidence endpoint

│
├── tests
│   └── test_api.py          # Unit tests

│
├── configs
│   └── confidence_terms.json # Glossary of confidence-related terms
│

├── logs
│

├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md
INSTALLATION:
 *Clone Repository
* bash
  git clone https://github.com/<your-username>/Confidence-Score-Extractor.git
  cd Confidence-Score-Extractor
  Create Virtual Environment
* bash
  python -m venv venv
Activate:

Windows:

* bash
 venv\Scripts\activate
 Linux/Mac:

* bash
 source venv/bin/activate
 Install Dependencies

* bash
 pip install -r requirements.txt
 Running Application
 Start FastAPI server:

* bash
 uvicorn app.main:app --reload
 Application runs at:

* Code
  http://127.0.0.1:8000
* API documentation:

* Code
  http://127.0.0.1:8000/docs
  
* API Usage
 Endpoint
 POST /confidence

Input
json
{
  "audio_file": "sample_audio.wav"
}
Output
json
[
  {
    "segment": "I worked with Python and FastAPI",
    "confidence": 0.93,
    "flag": "ok"
  },
  {
    "segment": "Ths iz noisyy exmple",
    "confidence": 0.42,
    "flag": "needs_review"
  }
]
Running Tests
Run:

* bash
 pytest
* Expected:
Code
2 passed

Run container

*bash
docker run -p 8000:8000 confidence-extractor
API will be available at:

Code
http://localhost:8000

** Technologies Used
* Python
* FastAPI
* Whisper (OpenAI)
* Pytest
* Git

** Future Improvements
 * Word-level confidence visualization
 * Integration with transcript cleaner pipeline
 * Multi-language audio support
 * Cloud deployment
 * CI/CD pipeline
