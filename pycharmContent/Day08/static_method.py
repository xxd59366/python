class Date:
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    @staticmethod
    def is_date_valid(string_date):
        year, month, date = map(int, string_date.split('-'))
        return 1 <= date <= 31 and 1 <= month <= 12 and year < 3999


if __name__ == '__main__':
    print(Date.is_date_valid('2018-02-04'))
    print(Date.is_date_valid('2018-22-04'))
