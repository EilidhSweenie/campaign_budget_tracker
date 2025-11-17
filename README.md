# Campaign Budget Tracker 
A tool to view and add marketing campaigns, including budget, spend, and status, built with Django (backend) and Vue 3 + Vuetify (frontend).

## Tech Stack

- **Backend:** Django, SQLite 
- **Frontend:** Vue 3, Vuetify
- **HTTP client:** Axios
- **Containerisation:** Docker, docker-compose

## Running with Docker

## Assumptions & Limitations

- For simplicity, CSRF is disabled on the /campaigns/add/ endpoint. In a production setup I would enable CSRF and either proxy the frontend through Django or share the CSRF token via cookies/meta tags

## Possible Improvements
- Currently the user provides the status directly, this field could be omitted and calculated based on budget and spend in the backend. This would save the user time and prevent any misclassifications. 