import numpy as np
import os

path = os.getcwd()
path=path+"/outputs"
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

#task1 

utilities = np.zeros((5, 4, 3))
utilities1 = np.zeros((5, 4, 3))

def findPossibleMovements(i, j, k, action):
    if action == 1 and i>=1 and j>=1 and k>=1:
        temp=[[-1, -1, -1, 0.5], [0, -1, -1, 0.5]]
        return temp
    elif action == 2 and k == 2 and j <= 2:
        temp=[[0, +1, -1, 0.64], [0, 0, -1, 0.16], [0, +1, -2, 0.16], [0, 0, -2, 0.04]]
        return temp
    elif action == 2 and k == 2 and j > 2:
        temp=[[0, 0, -1, 0.8], [0, 0, -2, 0.2]]
        return temp
    elif action == 2 and k == 1 and j <= 2:
        temp=[[0, +1, -1, 0.8], [0, 0, -1, 0.2]]
        return temp
    elif action == 2 and k == 1 and j > 2:
        temp=[[0, 0, -1, 1]]
        return temp
    elif action == 3 and k <= 1:
        temp=[[0, 0, +1, 0.8], [0, 0, 0, 0.2]]
        return temp
    elif action == 3 and k > 1:
        temp=[[0, 0, 0, 1]]
        return temp
    elif action == 1 and ( j == 0 or k == 0 ):
        temp=[[0, 0, 0, 1]]
        return temp
    elif action == 2 and k == 0:
        temp=[[0, 0, 0, 1]]
        return temp    

delta=0.001


actions = [1, 2, 3] #1 is shoot, 2 is dodge, 3 is recharge

gamma = 0.99

X = 1

penalty = -10/X

dummy = 0.000
index=0
f1 = open("outputs/task_1_trace.txt", "w+")
while True:
    f1.write("iteration="+str(index)+"\n")
    for j2 in range(0, 4):
        for k2 in range(0, 3):
            f1.write("("+str(0)+","+str(j2)+","+str(k2)+"):-1=["+"%.3f"%dummy+"]\n")
    count=0
    utilities=utilities1+0
    val_array=[]
    for i in range(1, 5):
        for j in range(0, 4):
            for k in range(0, 3):
                maxVal=-92233720
                maxAction=0
                for action in actions:
                    val=0
                    possibleMovements = findPossibleMovements(i, j, k, action)
                    for temps in possibleMovements:
                        if i+temps[0]==0:
                            val+=((penalty+10+gamma*utilities[i+temps[0]][j+temps[1]][k+temps[2]])*temps[3])
                        else:
                            val+=((penalty+gamma*(utilities[i+temps[0]][j+temps[1]][k+temps[2]]))*temps[3])
                    if maxVal < val:
                        maxAction = action
                        maxVal=val
                utilities1[i][j][k]=maxVal
                val_array.append(maxVal)
                if abs(utilities1[i][j][k]-utilities[i][j][k])<delta:
                    count+=1
    ind=0
    for i in range(1, 5):
        for j in range(0, 4):
            for k in range(0, 3):
                maxValArray=[]
                maxAction=0
                for action in actions:
                    val=0
                    possibleMovements = findPossibleMovements(i, j, k, action)
                    for temps in possibleMovements:
                        if i+temps[0]==0:
                            val+=((penalty+10+gamma*utilities1[i+temps[0]][j+temps[1]][k+temps[2]])*temps[3])
                        else:
                            val+=((penalty+gamma*(utilities1[i+temps[0]][j+temps[1]][k+temps[2]]))*temps[3])
                    maxValArray.append(val)
                if maxValArray[0] >= maxValArray[1]:
                    if maxValArray[0] >= maxValArray[2]:
                        f1.write("("+str(i)+","+str(j)+","+str(k)+"):SHOOT=["+"%.3f"%round(val_array[ind], 3)+"]\n")
                    else:
                        f1.write("("+str(i)+","+str(j)+","+str(k)+"):RECHARGE=["+"%.3f"%round(val_array[ind], 3)+"]\n")
                else:
                    if maxValArray[1]>=maxValArray[2]:
                        f1.write("("+str(i)+","+str(j)+","+str(k)+"):DODGE=["+"%.3f"%round(val_array[ind], 3)+"]\n")
                    else:
                        f1.write("("+str(i)+","+str(j)+","+str(k)+"):RECHARGE=["+"%.3f"%round(val_array[ind], 3)+"]\n")
                ind+=1
    index+=1
    f1.write("\n")
    f1.write("\n")
    if count == 48:
        break
f1.close()


