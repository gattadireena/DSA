def reverseString(s):
    #split the string into list
    words = s.split()
    #reverse the list of strings
    words.reverse()
    #joins the reversed words
    reversed_words = " ".join(words)
    return reversed_words

if __name__ == "__main__":
    s = "word blue"
    print(reverseString(s))