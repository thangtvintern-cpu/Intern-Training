def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""

    start = 0
    max_len = 1

    def expand(left: int, right: int):
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            curr_len = right - left + 1
            if curr_len > max_len:
                start = left
                max_len = curr_len
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)       
        expand(i, i + 1)   

    return s[start:start + max_len]


def main():
    s = input("Enter string: ").strip()
    result = longest_palindromic_substring(s)
    print("Longest Palindromic Substring:", result)


if __name__ == "__main__":
    main()

