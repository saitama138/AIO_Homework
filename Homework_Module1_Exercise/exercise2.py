from math import *
def is_number(N) :
    try :
        float(N)
    except ValueError:
        return False
    return True

def sigmoid(N) :
    return 1 / (1 + e ** -N)

def reLu(N) :
    if N <= 0 :
        return 0
    else :
        return N

def eLu(N) :
    alpha = 0.01
    if N <= 0 :
        return alpha * ((e ** N) - 1)
    else :
        return N

def exercise2() :
    print("Input x = ")
    x = input()
    if(is_number(x) == False) :
        print("x must be a number")
    else :
        print("Input activation Function (sigmoid|relu|elu) : ")
        type = str(input())
        if(type != "sigmoid" and type != "relu" and type != "elu") :
            print(f'{type} is not supportted')
        else :
            if type == "sigmoid" :
                print(f'{type} : f{(x)} = ', sigmoid(float(x)))
            elif type == "relu" :
                print(f'{type} : f{(x)} = ', reLu(float(x)))
            elif type == "elu" :
                print(f'{type} : f{(x)} = ', eLu(float(x)))



