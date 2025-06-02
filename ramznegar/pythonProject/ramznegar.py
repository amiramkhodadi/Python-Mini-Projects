user_text = input("Enter your text: ")
list_of_ord = []
for a in user_text:
    list_of_ord.append(str(ord(a)))

print(','.join(list_of_ord))

