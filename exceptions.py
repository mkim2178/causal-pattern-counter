class InvalidInputException(Exception):
    def __init__(self, message):
        super().__init__(message)
    
class MissingGraphException(Exception):
    def __init__(self, message):
        super().__init__(message)
