from exceptions import ZamceneDvereException


class Dvere:
    def __init__(self, zamceno: bool):
        self.zamceno = zamceno
    def otevrit(self):
        if self.zamceno:
            raise ZamceneDvereException
        else:
            return True
