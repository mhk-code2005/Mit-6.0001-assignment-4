# Problem Set 4A
# Name: <Mahir Kaya>
# Collaborators:
# Time Spent: x:xx`
#def letter_slider(string,specific_char):


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutation_list=[]
    third=[]
    def traveler(string, element):

        string=list(string)
        zero=0
        new_list=[]    
        list_result=[]
        while zero<=len(string):
            string.insert(zero, element)
            string2=string[:]
            string2=''.join(string2)
            list_result.append(string2)
            string.remove(element)
            zero+=1
            if zero>=len(string)+1:
                return list_result
                break
        for t in list_result:
            t=''.join(t)
            new_list.append(t)
        return(new_list)
    if len(sequence)==1:
        
        permutation_list.append(sequence)
        return((permutation_list))
    else:
        if len(sequence)>1:    
            k=sequence[0]
            sequence=list(sequence)
            sequence.remove(k)
            sequence=''.join(sequence)

        x=get_permutations(sequence)
        for t in x:
            w=traveler(t,k)
            
            
            third.append(w)
        for s in third:
            for p in s:
                permutation_list.append(p)
        for p in permutation_list:
            while permutation_list.count(p)>1:
                permutation_list.remove(p)
        
        return(permutation_list)

print(get_permutations('0000'))  
       
        
#            sequence=sequence.replace(sequence[zero], '')


#if __name__ == '__main__':
#
#   def tester_get_permutations():
#    ex1='abc'
#    print('input:', ex1)
#    expected_output=['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
#    print('expected output:',expected_output )
#    print('actual output:', get_permutations(ex1))
#    result1=all(elem in expected_output for elem in get_permutations(ex1))
#    
#    if result1:
#        print('success at ex1')
#    else:
#        print( 'failure at ex2')
#    ex2='cvv'
#    print('input:', ex2)
#    expected_output=['cvv', 'vcv', 'vvc']
#    print('expected output:',expected_output )
#    print('actual output:', get_permutations(ex1))
#    result2=all(elem in expected_output for elem in get_permutations(ex2))
#    
#    if result2:
#        print( 'Success at ex2')
#    else:
#        print( 'failure at ex2')
#    ex3='cvp'
#    print('input:', ex2)
#    expected_output=['cvp', 'vcp', 'vpc', 'cpv', 'pcv', 'pvc']
#    
#    print('expected output:',expected_output )
#    print('actual output:', get_permutations(ex3))
#    result3=all(elem in expected_output for elem in get_permutations(ex3))
#    
#    if result3:
#        print( 'Success at ex3')
#    else:
#        print( 'failure at ex3')
#    if result1 and result2 and result3:
#        return 'successfully implemented'
#print(tester_get_permutations()) 
#    
    
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', [ 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

