# Flask MongoDB CRUD Application

## Requirements
- Docker
- Docker Compose

## Setup

1. Clone the repository:

```bash
git clone https://github.com/soham2312/CRUD.git
cd CRUD
```

2. Create and activate virtual environment

```bash
bashCopypython -m venv venv

# Windows
venv\Scripts\activate

# Unix/MacOS
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4 .Configure environment variables
Create a .env file in the project root:

```bash
MONGO_URI=Mongo_connection_string
DATABASE_NAME=flask_mongo_crud
SECRET_KEY=your-secret-key-here
FLASK_DEBUG=True
HOST=0.0.0.0
PORT=5000
```
5 .Run the application

```bash
Copypython run.py
```
##Docker Setup

Build and run with Docker Compose

```bash
docker-compose up --build
```

#API Endpoints
##User Management
1. Create User
```bash
POST /user
Content-Type: application/json

{
    "name": "John Doe",
    "email": "john@example.com"
}
```
2. Get User
```bash
GET /user/<user_id>
```
3. Update User
```bash
PUT /user/<user_id>
Content-Type: application/json

{
    "name": "Updated Name",
    "email": "updated@example.com"
}
```
4. Delete User
```bash
DELETE /user/<user_id>
```
5. List All Users
```bash
GET /users
```






