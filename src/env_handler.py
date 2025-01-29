import os
from dotenv import load_dotenv

class EnvHandler:
    def __init__(self, env_file=".env"):
        """
        Initializes the EnvironmentHandler with a specified .env file.
        :param env_file: Path to the .env file.
        """
        self.env_file = env_file
        self._load_environment()

    def _load_environment(self):
        """
        Load environment variables from the specified .env file.
        """
        if os.path.exists(self.env_file):
            load_dotenv(self.env_file)
            print(f"Environment variables loaded from {self.env_file}")
        else:
            print(f".env file '{self.env_file}' not found. Using system environment variables.")

    @staticmethod
    def get_variable(key, default=None):
        """
        Get an environment variable's value.
        :param key: The environment variable key.
        :param default: The default value if the key is not found.
        :return: The value of the environment variable or the default value.
        """
        return os.getenv(key, default)
