print("일\t월\t화\t수\t목\t금\t토")

for i in range(1, 32):
    if i == 1:
        print("\t", i, end="\t")
    elif i % 7 == 0:
        print("\n", i, end="\t")
    else:
        print(i, end="\t")

