#https://leetcode.com/problems/length-of-last-word/description/


def lengthOfLastWord( s: str) -> int:
    words=s.split()
    return len(words[-1])


sin=" Hi Dear "
print(lengthOfLastWord(sin))
        