# Backend
This backend is implemented in Django. 

## Requests and Responses
### 1. `add_new_campaign`

**URL:** `/campaigns/add/`  
**Method:** `GET` or `POST`  

**Request:**

- **GET:**  
  Returns the HTML form for adding a new campaign.  

- **POST:**  
  Form data submitted to create a new campaign. Example fields:

| Field  | Type   | Description                 |
|--------|--------|-----------------------------|
| name   | string | Name of the campaign        |
| budget | number | Total budget for campaign   |
| spend  | number | Amount spent                |
| status | string | One of: "In Budget", "Warning", "Out of Budget" |

## 2. `view_all_campaigns`

**URL:** `/campaigns/view/`  
**Method:** `GET`  

**Request:**  
No parameters required.

**Response:** JSON array of all campaigns.

**Success Response Example:**

```json
[
  {
    "id": 1,
    "name": "Account A",
    "budget": 1000,
    "spend": 50,
    "status": "In Budget"
  },
  {
    "id": 2,
    "name": "Account B",
    "budget": 500,
    "spend": 300,
    "status": "Warning"
  },
  {
    "id": 3,
    "name": "Account C",
    "budget": 100,
    "spend": 150,
    "status": "Out of Budget"
  }
]

## How to Run Locally
Create a Python Virtual Environment
```
python -m venv backend_env
backend_env\Scripts\activate
```

Install Requirements
```
python -m pip install -r requirements.txt
```

Ensure Database is Populated
```
python manage.py migrate
```

Run Local Server
*Ensure in src/ directory*
```
py manage.py runserver
```

Deactivate Virtual Environment When Finished
```
deactivate
```