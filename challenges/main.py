def has_all_vowels(word):
    required = {"a", "e", "i", "o", "u"}
    word = word.lower() #treat as case-sensitive - lowercase 
    # TODO: build a set of vowels actually found in `word`,
    # then check if it contains all of `required`
    check = set() #creates an empty set
    for char in word: #loops through each character in the word
        if char in required: #checks if any of the character in 'word' is in 'required'
            check.add(char) #adds vowel characters to new set 
    return check == required #compares if all vowel characters - 'required' are available in 'check'