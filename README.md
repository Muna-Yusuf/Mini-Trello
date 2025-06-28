# 📝 Task & Board API

This is a Django REST API for managing boards and tasks with user authentication. It includes endpoints for registering users, creating and managing boards, and adding tasks.

## Endpoints:

- `POST /api/register/` – Create a new user account.
- `GET /api/boards/` – Get all boards belonging to the authenticated user.
- `POST /api/boards/` – Create a new board.
- `GET /api/boards/{id}/` – Get details of a specific board.
- `PUT /api/boards/{id}/` – Update a board's details.
- `DELETE /api/boards/{id}/` – Delete a specific board.
- `GET /api/tasks/` – Get all tasks for boards owned by the authenticated user.
- `POST /api/tasks/` – Create a new task linked to a board.
- `GET /api/tasks/{id}/` – Get details of a specific task.
- `PUT /api/tasks/{id}/` – Update a task's details.
- `DELETE /api/tasks/{id}/` – Delete a specific task.
- `GET /swagger/` – Swagger API docs.

---

## Getting Started:

1. Clone this repository:
    ```bash
    git clone https://github.com/Muna-Yusuf/Mini-Trello.git
    cd Mini-Trello
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv  
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the server:
    ```bash
    python manage.py runserver
    ```

---

## How to Use:

- **Register a user:**
``` bash
POST http://localhost:8000/api/register/ 
```
- Include the following JSON body:
     ```json
         {
            "username": "ali",
            "email": "ali@example.com",
            "password": "yourpassword123*"
        }
    ```
- Use the token to access profile:

- Authorization: Bearer <your_token>

- Create a board:
```bash
POST http://localhost:8000/api/boards/
```
- Include the following JSON body:
     ```json
         {
            "name": "Board Name"
        }
 
   ```
- Get all boards belonging to the authenticated user:
```bash
GET GET http://localhost:8000/api/boards/
```
- Get details of a specific board:

```bash
GET http://localhost:8000/api/boards/{id}/
```
- Create a task linked to a board:
```bash
POST http://localhost:8000/api/tasks/
```
- Include the following JSON body:
     ```json
         {
            "title": "Task Title",
            "description": "Task Description",
            "status": "todo",
            "board": 1  # ID of the board you want to assign the task to
        }
   ```
- Get all tasks for boards owned by the authenticated user:
```bash
GET http://localhost:8000/api/tasks/
```


---

## Testing with Bruno or Postman:

1. Open Bruno or Postman.

2. Create requests for the 3 main endpoints.

3. Register a user, log in, and copy the token.

4. Use the token to authorize the profile request.


---

Made using Django, JWT, and Swagger UI.

