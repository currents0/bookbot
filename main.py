def countWords(book):
    words = book.split()
    return len(words)

def countLetters(book):
    letters = {}
    for char in book:
        char = char.lower()
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def dictlist(dictionary):
    new = []
    for dict in dictionary:
        temp = {}
        temp["letter"] = dict
        temp["num"] = dictionary[dict]
        new.append(temp)
    return new

def report(book, words, letters):
    lettersLst = dictlist(letters)
    lettersLst.sort(reverse=True, key=sort_on)
    print(f"Report for {book}")
    print(f"Total wordcount: {words}\n")
    for i in range(0, len(lettersLst)):
        letter = lettersLst[i]["letter"]
        if letter.isalpha():
            num = lettersLst[i]["num"]
            print(f"'{letter}' has appeared {num} time/s")
    print("\nEnd of report")

def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read()
        count1 = countWords(file_contents)
        count2 = countLetters(file_contents)
        report(file, count1, count2)

main()