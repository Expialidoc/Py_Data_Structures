def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    l_phrase = phrase.lower()
    v_count = {}.fromkeys('aeiou', 0)

    for char in l_phrase:
        if char in 'aeiou':
            v_count[char] += 1

    return {k:v for k, v in v_count.items() if v !=0}

     

