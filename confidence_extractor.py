import whisper
model = whisper.load_model("base")
result = model.transcribe("sample_audio.wav", logprob_threshold=-1.0)
threshold = 0.85  
output = []
for segment in result["segments"]:
    confidence = segment.get("avg_logprob", None)
    if confidence is not None:
        conf_score = pow(10, confidence) if confidence < 0 else confidence
        flag = "needs_review" if conf_score < threshold else "ok"
        output.append({
            "segment": segment["text"],
            "confidence": round(conf_score, 2),
            "flag": flag
        })
for item in output:
    print(item)
