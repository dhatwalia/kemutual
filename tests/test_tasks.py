import unittest
import requests

BASE_URL = "http://localhost:8000"

class TestTaskAPI(unittest.TestCase):

    def setUp(self):
        # This method will run before each test
        self.new_task = {
            "title": "Test Task",
            "description": "This is a test task.",
            "status": "Pending"
        }

        # Create a task to test update and delete operations
        response = requests.post(f"{BASE_URL}/tasks", json=self.new_task)
        self.task_id = response.json().get('id')

    def test_create_task(self):
        # Test creating a new task
        response = requests.post(f"{BASE_URL}/tasks", json=self.new_task)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data['title'], self.new_task['title'])
        self.assertEqual(data['description'], self.new_task['description'])
        self.assertEqual(data['status'], self.new_task['status'])

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

    def test_delete_task(self):
        # Test deleting a task
        response = requests.delete(f"{BASE_URL}/tasks/{self.task_id}")
        self.assertEqual(response.status_code, 204)

        # Verify the task is deleted
        response = requests.get(f"{BASE_URL}/tasks/{self.task_id}")
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        # This method will run after each test, cleaning up any tasks created during tests
        requests.delete(f"{BASE_URL}/tasks/{self.task_id}")

if __name__ == "__main__":
    unittest.main()
