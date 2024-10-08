# Kent & Essex Mutual Insurance

Python and SQLite based solution to Task Management Pre-Interview Coding Exercise

## Table of Contents

- [Task Management System](#project)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API End Point](#api-end-point)
  - [Testing](#testing)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/dhatwalia/kemutual.git
   cd your-repo-name
   ```

2. **Set up a virtual environment:**
   ```sh
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the virtual environment:**
   ```sh
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

2. **Start the server:**
   ```sh
   uvicorn app.main:app --reload
   ```

3. **Access the application:**
   Open browser and navigate to `http://127.0.0.1:8000/tasks`.

4. **Interacting with the API:**
   - Use tools like Postman or cURL to interact with the API endpoints.
   - The API documentation is available at `http://127.0.0.1:8000/docs` (Swagger UI) or `http://127.0.0.1:8000/redoc` (ReDoc).

## API End Point
### Create task
- **POST** `/tasks/`
- **Request Body Example:**
  ```json
   {
      "title": "Task Title",
      "description": "Task Description",
      "status": "Pending"
   }
- **Response Code Example:** `201 Created`
- **Response Body Example:**
   ```json
   {
      "title": "Task Title",
      "description": "Task Description",
      "status": "Pending",
      "id": 1,
      "created_at": "2024-08-01T16:47:59.877894",
      "updated_at": "2024-08-01T16:47:59.877894"
   }
   ```

### Get All Tasks
- **GET** `/tasks/`
- **Response Code Example:** `200 OK`
- **Response Body Example:**
   ```json
   [
      {
         "title": "Task Title",
         "description": "Task Description",
         "status": "Pending",
         "id": 1,
         "created_at": "2024-08-01T16:47:59.877894",
         "updated_at": "2024-08-01T16:47:59.877894"
      },
      {
         "title": "Task Title 2",
         "description": "Task Description 2",
         "status": "In Progress",
         "id": 2,
         "created_at": "2024-08-01T16:45:59.519894",
         "updated_at": "2024-08-01T16:45:03.382894"
      }
   ]
   ```

### Get Task by ID
- **GET** `/tasks/{task_id}`
- **Response Code Example:** `200 OK`
- **Response Body Example:**
   ```json
   {
      "title": "Task Title",
      "description": "Task Description",
      "status": "Pending",
      "id": 1,
      "created_at": "2024-08-01T16:47:59.877894",
      "updated_at": "2024-08-01T16:47:59.877894"
   }
   ```

### Update Task by ID
- **PUT** `/tasks/{task_id}`
- **Request Body Example:**
  ```json
   {
      "title": "New Title",
      "description": "New Description",
      "status": "Completed"
   }
- **Response Code Example:** `200 OK`
- **Response Body Example:**
   ```json
   {
      "title": "New Title",
      "description": "New Description",
      "status": "Completed",
      "id": 1,
      "created_at": "2024-08-01T16:47:59.877894",
      "updated_at": "2024-08-01T16:53:17.628995"
   }
   ```

### Delete Task by ID
- **DELETE** `/tasks/{task_id}`
- **Response Code Example:** `204 No Content`

## Testing
1. **Run the virtual environment:**
   ```sh
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

2. **Start the server:**
   ```sh
   uvicorn app.main:app --reload
   ```

3. **In another session, run the virtual environment:**
   ```sh
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

4. **Run tests:**
   ```sh
   python -m unittest
   ```
