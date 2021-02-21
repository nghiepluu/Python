

greeting = "Hello there"
animal = "Donkey"
sound = "Hee Haw"
print(greeting.capitalize())
print(greeting.upper())
print(greeting.lower().count('h'))
print(greeting.casefold())
print(greeting.encode())
print(greeting.index("Hello"))
print(("The {} say {}").format(animal, sound))
print(("The {a} say {s}").format(a=animal, s=sound))
print(f"The {animal} say {sound}")
print(f'The {animal} say {sound.upper()}')