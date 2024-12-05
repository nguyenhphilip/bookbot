def main():
    frank = open_text("books/frankenstein.txt")
    num_words = get_num_words(frank)
    characters = get_chars_dict(frank, alpha_only=False)
    alpha_chars = get_chars_dict(frank, alpha_only=True)
    sorted_chars = return_sorted_dict(alpha_chars)
    print("")
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    for letter in sorted_chars:
        print(f"The '{letter[0]}' character was found {letter[1]} times.")
    print("")
    print("--- End report ---")

def open_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def return_sorted_dict(dict):
    list_of_items = list(dict.items())
    list_of_items.sort(key = lambda x: x[1], reverse=True)
    return list_of_items

def get_chars_dict(text, alpha_only=False):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    if alpha_only==True:
        alpha_dict = {}
        for k in chars:
            if k.isalpha():
                alpha_dict[k] = chars[k]
        return alpha_dict
    return 
    
main()