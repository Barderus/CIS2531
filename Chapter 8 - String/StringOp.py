'''
Embedded escapesequences
'''

print('Single quoted with embedded \'single\' quotes')

print('single uote with embedded \nnewline')

print('single quoted with embedded \ttab')

print('First letter of the alphabet is \x41')

print(str(123))

longMessage = "Python " "programming " "is " "fun"
print(longMessage)

#Raw stops the escape sequence
print(r'Single quoted with embedded \nnew line')

print(f"Here is my secret message {longMessage}")

greeting = "HELLO"

for ch in greeting:
    print(ch, end=" ")
    
# Count the amount of that in a sequence 
greeting.count("L")

greeting.isupper()

greeting.islower()

greeting.isdigit()