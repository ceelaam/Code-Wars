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