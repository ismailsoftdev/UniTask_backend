from django.db import models

class UserManager(models.Manager):
    
    def create_user(self, full_name, email, password=None, **extra_fields):
        """
        Create a new user.

        Args:
            full_name (str): The full name of the user.
            email (str): The email address of the user.
            password (str, optional): The password for the user. Defaults to None.
            **extra_fields: Additional fields to be passed when creating the user.

        Returns:
            User: The newly created user object.
        """
        user = self.model(full_name=full_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, full_name, email, password=None, **extra_fields):
        """
        Create a new superuser.

        Args:
            full_name (str): The full name of the superuser.
            email (str): The email address of the superuser.
            password (str, optional): The password for the superuser. Defaults to None.
            **extra_fields (dict): Additional fields for the superuser.

        Returns:
            User: The newly created superuser object.
        """
        user = self.create_user(full_name=full_name, email=email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    def deactivate_user(self, user):
        """
        Deactivates a user.

        Args:
            user (User): The user to be deactivated.

        Returns:
            None
        """
        user.is_active = False
        user.save()
    
    def activate_user(self, user):
        """
        Activate a user by setting their `is_active` attribute to `True` and saving the user.

        Parameters:
        - `user`: The user object to be activated.

        Returns:
        None
        """
        user.is_active = True
        user.save()
    
    def change_password(self, user, current_password, new_password):
        """
        Change the password for a user.

        Args:
            user (User): The user object for which the password needs to be changed.
            current_password (str): The current password of the user.
            new_password (str): The new password to be set for the user.

        Returns:
            bool: True if the password is successfully changed, False otherwise.
        """
        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()
            return True
    
    def get_by_natural_key(self, email):
        return self.get(email=email)