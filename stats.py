def get_book_text (filepath):
        with open(filepath) as filex:
            return filex.read()
def get_num_words(book):
     return len(get_book_text(book).split())
def get_num_characters(book):
      liste = {}
      text = get_book_text(book).lower()
      symbols = []
      for symbol in text:
            symbols.append(symbol)
      for symbol in symbols:
            liste[symbol] = liste.get(symbol, 0) + 1
      return (liste)                   
def chars_dict_to_sorted_list(chars_dict):
    # Convert dictionary to list of dictionaries
    chars_list = []
    for char, count in chars_dict.items():
        chars_list.append({"char": char, "count": count})
    
    # Sort by count
    def sort_by_count(item):
        return item["count"]
    
    chars_list.sort(reverse=True, key=sort_by_count)
    return chars_list


      