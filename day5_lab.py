#task 1: username formatter
a="Janani"
print(a.upper())
print(a.lower())
print(a.title())

#task2: Email validator 
email=input("Enter email:")
print(email[0].isalpha())
print(email.endswith(".com"))

#task3: character counter
text= "Knowledge is wisdom"
print(text.count("o"))
print(text.count("w"))

#task4: search a character
word="Ambition"
if "o" in word:
    print(word.find("o"))
else:
    print("character not found")
    
#task5: password checker
password="student123"
print(password.isalpha())
print(password.isdigit())
print(password.isalnum())

#task6: name decoration
text="welcome"
print(text.center(12,"*"))
print(text.ljust(12,"*"))
print(text.rjust(12,"*"))

#task7: text converter
a="Trust the process"
print(a.upper())
print(a.lower())
print(a.swapcase())

#task 8: replace words
text=input("Enter a sentence:")
print(text.replace("python","java"))

#task9: roll number formatter
a=input("Enter a roll number:")
print(a.zfill(10))

#task10: case analyzer
a="Janani"
print(a.isupper())
print(a.islower())
print(a.istitle())
