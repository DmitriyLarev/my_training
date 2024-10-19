class WordsFinder:
    def __init__(self, *files):
        self.files = files
        self.file_names = list(self.files)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file in self.files:
            with open(file, encoding="utf-8") as one_file:
                list_words = []
                for line in one_file:
                    for i in punctuation:
                        line = line.replace(i, "").lower()
                    list_words += line.split()
                    all_words[one_file.name] = list_words
        return all_words

    def find(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            if word in words:
                dict_[name] = words.index(word) + 1
        return dict_

    def count(self, word):
        dict_ = {}
        counter = 0
        for name, words in self.get_all_words().items():
            for i in words:
                if word == i:
                    counter += 1
                    dict_[name] = counter
        return dict_

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))