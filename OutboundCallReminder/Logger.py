import enum

class Logger(enum.Enum):

    INFORMATION=1
    ERROR=2

    @staticmethod
    def log_message(message_type, message):
        log_message = message_type.name + " : " + message
        print(log_message)