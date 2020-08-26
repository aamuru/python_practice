class Solution:
    def longestPalindrome(self, s: str) -> str:
        largest_palindrome=""
        for i in range(len(s)):
            palidromeOdd=self.largestPalindromeAtIndex(s,i,i)
            palindromeEven=self.largestPalindromeAtIndex(s,i,i+1)
            
            larger_palindrome=palidromeOdd if len(palidromeOdd) > len(palindromeEven) else palindromeEven
            largest_palindrome=larger_palindrome if len(larger_palindrome) >= len(largest_palindrome) else largest_palindrome
        
        return largest_palindrome
    
    def largestPalindromeAtIndex(self,s,left,right):
        leftIndex=0
        rightIndex=0
        while left>=0 and right<len(s):
            if s[left]==s[right]:
                leftIndex=left
                rightIndex=right
            else:
                break
            left-=1
            right+=1
        return s[leftIndex:rightIndex+1]