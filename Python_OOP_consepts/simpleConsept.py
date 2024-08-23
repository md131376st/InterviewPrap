class Sample:
    def __init__(self):
        """constructor with private variable var """

        self.__var = 0

    def print(self):
        print(self.__var)

    def get_var(self):
        return self.__var

    pass


class SampleChild(Sample):
    def __init__(self):
        super().__init__()
        self.__var2 = -1

    def print(self):
        print(f"variable is {self.__var}")

    pass


sample1 = Sample()
