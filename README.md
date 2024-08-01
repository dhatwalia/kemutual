# Kent & Essex Mutual Insurance

Python and SQLite based solution to Task Management Pre-Interview Coding Exercise

## Table of Contents

- [Task Management System](#project)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)

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

1. **Start the server:**
   ```sh
   uvicorn app.main:app --reload
   ```

2. **Access the application:**
   Open browser and navigate to `http://127.0.0.1:8000/tasks`.

3. **Interacting with the API:**
   - Use tools like Postman or cURL to interact with the API endpoints.
   - The API documentation is available at `http://127.0.0.1:8000/docs` (Swagger UI) or `http://127.0.0.1:8000/redoc` (ReDoc).
