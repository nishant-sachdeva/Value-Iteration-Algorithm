import numpy as np
import os

utilities3 = np.zeros((5, 4, 3))
utilities13 = np.zeros((5, 4, 3))

path = os.getcwd()
path=path+"/outputs"
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

def findPossibleMovements3(i, j, k, action):
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

delta3=0.001


actions3 = [1, 2, 3] #1 is shoot, 2 is dodge, 3 is recharge

gamma3 = 0.1

penalty3 =-2.5
dummy3 = 0.000
index3=0
f3 = open("outputs/task_2_part_2_trace.txt", "w+")
while True:
    f3.write("iteration="+str(index3)+"\n")
    for j2 in range(0, 4):
        for k2 in range(0, 3):
            f3.write("("+str(0)+","+str(j2)+","+str(k2)+"):-1=["+"%.3f"%dummy3+"]\n")
    count=0
    utilities3=utilities13+0
    val_array=[]
    for i in range(1, 5):
        for j in range(0, 4):
            for k in range(0, 3):
                maxVal=-92233720
                maxAction=0
                for action in actions3:
                    val=0
                    possibleMovements = findPossibleMovements3(i, j, k, action)
                    for temps in possibleMovements:
                        if i+temps[0]==0:
                            val+=((penalty3+10+gamma3*utilities3[i+temps[0]][j+temps[1]][k+temps[2]])*temps[3])
                        else:
                            val+=((penalty3+gamma3*(utilities3[i+temps[0]][j+temps[1]][k+temps[2]]))*temps[3])
                    if maxVal < val:
                        maxAction = action
                        maxVal=val
                utilities13[i][j][k]=maxVal
                val_array.append(maxVal)
                if abs(utilities13[i][j][k]-utilities3[i][j][k])<delta3:
                    count+=1
    ind=0
    for i in range(1, 5):
        for j in range(0, 4):
            for k in range(0, 3):
                maxValArray=[]
                maxAction=0
                for action in actions3:
                    val=0
                    possibleMovements = findPossibleMovements3(i, j, k, action)
                    for temps in possibleMovements:
                        if i+temps[0]==0:
                            val+=((penalty3+10+gamma3*utilities13[i+temps[0]][j+temps[1]][k+temps[2]])*temps[3])
                        else:
                            val+=((penalty3+gamma3*(utilities13[i+temps[0]][j+temps[1]][k+temps[2]]))*temps[3])
                    maxValArray.append(val)
                if maxValArray[0] >= maxValArray[1]:
                    if maxValArray[0] >= maxValArray[2]:
                        f3.write("("+str(i)+","+str(j)+","+str(k)+"):SHOOT=["+"%.3f"%round(val_array[ind], 3)+"]\n")
                    else:
                        f3.write("("+str(i)+","+str(j)+","+str(k)+"):RECHARGE=["+"%.3f"%round(val_array[ind], 3)+"]\n")
                else:
                    if maxValArray[1]>=maxValArray[2]:
                        f3.write("("+str(i)+","+str(j)+","+str(k)+"):DODGE=["+"%.3f"%round(val_array[ind], 3)+"]\n")
                    else:
                        f3.write("("+str(i)+","+str(j)+","+str(k)+"):RECHARGE=["+"%.3f"%round(val_array[ind], 3)+"]\n")
                ind+=1
    index3+=1
    f3.write("\n")
    f3.write("\n")
    if count == 48:
        break
f3.close()
