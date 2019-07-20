from traitlets import Unicode, default
from traitlets.config import ArgumentError

import json
from jsonschema import validate

from jupyterhub.auth import LocalAuthenticator

users_schema = {
        'type': 'array',
        'items': {
            'type': 'object',
            'properties': {
                'username': {'type': 'string'},
                'password': {'type': 'string'},
            },
            'required': ['username', 'password']
        }
}


class JsonAuthenticator(LocalAuthenticator):

    auth_file = Unicode(
        None,
        config=True,
        allow_none=True,
        help="JSON file with list of {username:'the-username', password:'some-password'}. See documentation for more details."
    )

    @default('create_system_users')
    def _create_system_users_default(self):
        return True

    def __init__(self, *args, **kwargs):
        super(LocalAuthenticator, self).__init__(*args, **kwargs)
        self.load_users()

    def load_users(self):
        """Loads user data from the auth_file and validates it
        """
        with open(self.auth_file) as f:
            users = json.load(f)
            validate(users, schema=users_schema)
            return users

    async def authenticate(self, handler, data):
        users = self.load_users()
        username = data['username']
        password = data['password']

        for user in users:
            if user['username'] == username and user['password'] == password:
                return username

        return None
