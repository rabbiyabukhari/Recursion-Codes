def is_palindrome(string):
    if len(string)==0 or len(string)==1:
        return True
    if string[0]!=string[-1]:
        return False
    return is_palindrome(string[1:-1])

def main():
    s='abcdeedcba'
    s1='abcdbba'#not a palindrome
    s2='abcdcba'
    s3=''
    s4='aakd'#not a palindrome
    s5='aaa'
    print(is_palindrome(s))#True
    print(is_palindrome(s1))#False
    print(is_palindrome(s2))#True
    print(is_palindrome(s3))#True
    print(is_palindrome(s4))#False
    print(is_palindrome(s5))#True
main()