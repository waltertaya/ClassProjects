class Electronic:
    def __init__(self):
        print("1")


class OSDevice(Electronic):
    def __init__(self):
        print("2")


class Smartphone(OSDevice):
    def __init__(self):
        super().__init__()
        print("3")


sm = Smartphone()
