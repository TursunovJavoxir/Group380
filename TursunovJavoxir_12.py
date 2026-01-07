class CheckYear:
    def __init__(self, year: int):
        self.year = year

    def is_check(self) -> bool:
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def result(self) -> str:
        if self.is_check():
            return "Високосный"
        else:
            return "Не високосный"