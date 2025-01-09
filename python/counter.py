class Counter:
    def __init__(self):
        self.__count = 0
        self.__is_closed = False

    def add(self):
        if self.__is_closed:
            raise Exception("Resource is closed")
        self.__count += 1

    def get_count(self):
        return self.__count

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__is_closed = True