
from abc import ABC, abstractmethod

class CognitiveArchitecture(ABC):
    def __init__(self, config):
        self.config = config
        self.memory = None
        self.reasoning_engine = None
        self.learning_module = None

    @abstractmethod
    def process_input(self, input_data):
        pass

    @abstractmethod
    def generate_response(self):
        pass

    @abstractmethod
    def update_knowledge(self):
        pass