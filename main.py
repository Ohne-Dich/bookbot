from stats import get_num_words
from stats import get_num_characters
from stats import chars_dict_to_sorted_list
import sys
book = (sys.argv[1])

def main():
      print (f"""============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {get_num_words(book)} total words
--------- Character Count -------""")
      char_counts = get_num_characters(book)
      sorted_chars = chars_dict_to_sorted_list(char_counts)

      for all in sorted_chars:
            char = all["char"]
            count = all["count"]

            if char.isalpha():
                 print(f"{char}: {count}")
      print ("============= END ===============")

main()
