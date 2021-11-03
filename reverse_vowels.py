def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    begin  = -1
    indices = []
    
    for v in s:
        begin += 1
        if v in 'aeiouAEIOU':
            indices.append(s.index(v, begin))
    
    if len(indices) % 2 != 0:
        mid_ind = int((len(indices) - 1)/2)
    else:
        mid_ind = int(len(indices)/2)
    
    lst = list(s)

    for i in range(mid_ind):
        m = indices[i];
        temp_vowel = lst[m]
        indices[i] = indices[len(indices)-1-i]
        lst[m] = lst[indices[i]]
        lst[indices[i]] = temp_vowel
    
    return "".join(lst)


    

            
    
