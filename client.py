import Pyro4

first_number = input("First number:")
second_number = input("Second number:")
action = input("Action:").strip()

Calculator = Pyro4.Proxy("PYRONAME:Calculator")
print(Calculator.calculate(first_number,second_number,action))