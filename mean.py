#from numpy.testing import assert_allclose
#assert_allclose(obs, exp, atol=err)
#Comment for travis!
def mean(num_list):
    #assert type(num_list) == list
    #assert isinstance(num_list, list)
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError:
        #msg = "Silly, your list is empty."
        #raise ZeroDivisionError(detail.__str__() + "\n" + msg)
        return 0
    except TypeError as detail:
        msg = "Not a list you dork."
        raise TypeError(detail.__str__() + "\n" + msg)
        
    #if(len(num_list) ==0):
    #    raise Exception("You suck, why would you give me an empty list.")
    
