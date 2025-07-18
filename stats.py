def get_num_words(book):
    return len(book.split())

def counter(book):
    
    dict = {}
    
    for word in book:
        for letter in word:
                if letter.isalpha():
                    lower = letter.lower()
                    if lower not in dict:
                        dict[lower] = 1
                    else:
                        dict[lower] += 1
    return dict

def sorter(dictionary):
    combined_list = []

    for key in dictionary:
        combined_list.append({
            "char": key,
            "num": dictionary[key]
        })

    combined_list.sort(key=lambda x: x["num"], reverse=True)
    return combined_list

        
        