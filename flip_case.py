def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # for char in phrase:
        # if char == to_swap.upper() or char == to_swap.lower():
            # char.swapcase()
        # else:
            # char
    s_phrase = [char.swapcase() if char == to_swap.upper() or char == to_swap.lower() else char for char in phrase]
    
    return "".join(s_phrase)

    

