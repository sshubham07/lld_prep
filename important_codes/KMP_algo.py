def build_lps(pattern):
    """
    LPS = Longest Prefix Suffix

    lps[i] stores:
    longest proper prefix which is also suffix
    for pattern[0:i+1]
    """

    m = len(pattern)
    lps = [0] * m

    length = 0   # length of previous longest prefix suffix
    i = 1

    while i < m:

        # characters match
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        else:
            # fallback using previous lps
            if length != 0:
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):

    n = len(text)
    m = len(pattern)

    lps = build_lps(pattern)

    i = 0   # pointer for text
    j = 0   # pointer for pattern

    while i < n:

        # match
        if text[i] == pattern[j]:
            i += 1
            j += 1

        # full pattern found
        if j == m:
            print("Pattern found at index:", i - j)

            # continue searching
            j = lps[j - 1]

        # mismatch after some matches
        elif i < n and text[i] != pattern[j]:

            # move pattern pointer using lps
            if j != 0:
                j = lps[j - 1]

            else:
                i += 1


# Example
text = "ababcabcabababd"
pattern = "ababd"

kmp_search(text, pattern)