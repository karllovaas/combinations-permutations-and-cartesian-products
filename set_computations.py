# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 22:58:25 2022

@author: lovaa
"""

def grow(X,add):
    '''

    Parameters
    ----------
    X : could be an empty list, a list with integers, or list within a list. 
        (each of these inputs is handled differently by a branch)
    add : an integer that representing the cardnality of a set or outcomes in
          an experiment 

    Returns:
        grow([],3) ---> [0,1,2]
        grow([0,1,2],2) ---> [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]] 
        grow([[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]],2)
        
        -->  [[0, 0, 0],[0, 0, 1],[0, 1, 0],
             [0, 1, 1],[1, 0, 0],[1, 0, 1],
             [1, 1, 0],[1, 1, 1],[2, 0, 0],
             [2, 0, 1],[2, 1, 0],[2, 1, 1]]              
    -------
    '''
    output = []
    if len(X) == 0:
        X = [i for i in range(add)]
    elif type(X[0]) == int:
        for i in range(len(X)):
            for j in range(add):
                output.append([i,j])
        return output
    else:
        for i in X:
            for j in range(add):
                output.append(i + [j])
        return output 
    return X 


def cartesian_product(X):
    '''

    Parameters
    ----------
    X : list of integers, each integer represents the cardnality of a set. For example, the sets
        A = [1,2], B = ['red','yellow'], C = ['space','time','place'] can be abstracted so that 
        in the resutling cartesian product set, each element of an input set is represented 
        by an integer corrosponding to it's index in the input set ([0,0,0] == [1,'red','space'']).
    
        A X B X C is represented by inputting cartesian_product([|A|,|B|,|C|]) =  cartesian_product([2,2,3])

    Returns : cartesian_product([2,2,2])--> [[0, 0, 0],
                                           [0, 0, 1],
                                           [0, 1, 0],
                                           [0, 1, 1],
                                           [1, 0, 0],
                                           [1, 0, 1],
                                           [1, 1, 0],
                                           [1, 1, 1]]
    -------
    
    '''
    output = []
    for i in X:
        output = grow(output,i)
    return output 

def permuter2(n,k):
    '''

    Parameters
    ----------
    n : n in P(n,k)
    k : k in P(n,k)
    Returns: permutations of length k sampled from a set of length n. 
    
    permuter(4,2)  --> [[0, 1],[0, 2],
                        [0, 3],[1, 0],
                        [1, 2],[1, 3],
                        [2, 0],[2, 1],
                        [2, 3],[3, 0],
                        [3, 1],[3, 2]]
    -------
    logic is as follows
    if |A| = n then permuations of size k (k <= n) exist in the set 
    {x_1,x_2,..,x_k | x_1,x_2,..,x_k in A}. After removing 
    list's with elements that appear more than once in the list, the remaining 
    elements are the permutations. 

    '''
    if k > n:
        return print("Error k must less than n")
    else:
        L1 = [n]*k
        L2 = cartesian_product(L1)
        L3 = without_replacement(L2)
    return L3 

def without_replacement(X):
    '''
    Parameters
    ----------
    X : list of list 
    Returns : removes list's with elements that appear more than once in the list.
              without_replacement([[0,0],[1,2]]) --> [[1,2]]
    -------
    
    '''
    iter_count = 0
    while iter_count < len(X):
        for j in range(len(X[iter_count])):
            s = 'n'
            if X[iter_count].count(X[iter_count][j]) > 1:
                X.remove(X[iter_count])
                s = 'yes'
                break
        if s == 'yes':
            iter_count = iter_count
        else:
            iter_count = iter_count + 1 
    return X


def combiner(n,k):
    '''
    Parameters
    ----------
    n : n in n choose k
    k : k in n choose k 

    Returns: A list of all possible combinations of length k with sampled from a set
    of length n. 
    
    combiner(4,2) --> [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    
    converts elements in permutations(n,k) into set objects, and removes equivalent sets until
    every set is unique. the remaining sets represent n choose k combinations. 
    
    (set([1,2,3]) == set([3,2,1]) 
    -------
    '''
    X = permuter2(n,k)
    T = tuple(X)
    for indx,obj in enumerate(X):
        X[indx] = set(obj)
    T = tuple(X)
    for i in T:
        while X.count(i) > 1: 
            X.remove(i)
    for indx, obj in enumerate(X):
        X[indx] = list(obj)
    X.sort()
    return X

def real_combination(L,k):
    '''

    Parameters
    ----------
    L : list
    k : sample size (k <= |L|)
    
    Returns: real_combination(['g','b','d'],2) --> [['g', 'b'], ['g', 'd'], ['b', 'd']]
    -------
    '''
    n = len(L)
    L3 = combiner(n, k)
    for i in range(len(L3)):
        for j in range(len(L3[i])):
            L3[i][j] = L[L3[i][j]]
    return L3

def real_cartesian(L):
    '''
    Parameters
    ----------
    L : list of list as in L = [[L_1],[L_2],...[L_n]] (|L|>1)

    Returns L_1 x L_2 x ... x L_n 
    -------
    '''
    simplified = []
    for i in L:
        simplified.append(len(i))
    L2 = simplified
    L3 = cartesian_product(L2)  
    dict1 = {i:L[i] for i in range(len(L))}
    for i in range(len(L3)):
        for j in range(len(L3[i])):
            L3[i][j] = dict1[j][L3[i][j]]
    return L3   
