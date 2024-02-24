def sum_of_array(arr):
    if len(arr)==0:
        return 0
    return arr[0]+sum_of_array(arr[1:])

def main():
    arr=[9,10,0]
    print(sum_of_array(arr))
main()