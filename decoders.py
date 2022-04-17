# Ceasar Cryptography decoder with option to adjust offset

def decoder(input, offset):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    decode = ""
    for letter in input:
        if letter in alphabet:
            new_letter = (alphabet.find(letter) + offset) % 26
            decode += alphabet[new_letter]
        else:
            decode += letter
    return decode

#-----------------------------------------------------------------------------------------------------------------------------------
#given a string, return the message translated into NATO phonetic alphabet

NATO = { 'A':'Alfa','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo',
       'F':'Foxtrot','G':'Golf','H':'Hotel','I':'India','J':'Juliett',
       'K':'Kilo','L':'Lima','M':'Mike','N':'November','O':'Oscar',
       'P':'Papa','Q':'Quebec','R':'Romeo','S':'Sierra','T':'Tango',
       'U':'Uniform','V':'Victor','W':'Whiskey','X':'Xray','Y':'Yankee',
       'Z':'Zulu'
       
      }
def to_nato(words):
    letter_list = [character for character in words if character != " "]
    
    def nato_decode(letter):
        return NATO[letter.upper()] if letter not in ",.!?" else letter
    
    
    nato_word_list = [nato_decode(item) for item in letter_list]
    
    return " ".join(nato_word_list)