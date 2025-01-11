letters = "abcdefghijklmnopqrstuvwxyz"

def get_character_count(input_text):
    character_dict = {}
    for char in input_text:
        char = char.lower()
        if char in character_dict.keys():
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    # print(character_dict)
    character_dict = dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))
    return character_dict

def main():
    file_contents = []
    count = 0
    # chars = 0
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    for word in words:
        count += 1
    character_dict = get_character_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document\n")
    for element in character_dict.keys():
        if element in letters:
            print(f"The '{element}' character was found {character_dict[element]} times")
    print("--- End report ---")

main()