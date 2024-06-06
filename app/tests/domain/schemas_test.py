from unittest import main, TestCase
from pydantic import ValidationError

from app.domain.schemas import User


class TestValidateUser(TestCase):
    def test_should_return_400_with_taken_sku(self):
        with self.assertRaises(ValidationError) as context:
            User(email="test@gmail.com", id=None, is_active=True, items=[])

        self.assertIsNotNone(context)


if __name__ == "__main__":
    main()
