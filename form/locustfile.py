from locust import HttpUser, task, between
import random
import string


class UserBehavior(HttpUser):
    wait_time = between(5, 9)

    @task
    def create_user_and_fill_form(self):
        # Create a user
        username = self.random_username()
        email = f"{username}@google.com"
        password = self.random_password()

        self.client.post("/api/user/register/", json={
            "username": username,
            "email": email,
            "password": password
        })

        credentials = {
            "username": username,
            "password": password
        }
        response = self.client.post("/api/user/login/", json=credentials)
        token = response.json().get("token")

        # Fill form with user info
        form_data = [
            {"field_id": 1, "value": "Test Value 1"},
            {"field_id": 2, "value": "Test Value 2"},
            {"field_id": 3, "value": "Female"},
            {"field_id": 4, "value": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.goodhousekeeping.com%2Flife%2Fpets%2Fa43276342%2Fcat-instagram-captions%2F&psig=AOvVaw3dh3mrO1nJmcuRiyT1Px7F&ust=1703063459630000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCKji4vaTm4MDFQAAAAAdAAAAABAN"}

        ]

        token = "Token {}".format(token)

        headers = {
            "Authorization": token
        }

        self.client.post("/api/form/submit/1/", headers=headers, json={"fields": form_data})


    def random_username(self):
        return ''.join(random.choices(string.ascii_letters, k=8))

    def random_password(self):
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(chars, k=12))
