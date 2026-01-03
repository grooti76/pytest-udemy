from main import userManager
import pytest

@pytest.fixture


def user_manager():
    return userManager()


def test_add_user(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com") == True
    assert user_manager.get_user_email("john_doe") == "john@example.com"
    
def test_to_add_existing_user(user_manager):
    user_manager.add_user("jane_doe", "jane@example.com")
    assert user_manager.add_user("jane_doe", "jane2@example.com") == "User already exists."
    