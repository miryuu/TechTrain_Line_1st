import numpy as np
import in_t_list as itl
from datetime import datetime as dt


def lengs_list(list_d):
    
    time_dif = []
    lengs = []
    
    for i in range(len(list_d[0]) - 1):
        kep = list_d[0][i+1] - list_d[0][i]
        time_dif.append(kep.seconds + kep.microseconds * 10 ** (-6))
        
        
    
    for t in range(len(time_dif)-1):
        ave_speed = (list_d[1][t] + list_d[1][t+1]) / 2
        lengs.append(ave_speed * time_dif[t])

    return time_dif, lengs
                     
        
if __name__ == "__main__":
    
    path = "input_001.txt"
    list_d = itl.input_data(path)
    print(lengs_list(list_d))
    

    
        
        
        
        