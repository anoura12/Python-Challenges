import time
import pandas as pd
import numpy as np


def listGenerator(filename):
    """
    Return list of elements from the text document.
    
    Parameters:
        filename(str): Stores the name of text document.

    Returns:
        filevar(list): Stores the extracted list from filename.

    """
    filevar = []
    with open(filename) as f:
        filevar = f.read().split('\n')
    return(filevar)

def commonElements(subset_elem,all_elem):        
    """
    Find common elements from the two lists generated from listGenerator. 

    Display the number of common elements and time taken to search for them.

    Parameters:
        subset_elem(list): Contains the elements extracted from subset_elemets.txt.
        all_elem(list): Contains the elements extracted from all_elements.txt.

    """
    start = time.time()
    verified_elements = []

    for element in subset_elem:
        if element in all_elem:
            verified_elements.append(element)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))

def commonElements_numpy(subset_elem,all_elem):
    """
    Find common elements from the two lists using the numpy module. 

    Display the number of common elements and time taken to search for them.

    This executes faster than the commonElements function.

    Parameters:
        subset_elem(list): Contains the elements extracted from subset_elemets.txt.
        all_elem(list): Contains the elements extracted from all_elements.txt.
    
    """

    start = time.time()
    verified_elements = np.intersect1d(subset_elem,all_elem)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))

def commonElements_pydataStructure(subset_elem,all_elem):
    """
    Find the common elements from the two lists using sets.

    Display the number of common elements and time taken to search for them.

    This executes faster than both the commonElements and commonElements_numpy functions.

    Parameters:
        subset_elem(list): Contains the elements extracted from subset_elemets.txt.
        all_elem(list): Contains the elements extracted from all_elements.txt.

    """

    start = time.time()
    verified_elements = set(subset_elem) & set(all_elem)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))


subset_elements = listConverter('subset_elemets.txt')
all_elements = listConverter('all_elements.txt')

commonElements(subset_elements,all_elements)
commonElements_numpy(subset_elements,all_elements)
commonElements_pydataStructure(subset_elements,all_elements)
