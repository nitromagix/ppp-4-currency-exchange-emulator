class Currency:

    currencies =  {'CHF': 0.930023, #swiss franc 
                    'CAD': 1.264553, #canadian dollar
                    'GBP': 0.737414, #british pound
                    'JPY': 111.019919, #japanese yen
                    'EUR': 0.862361, #euro
                    'USD': 1.0} #us dollar
        
    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    @staticmethod
    def new_from_int_float_or_currency(input):
        new_currency = None
        if type(input) == int or type(input) == float:
            new_currency = Currency(input)
        elif type(input) == Currency:
            new_currency = Currency(input.value, input.unit)
        else:
            print("Could not create currency from input")
        return new_currency

    def changeTo(self, new_unit):
        """
          An Currency object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    #add magic methods here
    def __repr__(self):
        # This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.
        return f"{self.value} {self.unit}"

    def __str__(self):
        #This method returns the same value as __repr__(self).
        return f"{self.value} {self.unit}"

    def __add__(self, other):
        #Defines the '+' operator. If other is a Currency object, the currency values are added and the result will be the unit of self. If other is an int or a float, other will be treated as a USD value.
        _other = Currency.new_from_int_float_or_currency(other)
        _other.changeTo(self.unit)
        sum = round(self.value + _other.value, 2)
        return Currency(sum, self.unit)

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return Currency(other).__add__(self)

    def __sub__(self, other):
        _other = Currency.new_from_int_float_or_currency(other)
        _other.changeTo(self.unit)
        difference = round(self.value - _other.value, 2)
        return Currency(difference, self.unit)

    def __isub__(self, other):
        return self.__sub__(other)

    def __rsub__(self, other):
        return Currency(other).__sub__(self)


v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")

print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 
