from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        return self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        try:
            if index < 0:
                raise IndexError
            desired_value = self._data[index]
        except IndexError:
            raise IndexError("Índice Inválido ou Inexistente")
        else:
            return desired_value
