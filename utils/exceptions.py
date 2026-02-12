class CustomException(Exception):
    pass

class NotFoundException(CustomException):
    def __init__(self, message="Not found."):
        self.message = message
        super().__init__(self.message)

class ValidationException(CustomException):
    def __init__(self, message="Validation failed."):
        self.message = message
        super().__init__(self.message)

class DatabaseException(CustomException):
    def __init__(self, message="Database error occurred."):
        self.message = message
        super().__init__(self.message)
