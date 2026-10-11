text = input("Введите строку: ")
text2 = ""
for j in reversed(text):
    text2+=j
if(text == text2):
    print("Палиндром!")
else:
    print("Не палиндром!")