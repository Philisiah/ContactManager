class MoneyError(Exception):

    def __str__(self):
        return "Money Exception: We cannot afford to hire :"


class Fellow:

    fellows_hired = 0

    def __init__(self, name, country):
        try:
            if Fellow.fellows_hired < 4:
                self.name = name
                self.country = country
                Fellow.fellows_hired += 1
            else:
                raise MoneyError
        except MoneyError:
            print(MoneyError(), name)


# for num in range(10):
#   name = input("Enter Name: ")
#   cntry = input("Enter Country: ")
#   Fellow(name, cntry)
