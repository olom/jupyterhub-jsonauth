# Jupyerhub JSON Authenticator

This package extends the built in LocalAuthenticator adding support for a simple JSON file to specify users.


## Installation

First install Jupyter Hub and all the required dependencies.

Then run:


```bash
pip install .
```


## Usage

First create a file with desired users and passwords conforming to the following schema:

```javascript
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
```

Then tell Jupyerhub to use it.

From the command line:

```bash
jupyterhub --JupyterHub.authenticator_class='json' --JsonAuthenticator.auth_file='path/to/users.json' [other arguments]
```

From the config file:

```python
c.JupyterHub.authenticator_class = 'json'
c.JsonAuthenticator.auth_file = 'path/to/users.json'
```

As this authenticator extends LocalAuthenticator it needs the hub to be run with enough privileges to create new users
(for example, with sudo).

Another option is to modify the parameter JsonAuthenticator.add_user_cmd
It uses the original convention from Jupyterhub:

```python
# This is a fragment from jupyerhub/auth.py
    add_user_cmd = Command(
        help="""
        The command to use for creating users as a list of strings

        For each element in the list, the string USERNAME will be replaced with
        the user's username. The username will also be appended as the final argument.

        For Linux, the default value is:

            ['adduser', '-q', '--gecos', '""', '--disabled-password']

        To specify a custom home directory, set this to:

            ['adduser', '-q', '--gecos', '""', '--home', '/customhome/USERNAME', '--disabled-password']

        This will run the command:

            adduser -q --gecos "" --home /customhome/river --disabled-password river

        when the user 'river' is created.
        """
    ).tag(config=True)

    @default('add_user_cmd')
    def _add_user_cmd_default(self):
        """Guess the most likely-to-work adduser command for each platform"""
        if sys.platform == 'darwin':
            raise ValueError("I don't know how to create users on OS X")
        elif which('pw'):
            # Probably BSD
            return ['pw', 'useradd', '-m']
        else:
            # This appears to be the Linux non-interactive adduser command:
            return ['adduser', '-q', '--gecos', '""', '--disabled-password']
```
