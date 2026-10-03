def shift(ip, sh):
    res = ''
    for ch in ip:
        if ch.isalpha():
            if ch.isupper():
                res += chr((ord(ch) - ord('A') + sh) % 26 + ord('A'))
            else:
                res += chr((ord(ch) - ord('a') + sh) % 26 + ord('a'))
        else:
            res += ch
    return res
def vigenere(ip, key):
    res = ''
    j = 0
    for ch in ip:
        if ch.isalpha():
            sh = ord(key[j % len(key)].upper()) - ord('A')
            if ch.isupper():
                res += chr((ord(ch) - ord('A') + sh) % 26 + ord('A'))
            else:
                res += chr((ord(ch) - ord('a') + sh) % 26 + ord('a'))
            j += 1
        else:
            res += ch
    return res
print("1. Caesar Shift\n2. Vigenere\n3. Substitution")
op = int(input("Enter your choice: "))
if op == 1:
    print("Output:", shift(input('Enter the input: '), int(input('Enter the shift: '))))
elif op == 2:
    print("Output:", vigenere(input('Enter the input: '), input('Enter the key: ')))
elif op == 3:
    print("Output:", shift(input('Enter the input: '), 3))
else:
    print("Invalid choice")
