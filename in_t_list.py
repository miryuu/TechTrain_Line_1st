import numpy as np
from datetime import datetime as dt
#13:50:08.245 0.0

def input_data(path):
    kep0 = []
    kep1 = []
    with open(path) as f:
        stript_d = [i.strip() for i in f.readlines()]
        for d in stript_d:
            if len(d) >= 15:
                kep0.append(dt.strptime(d[:12], '%H:%M:%S.%f'))
                kep1.append(float(d[13:]))
                
        data = [kep0,kep1]
            
    return data                

if __name__ == "__main__":
    
    path = "input_001.txt"
    
    print(input_data(path))

