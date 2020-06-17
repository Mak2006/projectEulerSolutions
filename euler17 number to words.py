from num2words import num2words

if __name__ == '__main__':
    seq = []
    length = 0
    for i in range(1, 1001):
        w = num2words(i)
        w = w.replace(" ", "") # omit space and -
        w = w.replace("-", "")
        print(w)
        length = length + len(w)

    print("ans "+ str(length))