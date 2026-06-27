from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import whisper

app = FastAPI()

# Load Whisper model once
model = whisper.load_model("base")

class ConfidenceRequest(BaseModel):
    audio_file: str = Field(
        ..., description="Path to the audio file to analyze"
    )

class ConfidenceResponse(BaseModel):
    segment: str
    confidence: float
    flag: str

@app.post("/confidence", response_model=list[ConfidenceResponse])
def extract_confidence(request: ConfidenceRequest):
    try:
        result = model.transcribe(request.audio_file, logprob_threshold=-1.0)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    threshold = 0.85
    output = []

    for segment in result["segments"]:
        confidence = segment.get("avg_logprob", None)
        if confidence is None:
            continue
        conf_score = pow(10, confidence) if confidence < 0 else confidence
        flag = "needs_review" if conf_score < threshold else "ok"
        output.append(
            ConfidenceResponse(
                segment=segment["text"],
                confidence=round(conf_score, 2),
                flag=flag
            )
        )

    return output
