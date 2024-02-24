def reverse_string(string):
    if len(string)<=1:
        return string
    return reverse_string(string[1:])+string[0]

def main():
    s1='abcdef'
    s2=''
    s3='aba'
    s4='rabbit'
    s5='a'
    print("s1 reversed: ",reverse_string(s1))
    print("s2 reversed: ",reverse_string(s2))
    print("s3 reversed: ",reverse_string(s3))
    print("s4 reversed: ",reverse_string(s4))
    print("s5 reversed: ",reverse_string(s5))
main()