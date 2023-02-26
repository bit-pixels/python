# str.format() =    optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)

# {} = format field
print("The {} jumped over the {}".format("cow", "moon"))
print("The {0} jumped over the {1}".format(animal, item))   # positional arguments
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))   # keyword arguments

text = "The {} jumped over the {}"
print(text.format("cow", "moon"))

name = "Jack"

print("My name is {}".format(name))
print("My name is {:10}".format(name, name))   # amount of padding
print("My name is {:<10}".format(name, name))  # < = left align
print("My name is {:>10}".format(name, name))  # > = right align
print("My name is {:^10}".format(name, name))  # ^ = center align

number = 1000

print("The number is {:.3f}".format(number))  # 3 Decimal Places
print("The number is {:,}".format(number))    # prints 1,000
print("The number is {:b}".format(number))    # Binary Output
print("The number is {:o}".format(number))    # Octal Number Output
print("The number is {:X}".format(number))    # Hexadecimal Output
print("The number is {:E}".format(number))    # Scientific Notation Output
