from awskit.lib import common
import os

class Config:
    def __init__(self, environment: str):
        self.environment = environment

    def get_environment(self) -> str:
        common.second_shared_function()
        return self.environment
