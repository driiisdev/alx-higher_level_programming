#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        a = len(i)
        for j in range(a):
            if j != a - 1:
                print("{:d} ".format(i[j]), end="")
            else:
                print("{:d}".format(i[j]), end="")
        print("")
