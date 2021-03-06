#codewarproblem 17.04.22
#return the number of words in list that has letters with same index as its respective index in the alphabet
def solve(arr):
    alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
    
    def compare_index(a):
        count = 0
        letter_list = list(a.lower())
        smaller_list = min([len(alphabet_list),len(letter_list)])
        for index in range(smaller_list):
            if letter_list[index] == alphabet_list[index]:
                count += 1
        return count
    
    return [compare_index(word) for word in arr] if arr else None

#-------------------------------------------------------------------------
#find position of vowels in a word

def vowel_indices(word):
    vowels = "aeiouyAEIOUY" 
    return [index for index in range(1,(len(word)+1)) if word[index-1] in vowels]

#-----------------------------------------------------------------------------------------
# return True if every odd number in a list is greater than all the even numbers

def is_odd_heavy(arr):
    odd_integer_list = [odd for odd in arr if odd % 2 != 0]
    even_integer_list = [even for even in arr if even % 2 ==0]
    
    if odd_integer_list:
        for odd_num in odd_integer_list:
            for even_num in even_integer_list:
                if odd_num < even_num:
                    return False
    else:
        return False
    
    return True
#--------------------------------------------------------------------------------------------
#function that informs if character in a string appears more than once in a string. Returns a encoded message consist if "(" == appears once, ")" == appears twice
def duplicate_encode(word):
    lower = word.lower()
    new_set = set(lower)
    dubble = [i for i in new_set if lower.count(i) >1]
    encoder = ""
    for char in lower:
        if char in dubble:
            encoder += ")"
        else:
            encoder += "("
    return encoder
#---------------------------------------------------------------------------------------------
#function checks if given value is an valid IP address
def is_valid_IP(strng):
    if strng.count(".") ==3:
        num_list = strng.split(".")
        for num in num_list:
            if num.isnumeric():
                if int(num) > 255:
                    return False
                elif len(num) >1 and num[0] == "0":
                    return False
            else:
                return False
    else:
        return False
    return True

