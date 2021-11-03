def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    l = '('
    r = ')'
    l_count = parens.count(l)
    r_count = parens.count(r)
    if l_count == r_count:
        if parens[0] == l and parens[-1] == r:
            return True
        else:
            return False
    else:
        return False

