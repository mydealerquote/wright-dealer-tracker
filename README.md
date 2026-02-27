# Wright Dealer Tracker (Personal Use)

## Run Locally
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask run

## Deploy to Railway
- Push to GitHub
- Create new Railway project
- Deploy using Procfile

## Next Step
Implement real API call inside fetcher.py after inspecting the dealer locator network request.
