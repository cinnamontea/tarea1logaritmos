from collections import defaultdict


def boyer_moore_horspool(pattern, text):
    m = len(pattern)
    n = len(text)

    if m > n:
        return -1

    skip = defaultdict(lambda: m)
    found_indexes = []

    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1

    k = m - 1

    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            found_indexes.append(i + 1)

        k += skip[ord(text[k])]

    return found_indexes

patron = input("patron\n")
texto = open('test.txt')
result = boyer_moore_horspool(patron, texto.read())
print(result)