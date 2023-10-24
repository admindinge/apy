def get_single_character_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            if len(user_input) != 1:
                raise ValueError("ᲨᲔᲘᲧᲕᲐᲜᲔ ᲛᲮᲝᲚᲝᲓ ᲔᲠᲗᲘ ᲡᲘᲛᲑᲝᲚᲝ.")
            if user_input.isdigit():
                raise ValueError("ᲠᲘᲪᲮᲕᲘᲡ ᲨᲔᲧᲕᲐᲜᲐ ᲐᲠ ᲘᲧᲝ ᲡᲐᲭᲘᲠᲝ")
            if not user_input.isalpha():
                raise ValueError("ᲡᲘᲛᲑᲝᲚᲝ ᲐᲠᲘᲡ a, b, გ, დ და ა. შ.")
            return user_input
        except ValueError as e:
            print(f"Შ Ე Ც Დ Ო Მ Ა!: {e}")
            
def get_language_code(prompt):
    valid_languages = ["en", "ru", "ge"]  # ენების დასაშვები სია

    while True:
        try:
            user_input = input(prompt)
            if user_input not in valid_languages:
                raise ValueError("ᲣᲜᲓᲐ ᲨᲔᲘᲧᲕᲐᲜᲝ ᲮᲔᲚᲛᲘᲡᲐᲬᲓᲝᲛᲘ ᲔᲜᲘᲓᲐᲜ ᲔᲠᲗᲔᲠᲗᲘ (ᲛᲐᲒᲐᲚᲘᲗᲘ, 'en', 'ru', 'ge').")
            return user_input
        except ValueError as e:
            print(f"ᲨᲔᲪᲓᲝᲛᲐ: {e}")




# ფუნქციების გამოყენება
character = get_single_character_input("ᲨᲔᲘᲧᲕᲐᲜᲔ: ")
print(f"ᲨᲔᲜ ᲨᲔᲘᲧᲕᲐᲜᲔ: {character}")


# language_code = get_language_code("ᲨᲔᲘᲧᲕᲐᲜᲔ ᲔᲜᲘᲡ ᲙᲝᲓᲘ (en, ru, ge и т. д.): ")
# print(f"ᲗᲥᲕᲔᲜ ᲐᲛᲝᲐᲠᲩᲘᲔᲗ ᲔᲜᲐ: {language_code}")