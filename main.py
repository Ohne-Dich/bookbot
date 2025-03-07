def get_book_text (filepath):
        with open(filepath) as filex:
            return filex.read()            
def main():
      print(get_book_text ("./books/frankenstein.txt"))
main()
