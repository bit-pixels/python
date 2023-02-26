# **kwargs. parameter that will pack all arguments into a dictionary. useful for allowing varying keyword arguments.

def hello(**kwargs):
    try:
        print("Hello", kwargs["first"], kwargs["middle"], kwargs["last"] + "!")
    except KeyError:
        print("Hello", kwargs["first"], kwargs["last"] + "!")


hello(first="Jack", last="Booth")
