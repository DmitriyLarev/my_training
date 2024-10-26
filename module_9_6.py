def all_variants(text):
    for j in range(len(text)):
        for k in range(len(text) - j):
            yield text[k:k+j+1]

a = all_variants("abc")
for i in a:
    print(i)

