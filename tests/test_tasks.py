import unittest
import requests

BASE_URL = "http://localhost:8000"

class TestTaskAPI(unittest.TestCase):

    def setUp(self):
        # This method will run before each test
        self.invalid_id = 99999
        self.task = {
            "title": "Test Task",
            "description": "This is a test task.",
            "status": "Pending"
        }

        # Create a task to test update and delete operations
        response = requests.post(f"{BASE_URL}/tasks", json=self.task)
        self.task_id = response.json().get('id')

    def test_create_task(self):
        # Test creating a new task
        response = requests.post(f"{BASE_URL}/tasks", json=self.task)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data['title'], self.task['title'])
        self.assertEqual(data['description'], self.task['description'])
        self.assertEqual(data['status'], self.task['status'])

    def test_create_task_with_invalid_status(self):
        # Test creating a new task with an invalid status
        created_task = {
            "title": "Test Task",
            "description": "This is a test task.",
            "status": "Invalid Status"
        }
        response = requests.post(f"{BASE_URL}/tasks", json=created_task)
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertEqual(data['detail'], f'Invalid task status: Invalid Status')

    def test_get_all_tasks(self):
        # Test retrieving all tasks
        response = requests.get(f"{BASE_URL}/tasks")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_task_by_id(self):
        # Test retrieving a task by ID
        response = requests.get(f"{BASE_URL}/tasks/{self.task_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['id'], self.task_id)

    def test_get_task_by_id_with_nonexistent_id(self):
        # Test retrieving a task by ID
        response = requests.get(f"{BASE_URL}/tasks/{self.invalid_id}")
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertEqual(data['detail'], 'Task not found')

    def test_update_task(self):
        # Test updating a task
        updated_task = {
            "title": "Updated Task Title",
            "description": "Updated Task Description",
            "status": "In Progress"
        }
        response = requests.put(f"{BASE_URL}/tasks/{self.task_id}", json=updated_task)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['title'], updated_task['title'])
        self.assertEqual(data['description'], updated_task['description'])
        self.assertEqual(data['status'], updated_task['status'])

    def test_update_task_with_nonexistent_id(self):
        # Test updating a task
        updated_task = {
            "title": "Updated Task Title",
            "description": "Updated Task Description",
            "status": "In Progress"
        }
        response = requests.put(f"{BASE_URL}/tasks/{self.invalid_id}", json=updated_task)
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertEqual(data['detail'], 'Task not found')

    def test_update_task_with_invalid_status(self):
        # Test updating a task
        updated_task = {
            "title": "Updated Task Title",
            "description": "Updated Task Description",
            "status": "Invalid Status"
        }
        response = requests.put(f"{BASE_URL}/tasks/{self.task_id}", json=updated_task)
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertEqual(data['detail'], 'Invalid task status: Invalid Status')

    def test_delete_task(self):
        # Test deleting a task
        response = requests.delete(f"{BASE_URL}/tasks/{self.task_id}")
        self.assertEqual(response.status_code, 204)

        # Verify the task is deleted
        response = requests.get(f"{BASE_URL}/tasks/{self.task_id}")
        self.assertEqual(response.status_code, 404)

    def test_delete_task_with_nonexistent_id(self):
        # Test deleting a task
        response = requests.get(f"{BASE_URL}/tasks/{self.invalid_id}")
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        # This method will run after each test, cleaning up any tasks created during tests
        requests.delete(f"{BASE_URL}/tasks/{self.task_id}")

if __name__ == "__main__":
    unittest.main()
