
class Memory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.short_term = {}
        self.long_term = {}
        
    def store(self, key, value, memory_type='short'):
        if memory_type == 'short':
            self.short_term[key] = value
        else:
            self.long_term[key] = value
            
    def retrieve(self, key, memory_type='short'):
        if memory_type == 'short':
            return self.short_term.get(key)
        return self.long_term.get(key)