#Filepath
Filepath = "books/frankenstein.txt"

#Getting the text.
def get_book_text(Filepath):

 #Hopefully Opening and reading the code
 with open(Filepath, "r") as f:
     file_contents = f.read()
 # Dumb attempt in hopes that it would print... and returning the value
 return file_contents
 
#Word count
def word_count():
    text = get_book_text(Filepath)
    words = text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

#Main Function
def main():
     text = get_book_text(Filepath)
     print(text)



#main()
word_count()

