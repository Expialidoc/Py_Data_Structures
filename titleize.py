def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    l_phrase = phrase.split(' ') # make a list of words
    return " ".join([word.capitalize() for word in l_phrase]) # join capitalized words
