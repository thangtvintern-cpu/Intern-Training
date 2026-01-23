# Training FastAPI
** Data from OJT(Python Basic) data_json.pkl **

## API Endpoints

- GET /purchases
- GET /purchases/{user_id}
- GET /purchases/{user_id}/total-price
- GET /purchases/{user_id}/total-price/{purchase_id}
Path Variable: 
 - user_id: 4GzCLpB5a2TcaGLHqyNsYm
 - purchase_id: QZsJXL22zcuEdHcEozpnYK


 ## Set up environment

 1. Create virtual environment
 - python -m venv .venv
 - .venv\Scripts\activate
 2. Install dependencies
 - pip install fastapi[standard]
 3. Run the server
 - fastapi dev main.py
