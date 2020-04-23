alist = [1, 3, 5, 7, 9, 11, 13, 15]
blist = []
for i in alist:
    if i <= 10:
        j = i - 1
        blist.append(j)
    else:
        break
print(blist)