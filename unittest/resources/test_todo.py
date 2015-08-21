import json

from app import db, Todo, TodoList, User
from unittest import ResourceTest


class TestTodo(ResourceTest):
    """Superclass for helper methods.
    """
    def mySetup(self):
        self.user = User('Test User', 'test@test.com', 'password')
        self.todoList = TodoList('Test List', 1)
        db.session.add(self.user)
        db.session.add(self.todoList)
        db.session.commit()

    def myTeardown(self):
        pass


class TestTodo_get(TestTodo):
    """Test cases for the get API endpoint.
    """
    def test_get_success(self):
        """Verify todo is successfully returned.
        """
        todo = Todo('Test Subject', 1, None, 'Test Description', 3, False, 1)
        db.session.add(todo)
        db.session.commit()

        resp = self.client.get('/todos/%s' % todo.id)

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusMsg': 'Ok',
                'statusDetails': {},
                'statusCode': 'HTTPOK'
            },
            'result': {
                'id': 1,
                'subject': 'Test Subject',
                'dueDate': None,
                'description': 'Test Description',
                'priority': 3,
                'completed': False,
                'assignee': 'Test User',
                'list': 'Test List'
            }
        }

    def test_get_notFound(self):
        """Verify notFound is raised if todo with the given id does not exist.
        """
        resp = self.client.get('/todos/1000')

        assert resp.status_code == 404
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 404,
                'statusMsg': 'Not found',
                'statusDetails': {}
            },
            'result': {}
        }

    def test_get_todoMultiSuccess(self):
        """Verify list of todos is successfully returned.
        """
        todo1 = Todo('Test1 Subject', 1, None, 'Test1 Description', 3, False, 1)
        todo2 = Todo('Test2 Subject', 1, None, 'Test2 Description', 3, False, 1)
        db.session.add(todo1)
        db.session.add(todo2)
        db.session.commit()

        resp = self.client.get('/todos/')

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusMsg': 'Ok',
                'statusDetails': {},
                'statusCode': 'HTTPOK'
            },
            'result': [
                {
                    'id': 1,
                    'subject': 'Test1 Subject',
                    'dueDate': None,
                    'description': 'Test1 Description',
                    'priority': 3,
                    'completed': False,
                    'assignee': 'Test User',
                    'list': 'Test List'
                },
                {
                    'id': 2,
                    'subject': 'Test2 Subject',
                    'dueDate': None,
                    'description': 'Test2 Description',
                    'priority': 3,
                    'completed': False,
                    'assignee': 'Test User',
                    'list': 'Test List'
                }
            ]
        }


class TestTodo_post(TestTodo):
    """Test cases for the post API endpoint.
    """
    def test_post_success(self):
        """Verify new todo is successfully returned.
        """
        todo = {
            'subject': 'Test Subject',
            'todoListId': 1,
            'dueDate': None,
            'description': 'Test Description',
            'priority': 3,
            'completed': 0,
            'assigneeId': 1
        }

        resp = self.client.post('/todos/?todolist=1', data=todo)

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusMsg': 'Ok',
                'statusDetails': {},
                'statusCode': 'HTTPOK'
            },
            'result': {
                'id': 1,
                'subject': 'Test Subject',
                'dueDate': None,
                'description': 'Test Description',
                'priority': 3,
                'completed': False,
                'assignee': 'Test User',
                'list': 'Test List'
            }
        }

    def test_post_badRequest(self):
        """Verify badRequest is raised if todo fields are missing.
        """
        todo = {}
        resp = self.client.post('/todos/', data=todo)

        assert resp.status_code == 400
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 400,
                'statusMsg': 'Bad request',
                'statusDetails': {}
            },
            'result': {}
        }

class TestTodo_put(TestTodo):
    """Test cases for the put API endpoint.
    """
    def test_put_success(self):
        """Verify updated todo is successfully returned.
        """
        todo = Todo('Test Subject', 1, None, 'Test Description', 3, False, 1)
        db.session.add(todo)
        db.session.commit()

        newTodoData = {
            'subject': 'New Subject',
            'priority': 2,
            'completed': 1
        }

        resp = self.client.put('/todos/%s' % todo.id, data=newTodoData)

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusMsg': 'Ok',
                'statusDetails': {},
                'statusCode': 'HTTPOK'
            },
            'result': {
                'id': 1,
                'subject': 'New Subject',
                'dueDate': None,
                'description': 'Test Description',
                'priority': 2,
                'completed': True,
                'assignee': 'Test User',
                'list': 'Test List'
            }
        }

    def test_put_notFound(self):
        """Verify notFound is raised if todo with the given id does not exist.
        """
        resp = self.client.put('/todos/1000')

        assert resp.status_code == 404
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 404,
                'statusMsg': 'Not found',
                'statusDetails': {}
            },
            'result': {}
        }


class TestTodo_delete(TestTodo):
    """Test cases for the delete API endpoint.
    """
    def test_delete_success(self):
        """Verify todo is successfully deleted.
        """
        todo = Todo('Test Subject', 1, None, 'Test Description', 3, False, 1)
        db.session.add(todo)
        db.session.commit()

        resp = self.client.delete('/todos/%s' % todo.id)

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusMsg': 'Ok',
                'statusDetails': {},
                'statusCode': 'HTTPOK'
            },
            'result': None
        }

    def test_delete_notFound(self):
        """Verify notFound is raised if todo with the given id does not exist.
        """
        resp = self.client.delete('/todos/1000')

        assert resp.status_code == 404
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 404,
                'statusMsg': 'Not found',
                'statusDetails': {}
            },
            'result': {}
        }
