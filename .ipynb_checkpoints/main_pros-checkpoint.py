import numpy as np
import in_t_list as itl


def time_delt(list_d):
    
    first_fare = 410 # 1.052km
    up_fare = 80 # 237m
    kep = 0
    time_dif = []
    
    for i in range(len(list_d[0]) - 1):
        time_dif.append(list_d[0][i+1] - list_d[0][i])
    
    return time_dir
        
if __name__ == "__main__":
    
    path = "input_001.txt"
    list_d = itl.input_data(path)
    print(time_delt(list_d))
    

    
        
        
        
        