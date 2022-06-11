from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the identifier
    for authentication instead of usernames
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and saves a User with the given email and password.

        Args:
            email (_type_): _description_
            password (_type_): _description_

        Raises:
            ValueError: _description_
        """
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
