
# Matthew Vue
# This function gets all the substrings of the given input string

def all_substrings(s, n, idx,end_idx, res):

    '''
    s: input string
    n: length of input string
    idx: integer. set to 0. signals when at the end of the curent input string.
    end_idx: integer. set to 0. signals when done iterating through original input string.
    res: array to append the substrings to
    '''

    if s[:idx] not in res:
        res.append(s[:idx])

    # base case
    # we're at the end of the original input string
    if end_idx == n:
        return
    else:
        # not at the end of the string
        if idx < len(s):
            all_substrings(s,n,idx+1,end_idx,res)
        # at the end of the string
        # increment end_idx by 1, remove the first character from the string
        else:
            all_substrings(s[1:],n,0,end_idx+1,res)



s = 'mystring'

# to store all substrings
res = []

all_substrings(s, len(s), 0,0, res)

res
