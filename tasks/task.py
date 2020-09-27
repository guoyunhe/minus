"""Base Task Class"""

from qtpy.QtCore import Property, QObject, Signal, Slot


class Task(QObject):
    """
    Task Class
    """

    __size = 0
    size_changed = Signal(int)

    def get_size(self):
        '''Size getter'''
        return self.__size

    def set_size(self, size):
        '''Size setter'''
        self.__size = size
        self.size_changed.emit(size)

    size = Property(int, get_size, set_size, notify=size_changed)

    @Slot()
    def scan(self):
        '''Check if the task is needed, and return options if needed'''
        print('scan...')
        self.set_size(2000)

    @Slot()
    def exec(self):
        '''Run the task with options'''
        print('exec...')
        self.set_size(0)
