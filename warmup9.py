#Ryan Jones
#3/1/18

text = input('Enter text: ')
for ch in text:
    if ch in 'aeiouAEIOU':
        print(ch.upper())
    else:
        print(ch.lower())