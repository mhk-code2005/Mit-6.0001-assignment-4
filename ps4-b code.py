# Problem Set 4B
# Name: <Mahir Kaya>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while t finish.
    '''
#    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
#    print("  ", len(wordlist), "words loaded.")
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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("C:\\Users\\mahir\\OneDrive\\Desktop\\progrmming\MIT CODING\\\ps4\\story.txt", "r")
    story = str(f.read())
    f.close()
    return story
#print(get_story_string())
### END HELPER CODE ###

WORDLIST_FILENAME = 'C:\\Users\\mahir\\OneDrive\\Desktop\\progrmming\MIT CODING\\\ps4\\words.txt'
word_list=(load_words(WORDLIST_FILENAME))
class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
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
        return(self.text)
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        word_list2=word_list[:]
        return word_list2
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
                
        '''
        dict1={}
        dict_final={}
        dict_final2={}
        p=1
        
        for s in string.ascii_letters:
            
            if p==27:
                p=1
            dict1.update({s:p})
            p+=1
        for t in dict1:
            p=dict1[t]+shift
                
            while p>26:
                p-=26
            dict_final.update({t:p})
        for s in string.ascii_letters:
            p=dict_final[s]
            if s in string.ascii_lowercase:
                r=string.ascii_letters[p-1]
                dict_final2.update({s:r})
            if s in string.ascii_uppercase:
                r=string.ascii_letters[p+25]
                dict_final2.update({s:r})
        return dict_final2
                
                                


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        k=''
        f=self.build_shift_dict(shift)
        for s in (self.text):
            if s in string.ascii_letters:
                
                    k+=f[s]
            
            else:
                k+=s
        return k
a=Message('Hello World')
#
#print(a.apply_shift(3))
#print(a.build_shift_dict(3))
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        Message.__init__(self,text)
        self.shift=shift
        
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        self.text=text
        self.shift=shift
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return  self.shift
    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        r=self.build_shift_dict(self.shift)
        r2=r.copy()
        return r2
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''

        return self.apply_shift(self.shift)
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift=shift
b = PlaintextMessage('ab', 0)
#print(b.build_shift_dict(b.get_shift()))
#print(b.get_message_text_encrypted())
#print(b.get_message_text_encrypted())
#(b.change_shift(1))
#print(b.get_shift())
#print(b.get_message_text_encrypted())


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.valid_words=load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        ''' 
        shift=0
        right_words=[]
        ps=[]
        ps2=[]
        ps3=[]
        final=[]
        
        for shift in range  (26):
            dicti={}
            p=''
            f=self.build_shift_dict(shift)
#            print(f)
            for w in f:
                dicti.update({f[w]:w})
            for t in self.text:
                if t in string.ascii_letters:
                    p+=dicti[t]
                
                else:
                    p+=t
            ps.append((p))
            final.append(shift)
#            ps2.update({p:shift})
#            print(dicti)

            shift+=1
#        print(ps)
        for elem in ps:
            elem=elem.split()
            ps2.append(elem)
#        print(ps2)
        for k in ps2:
            s=0

            for p in k:
                  if is_word(word_list, p)==True:
                       s+=1
                  else:
                     s=s
            ps3.append(s)
        a=max(ps3)    
        index=ps3.index(a)
        text=ps[index]
        shift=final[index]
        return (shift, text)
#       print(dicti, 'shift', shift)
#       def truth_getter(string):
#                    truth=[]
#                    if ' ' or '' or '.' not in string:
#                        if is_word(word_list, string)==True:
#                            truth.append('TRUE')
#                    if ' ' or '' or '.' in string:
#                        string=string.split(' ')
#                        for t in string:
#                            if t=='' or t==' ' or t== '.':
#                                truth.append('TRUE')
#                            else:
#                                if is_word(word_list, t)==True:
#                                    truth.append('TRUE')
#                                else:
#                                    truth.append('FALSE')
#                            
#                      
#                    if truth.count('FALSE')>=1:
#                        return False
#                    else:
#                        return True
#        for elem in ps:
#            if truth_getter(elem)==True:
#                right_words.append(elem)
#            else:
#                return "Can not decyrpt"
#        for k in right_words:
#            shift=ps2[k]
#            final.append(('shift:',shift,'text:', k  ))
#            
#        return((final))
#a=CiphertextMessage('OCjkt')
#print(a.decrypt_message())


if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

#    #TODO: best shift value and unencrypted story 
    def tester():
            ex1=PlaintextMessage('Hello World', 3)
            EXPECTED_OUTPUT="Khoor Zruog"
            Actual_output=ex1.get_message_text_encrypted()
            if Actual_output==EXPECTED_OUTPUT:
                x='Success'
                print(x)
            else:
                x='Fail'
                print('First test:',x)
            ex2=PlaintextMessage('MAhir K', 2)
            Actual_output2=ex2.get_message_text_encrypted()
            Expected_output2=('OCjkt M')
            if Actual_output2==Expected_output2:
                y='Success'
            else:
                y='Fail'
            print('Second Test:',y)
            ex3=CiphertextMessage("Khoor Zruog")
            Actual_output3=ex3.decrypt_message()
            Expected_output3=(3,'Hello World')
            if Actual_output3==Expected_output3:
                z='Success'
            else:
                z='Fail'
            print('Third test:',z)
            ex4=CiphertextMessage('JqtuG')
            Actual_output4=(ex4.decrypt_message())
            Expected_output4=(2,'HorsE')
            if Actual_output4==Expected_output4:
                r='Success'
            else:
                r='Fail'
            print('Fourth test:', r)
            if r=='Success':
                if z=='Success':
                    if y=='Success':
            
                        if x=='Success':
                            print('Classes implemented correctly')
    tester()    
    #print(('Xoqy'))
#story=CiphertextMessage('Khoor Zruog')
#print(story)
#print(story.decrypt_message())

  #################story###############
  #(14, 'Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed aclass. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.')
  