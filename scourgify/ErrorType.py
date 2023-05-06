import sys


class ErrorType:
    def __init__(self, result=None, is_error=False, error_message=""):
        self.result = result
        self.is_error = is_error
        self.error_message = error_message

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    @property
    def is_error(self):
        return self._is_error

    @is_error.setter
    def is_error(self, is_error):
        self._is_error = is_error

    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        self._error_message = f"[Error]:{error_message}" if self._is_error else ""

    def __str__(self):
        return f"result: {self._result} {self._error_message}"

    def __eq__(self, other):
        is_equal = other.result == self.result
        is_equal &= other.is_error == self.is_error
        is_equal &= other.error_message == self.error_message
        return is_equal


def create_error(error_message: str):
    return ErrorType(result=None, is_error=True, error_message=error_message)


def create_result(result):
    return ErrorType(result=result)


def pipe(result: ErrorType, next_func):
    new_result = next_func(result)
    if new_result.is_error:
        exit_program(new_result)
    return new_result


def exit_program(error_type: ErrorType):
    print(error_type.error_message)
    sys.exit()
