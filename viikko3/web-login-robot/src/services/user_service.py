import re
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if self._user_repository.find_by_username(username):
           raise UserInputError(f"User with username {username} already exists")

        if re.match(r"^[a-z]{3,}$", username) is None:
            raise UserInputError("Username is not valid")

        if re.match(r"^(?=.*\d)(?=.*[a-z]).{8,}$", password) is None:
            raise UserInputError("Password is not valid")
        
        if password != password_confirmation:
            raise UserInputError("Passwords differs, should be the same")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa


user_service = UserService()
