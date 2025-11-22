"This activity re-aquaints users with common methods with strings, ints, and floats"

__author__ = "Will Lam lamwillp88@gmail.com"

#2.3 Personal Message
name = "homie"
print(f"Yo, {name.title()} you wanna be an analyst?")

#2.4 Name Cases
name_2 = "will"
print(name_2.lower())
print(name_2.upper())
print(name_2.title())

#2.56 Famous Quote
author = "Will Hunting"
quote = "Do you like apples?"
message = f"{author} once said, {quote}"
print(message)

#2.7 Stripping Names
stripper_name = "  KiKi  "
print(stripper_name.lstrip())
print(stripper_name.rstrip())
print(stripper_name.strip())
print("\tDiamond")
print("Stripper Names:\n\tKiki\n\tDiamond\n\tRubi")

#2.8 Remove Prefixes and Suffixes
filename = "python_notes.txt"
filename.removesuffix(".txt")

#2.910 Print Favorite Number
favorite_number = 88
print(f"{favorite_number} is my favorite number!")
