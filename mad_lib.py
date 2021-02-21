story = """
Roses are {colour1}
Violets are {colour2}
Sugar is {adjective}
And so are you
"""

colour1 = input("Give me a colour: ")
colour2 = input("Give me another colour: ")
adjective = input("And an adjective: ")

print(story.format(colour1=colour1, colour2=colour2, adjective=adjective))