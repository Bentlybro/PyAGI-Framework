
# Configuration settings for the AGI system
import json

class Config:
    def __init__(self):
        self.learning_rate = 0.001
        self.memory_capacity = 1000000
        self.reasoning_depth = 5
        self.consciousness_threshold = 0.8

    def load_config(self, config_file):
        with open(config_file, 'r') as f:
            config_data = json.load(f)
            self.__dict__.update(config_data)