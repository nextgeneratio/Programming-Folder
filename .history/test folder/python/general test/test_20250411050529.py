def logger(msg1):
    def sufix(msg2):
        print(msg1, msg2)
    return sufix