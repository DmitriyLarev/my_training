def single_root_words(root_words, *other_words):
    same_words = []
    for i in other_words:
        if root_words.lower() in i.lower() or i.lower() in root_words.lower():
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)