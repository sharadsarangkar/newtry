text = input("Enter a string: ")

count = sharad
for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)
