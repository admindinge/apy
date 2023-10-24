
def greet_user():
    name = input("ᲠᲐ ᲒᲥᲕᲘᲐ ᲨᲔᲜ?? ")
    print(f"ᲒᲐᲛᲐᲠᲯᲝᲑᲐ, {name}!")
    
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("ᲨᲔᲪᲓᲝᲛᲐ; ᲣᲜᲓᲐ ᲨᲔᲛᲝᲘᲧᲕᲐᲜᲝ ᲛᲗᲔᲚᲘ ᲠᲘᲪᲮᲕᲘ.")

def get_single_character_input(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) == 1 and user_input.isalpha():
            return user_input
        else:
            print("ᲨᲔᲘᲧᲕᲐᲜᲔ ᲛᲮᲝᲚᲝᲓ ᲔᲠᲗᲘ ᲡᲘᲛᲑᲝᲚᲝ (ᲐᲡᲝ).")


def get_language_code_input(prompt):
    valid_languages = ["en", "ru", "ge"]  # ᲔᲜᲔᲑᲘ

    while True:
        user_input = input(prompt)
        if user_input in valid_languages:
            return user_input
        else:
            print("ᲨᲔᲛᲝᲘᲧᲕᲐᲜᲔ ᲔᲜᲘᲡ ᲙᲝᲓᲘ (ᲛᲐᲒᲐᲚᲘᲗᲐᲓ, 'en', 'ru', 'ge').")



# ᲤᲣᲜᲥᲪᲘᲔᲑᲘᲡ ᲒᲐᲛᲝᲧᲔᲜᲔᲑᲐ
greet_user()

# age = get_integer_input("ᲠᲐᲛᲓᲔᲜᲘ ᲬᲚᲘᲡ ᲮᲐᲠ? ")
# print(f"ᲨᲔᲜ ᲮᲐᲠ {age} ᲬᲚᲘᲡ.")

# character = get_single_character_input("ᲨᲔᲘᲧᲕᲐᲜᲔ ᲛᲮᲝᲚᲝᲓ ᲔᲠᲗᲘ ᲡᲘᲛᲑᲝᲚᲝ: ")
# print(f"ᲨᲔᲜ ᲨᲔᲘᲧᲕᲐᲜᲔ ᲡᲘᲛᲑᲝᲚᲝ: {character}")

# language_code = get_language_code_input("ᲨᲔᲘᲧᲕᲐᲜᲔ ᲔᲜᲘᲡ ᲙᲝᲓᲘ (ᲛᲐᲒᲐᲚᲘᲗᲐᲓ, 'en', 'ru', 'ge'): ")
# print(f"ᲨᲔᲜ ᲐᲛᲝᲘᲠᲩᲘᲔ ᲔᲜᲘᲡ ᲙᲝᲓᲘ: {language_code}")