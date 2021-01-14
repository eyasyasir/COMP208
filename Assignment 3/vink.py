# Author: Eyas Hassan
# Assignment 3, Question 2

import matplotlib.pyplot as plt

# Return a list of terms of the Vink sequence for the given n and k values
# until a term of 1 is reached. If a term of 1 is not reached after j terms,
# then return the empty list.
def vink_sequence(n, k=1, j=1000):
    terms = [n]
    for i in range(j):
        # check if last term is 1
        if terms[-1] == 1:
            return terms
        
        # calculate next term in sequence
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + k
        terms.append(int(n))
    
    return [] # no term of 1 was found

# Save a graph showing showing the number of terms it takes for the Vink sequence to converge to 1
# for values of n in the range [1, max n] (inclusive)
def graph_time_to_convergence(max_n):
    plt.figure()
    
    # list comprehension to create list of all terms in range [1, max_n] representing x values of scatter plot.
    # list comprehension to create list (y_values) of number of terms it takes for vink sequence to converge to 1, with n being
    # each element in list x_values
    x_values = [i + 1 for i in range(max_n)]
    y_values = [len(vink_sequence(i)) for i in x_values]
    
    plt.plot(x_values, y_values, "c.", markersize = 2) # plotting scatter plot with cyan, point stlye, size 2 markers
    
    # adding graph title and axes titles
    plt.title("Number of terms until convergence to 1 for n in [1, {}]".format(max_n))
    plt.xlabel("n")
    plt.ylabel("Number of terms until convergence to 1")
    
    #plt.show()
    plt.savefig("convergence_maxn={}.png".format(max_n)) # saving graph with string formated to take variable max_n
    
    return plt.axes()

# Save a bar chart showing the number of values of n (in the range [0, 10000]) that converge to 1 (within 1000 terms)
# for odd values of k in the range [1, max k]
def graph_convergence_of_ks(max_k):
    plt.figure()

    # list comprehension to create list of n terms in range [1, 10000]
    n = [i + 1 for i in range(10000)]
    
    # list comprehesnion to create list of odd k terms in range [1, max_k], adjusted to deal with even and odd max_k
    # user inputs. list represents x values of graph.
    if max_k % 2 == 0:
        x_values = [i for i in range(1, max_k, 2)]
    else:
        x_values = [i for i in range(1, max_k + 1, 2)]
        
    y_values = [] # create empty list of y values
    
    # counting number of vink sequences with n in range [1, 10000] that converge to 1 and populating list y_values
    for k in x_values:
        count = 0
        for term in n:
            if len(vink_sequence(term, k)) > 0:
                count += 1
        y_values.append(int(count))

    plt.bar(x_values, y_values, width=0.6, color="cyan") # plotting bar graph with cyan 0.6 wide bars
    
    # adding graph title and axes titles
    plt.title("Convergence for values of k")
    plt.xlabel("k")
    plt.ylabel("Number of n that converged to 1")
    
    #plt.show()
    plt.savefig("convergence_maxk={}.png".format(max_k)) # saving graph with string formated to take variable max_k

    return plt.axes()

# Save line graph showing the values of the terms of the Vink sequence until a 1 is reached, for every power of
# 2 in the range [2, max n] (inclusive), with k=1 and j=1000.
def graph_nums_to_1(max_n):
    plt.figure()
    
    # populating list n with terms of powers of 2 in range [1, max_n]
    n = []
    for i in range(1, max_n + 1):
        if 2 ** i > max_n:
            break
        n.append(2 ** i)
    
    # creating nested list containing vink sequences for each element in n
    sequence = []
    for term in n:
        sequence_for_term = vink_sequence(term)
        sequence.append(sequence_for_term)
        
    # iterating through nested list of vink sequences to plot time evolution of each vink sequence after each step
    for i in range(len(sequence)):
        x_values = []
        y_values = []
        # here j corresponds to the step number and it is also used to access the elements in the nested vink sequence list
        for j in range(len(sequence[i])):
            x = j
            y = sequence[i][j]
            x_values.append(x)
            y_values.append(y)
        plt.plot(x_values, y_values, label="{}".format(n[i])) # plotting with each line having label of its n term
    
    # adding graph title, axes titles, and a legend
    plt.title("Convergence of n over time")
    plt.xlabel("Step number")
    plt.ylabel("Term")
    plt.legend()
    
    plt.show()
#     plt.savefig("numsto1_maxn={}.png".format(max_n)) # saving graph with string formated to take variable max_n
    
    return plt.axes()

# Sample code for testing (do not include this with your final submission)
# axes = graph_time_to_convergence(1000)
# axes = graph_convergence_of_ks(8)
axes = graph_nums_to_1(2**10)
