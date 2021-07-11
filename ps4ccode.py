# Problem Set 4C
# Name: <Mahir Kaya>
# Collaborators:
# Time Spent: x:xx

import string
from ps4acode import get_permutations

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    

    inFile = open(file_name, 'r')

    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])

    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list
def get_keys(dictionary):
    list1 =[]
    for t in dictionary.keys():
        list1.append(t)
    return list1
def get_values(dictionary):
    list1=[]
    for s in dictionary.values():
        list1.append(s)
    return list1

WORDLIST_FILENAME = 'C:\\Users\\mahir\\OneDrive\\Desktop\\progrmming\MIT CODING\\\ps4\\words.txt'

VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.text=text
        self.valid_words=load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.text
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        alphabet={}
        
        for s in string.ascii_letters:
            alphabet.update({s:s})
            
        for k in alphabet:
            if k in VOWELS_LOWER:
                
                    index=VOWELS_LOWER.find(k)
                    alphabet[k]=vowels_permutation[index]
            if k in VOWELS_UPPER:
                wk=k.lower()
                p=alphabet[wk]
                p=p.upper()
                
                alphabet[k]=p
        return alphabet
            
            
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        p=''
        for s in self.text:
            if s in string.ascii_letters:
                p+=transpose_dict[s]
            else:
                p+=s
        return p
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        SubMessage.__init__(self,text)
        self.valid_words=load_words(WORDLIST_FILENAME)
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        f=[]
        r=get_permutations('aeiou')
        final_turn=[]
        possible_words=[]
        empty_list=[]

        for k in r:
            transpose_dict=self.build_transpose_dict(k)
                    
            list_of_orig=get_keys(transpose_dict)
            list_of_later=get_values(transpose_dict)
            p=''
            for t in self.text:
    
                    if t in VOWELS_LOWER:
                        index=list_of_orig.index(t)
                        p+=list_of_later[index]

                        
                    if t in VOWELS_UPPER:
                        t=t.lower()
                        index=list_of_orig.index(t)
                        x=((list_of_later[index]).upper())
                        p+=x
                    if t not in VOWELS_LOWER  and t not in VOWELS_UPPER:
                        p+=t
                    
            f.append(p)
        
        if ' ' in self.text:
            
            for p in f:
                    k=0
                    zero=-1
                    s=p.split()
                    for asd in s:
                        
                        if is_word(self.valid_words, asd)==True:
                            k+=1
                        else:
                            k=k
                        zero+=1
    
                    empty_list.append(k)
                    
            maximum=max(empty_list)
            
            possible_permutations=[]
            if empty_list.count(maximum)==1:
                index=empty_list.index(maximum)
                possible_words.append(f[index])



                for t in possible_words:
                    index=f.index(t)
                    
    
                    possible_permutations.append(r[index])
                    
                for t in possible_permutations:
                    index=possible_permutations.index(t)
                    k=possible_words[index]
                    final_turn.append([t +' '+'permutation for'+' '+ k])
    
                
                return final_turn
            if empty_list.count(maximum)>1:
                index_list=[]
                zero3=0
                for t in empty_list:
                    if t==maximum:
                        index_list.append(zero3)
                    zero3+=1
                for k in index_list:
                    final_turn.append((r[k]+' '+'for'+' '+f[k]))
                return final_turn
                

        
        if ' ' not in self.text:
            for p in f: 
                if is_word(self.valid_words, p)==True:
                        possible_words.append(p)
            possible_permutations=[]
            t=0
            index_list=[]
            for s in f:
                if s in possible_words:
                    index_list.append(t)

                t+=1

            for k in index_list:
                final_turn.append([r[k] +' '+'permutation for word'+' '+ f[k]+' '+'->'+' '+ 'encrypted message:'+ ' '+ self.text])

            return final_turn

if __name__ == '__main__':
#
#    # Example test case
#    message = SubMessage("Hello World!")
#    permutation = "eaiuo"
#    enc_dict = message.build_transpose_dict(permutation)
#    print("Original message:", message.get_message_text(), "Permutation:", permutation)
#    print("Expected encryption:", "Hallu Wurld!")
#    print("Actual encryption:", message.apply_transpose(enc_dict))
#    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
#    print("Decrypted message:", enc_message.decrypt_message())
#     
#    TODO: WRITE YOUR TEST CASES HERE
    def tester_submessage():
        ex1=SubMessage('final')
        actual_outpur_1=ex1.apply_transpose(ex1.build_transpose_dict('eaoui'))
        expected_output_1='fonel'
        if actual_outpur_1==expected_output_1:
            x='Success'
        else:
            x='Fail'
        print('first test:', x)
        ex2=SubMessage('final')
        actual_outpur_2=ex2.get_message_text()
        expected_output_2='final'
        if actual_outpur_2==expected_output_2:
            y='Success'
        else:
            y='Fail'
        print('second test:', y)
        ex3=EncryptedSubMessage('Oist us thit wiy')
        Expected_output_3='ouaei for East is that way'
        actual_outpur_3=ex3.decrypt_message()
        if Expected_output_3 in actual_outpur_3:
            Z='Success'
        else:
            Z='Fail'
        print('Third test:', Z)
        ex4=EncryptedSubMessage('saith')
        expected_output_4=['oeuai permutation for word south -> encrypted message: saith']
        actual_output_4=ex4.decrypt_message()        
        if    expected_output_4 in actual_output_4 :
            f='Success'
        else:
            f='Fail'
        print('Fourth test', f)
        if x=='Success' and y=='Success' and Z=='Success' and f=='Success':
            return (str('CLASSESS IMPLEMENTED SUCCESSFULLY'))
#    print(tester_submessage())
