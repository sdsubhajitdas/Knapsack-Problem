import os


def knapSack(w, wt, val, n):
    '''
    Returns the maximum value that can be put in a knapsack of
    capacity w
    '''

    if n == 0 or w == 0:
        '''Base Case'''
        return 0

    if (wt[n-1] > w):
        '''
        If weight of the nth item is more than 
        Knapsack of capacity w, then this item 
        cannot be included in the optimal solution.
        '''
        return knapSack(w, wt, val, n-1)

    else:
        '''
        return the maximum of two cases:
        - N-th item included
        - not included
        '''
        return max(val[n-1] + knapSack(w-wt[n-1], wt, val, n-1),
                   knapSack(w, wt, val, n-1))


def main():
    '''Entry point to the program'''

    val = list(map(int, input(
        "Enter the values for Knapsack Problem, each seperated with a space\n").split(' ')))

    wt = list(map(int, input(
        f"\nEnter the weights for {val} values, each seperated with a space\n").split(' ')))

    w = int(input("\nEnter the total weight of the Knapsack Bag :\t"))

    n = len(val)

    print(
        f"\n\nTotal value which the Knapsack Bag of weight {w} can hold is:\t{knapSack(w, wt, val, n)}")


if __name__ == '__main__':
    '''Driver code to run the whole program.'''
    os.system('clear')
    main()
