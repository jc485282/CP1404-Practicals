from Prac07.programminglanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


print(ruby)
print(python)
print(vb)

# Line break
print()

languages = [ruby, python, vb]

for language in languages:
    if language.is_dynamic():
        print(language)
