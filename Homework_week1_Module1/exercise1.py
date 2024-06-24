def exercise1(tp, fp, fn) :
    if(type(tp) != int) :
        print("tp must be int")
    elif (type(fp) != int) :
        print("fp must be int") 
    elif (type(fn) != int) :
        print("fn must be int")
    elif tp <= 0 or fp <= 0 or fn <= 0 :
        print("tp and fp and fn must be greater than zero")
    else :
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1_score = (2 * (precision * recall)) / (precision + recall)        
        print(f'precision is {precision}')
        print(f'recall is {recall}')
        print(f'f1-score is {f1_score}')


    
