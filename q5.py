string = input("Digite uma string: ")
def inverte(s):
    novaString = ""
    i = len(s) - 1
    while i >= 0:
        novaString = novaString + s[i]
        i = i - 1
    return novaString

print(inverte(string))