def ok(nr):
    duplicates = False
    for i in range(5):
        if nr[i] > nr[i+1]:
            return False
        duplicates = duplicates or (nr[i] == nr[i+1])

    return duplicates


def main():
    count = 0
    for i in range(206938, 679128):
        if ok(str(i)):
            count += 1
    return count


print(main())

