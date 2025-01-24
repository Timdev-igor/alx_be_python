class Calculator:
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to return the sum of two numbers.
        Does not rely on class or instance-specific data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to return the product of two numbers.
        Prints the class attribute 'calculation_type' before performing multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
