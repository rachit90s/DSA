#https://leetcode.com/problems/two-sum/description/
def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    reverse=0
    temp=x

    while temp>0:
        reverse = reverse * 10 + (temp%10)
        temp//=10

    return x==reverse

x=121
print(isPalindrome(x))    
