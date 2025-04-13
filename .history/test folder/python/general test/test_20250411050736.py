def logger(msg1):
    def sufix(msg2):
        result = f"{msg1}: {msg2}"
        return result
    return sufix

error_logger = logger("ERROR")
error_logger("File not found")
