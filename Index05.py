def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=0
    if s[0] in "0123456789":
        a+=1
    if s[1] in "0123456789":
        a+=1
    if s[2] in "0123456789":
        a+=1
    if s[3] in "0123456789":
        a+=1
    if s[4] in "0123456789":
        a+=1
    return a