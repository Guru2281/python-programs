def count_vowels(str):
    count=0
    for alph in str:
        if alph.lower() in ['a','e','i','o','u']:
            count+=1
    return count

if __name__=="__main__":
    str=input("Enter string :")
    print(count_vowels(str))
