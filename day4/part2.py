def ok(nr):
    duplicates = False
    cg = nr[0]
    cc = 1
    for i in range(1, 6):
        if nr[i-1] > nr[i]:
            return False
        if nr[i] == cg:
            cc += 1
        elif cc == 2:
            duplicates = True
        else:
            cg = nr[i]
            cc = 1

    return duplicates or cc == 2


def main():
    count = 0
    for i in range(206938, 679128):
        if ok(str(i)):
            count += 1
    return count


print(ok('111122'))
print(main())

