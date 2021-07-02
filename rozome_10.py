text = input("enter a string: ")
Segmenter = text.split()
for i in Segmenter:
    for i_1 in i:
        d = i_1[0].upper()
        print(d, end="")
        break

