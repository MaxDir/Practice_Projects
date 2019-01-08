def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

failname = input("Введите мия файла: ")
with open(failname) as f:
    text = f.read()
print(count_char(text, "r"))