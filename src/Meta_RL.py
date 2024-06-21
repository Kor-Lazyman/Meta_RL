import random
task=[]

def Make_Task():
    for mean in range(7,15):
        for high in range(0,5):
            for low in range(0,5):
               Dist_info={"Dist_Type":0,
               "Mean":mean,
               "High":high,
               'Low':low}
               task.append(Dist_info)

    for mean in range(7,15):
        for sigma in range(0,5):
            Dist_info={"Dist_Type":1,
             "Mean":mean,
             "Sigma":sigma
            }
            task.append(Dist_info)
    return task
Dist_info=Make_Task()