# Campaign Budget Tracker 
A tool to view and add marketing campaigns, including budget, spend, and status, built with Django (backend) and Vue 3 + Vuetify (frontend).

## Tech Stack

- **Backend:** Django, SQLite 
- **Frontend:** Vue 3, Vuetify
- **HTTP client:** Axios
- **Containerisation:** Docker, docker-compose

## Running with Docker
Please find below instructions on how to run the tool with docker compose:

1. Clone reposititory 
```
git clone https://github.com/EilidhSweenie/campaign_budget_tracker.git
```
2. Navigate to root directory 
```
cd campaign_budget_tracker
```
3. Run docker compose
```
docker-compose up
```

Once docker compose has executed, the tool will be avialable at *http://localhost:5173/*

If you prefer to run the frontend/backend directly, instructions on how to do so are available in the READMEs of those directories.

## Possible Improvements
- Currently the user provides the status directly, this field could be omitted and calculated based on budget and spend in the backend. This would save the user time and prevent any misclassifications. 
- In the future I would add tests to ensure functionality works as expected. 
- Currently the tool only runs locally, to productionise it I would add extra features such as handling csrf tokens and using a more robust database