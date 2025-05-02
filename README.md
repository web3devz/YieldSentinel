
# Verifier API Project

This is a complete FastAPI-based web service to analyze yield strategies for performance scores and benchmark yields.

## ✅ Features

- API endpoint `/analyze` to compute scores from submitted data.
- Real-time computation based on JSON strategy history.
- Uses weighted averages and volatility for fair scoring.

## 📦 Files

- `verifier_logic.py`: Core yield performance logic.
- `verifier_api.py`: FastAPI app with endpoint.
- `sample_data.json`: Example payload for testing.

## 🚀 How to Run

### Install dependencies
```bash
pip install fastapi uvicorn
```

### Start the server
```bash
uvicorn verifier_api:app --reload
```

### Test the endpoint
Use Postman or CURL:

```bash
curl -X POST http://127.0.0.1:8000/analyze \
-H "Content-Type: application/json" \
-d @sample_data.json
```

## 📄 Output
You’ll receive JSON with:
- `benchmarkYield`
- `performanceScore`
- `recommendation`
