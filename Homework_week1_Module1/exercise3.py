from math import *
import random
def exercise3() :
    print("Input number of samples (integer number) which are generated : ", end = '')
    N = type(input())

    if type(N) != int :
        print("number of samples must be an integer number")
    else :
        print("Input lost name: ", end = '')
        loss_name = str(input())
        loss = 0
        if loss_name == "MAE" :
            for i in range(N) :
                predict = random.uniform(0, 10)
                target = random.uniform(0, 10)
                loss+= abs(target - predict)
                print(f'loss name: {loss_name}, ', f'sample: {i}, ', f'pred: {predict}, ', f'target: {target}, ',
                      f'loss: {loss}')
                print()
            loss/= N
            print(f'final {loss_name}: {loss}')
        elif loss_name == "MSE" :
            for i in range(N) :
                predict = random.uniform(0, 10)
                target = random.uniform(0, 10)
                #calculate loss
                loss+= ((target - predict) ** 2)
                print(f'loss name: {loss_name}, ', f'sample: {i}, ', f'pred: {predict}, ', f'target: {target}, ',
                      f'loss: {loss}')
                print()
            loss/= N
            print(f'final {loss_name}: {loss}')
        else :
            for i in range(N) :
                predict = random.uniform(0, 10)
                target = random.uniform(0, 10)
                #calculate loss
                loss+= ((target - predict) ** 2)
                print(f'loss name: {loss_name}, ', f'sample: {i}, ', f'pred: {predict}, ', f'target: {target}, ',
                      f'loss: {loss}')
                print()
            loss/= N
            loss = sqrt(loss)
            print(f'final {loss_name}: {loss}')



            




            




        


