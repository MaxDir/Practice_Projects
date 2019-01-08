def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count
file = open("text.txt", "w")
file.close()
filename = "text.txt"
with open(filename) as f:
	text = f. read()