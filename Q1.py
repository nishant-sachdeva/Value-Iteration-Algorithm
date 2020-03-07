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
        temp=[[0, 0, 0, 0]]
        return temp
    elif action == 2 and k == 0:
        temp=[[0, 0, 0, 0]]
        return temp    

delta=0.001


actions = [1, 2, 3] #1 is shoot, 2 is dodge, 3 is recharge

gamma = 0.99

X = 0.5

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
                    if val!=0:
                        if maxVal < val:
                            maxAction = action
                            maxVal=val
                utilities1[i][j][k]=maxVal
                if maxAction==1:
                    f1.write("("+str(i)+","+str(j)+","+str(k)+"):SHOOT=["+"%.3f"%round(maxVal, 3)+"]\n")
                elif maxAction==2:
                    f1.write("("+str(i)+","+str(j)+","+str(k)+"):DODGE=["+"%.3f"%round(maxVal, 3)+"]\n")
                elif maxAction==3:
                    f1.write("("+str(i)+","+str(j)+","+str(k)+"):RECHARGE=["+"%.3f"%round(maxVal, 3)+"]\n")
                if abs(utilities1[i][j][k]-utilities[i][j][k])<delta:
                    count+=1
    index+=1
    f1.write("\n")
    f1.write("\n")
    if count == 48:
        break
f1.close()

# task2 part 1

utilities2 = np.zeros((5, 4, 3))
utilities12 = np.zeros((5, 4, 3))

def findPossibleMovements2(i, j, k, action):
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
        temp=[[0, 0, 0, 0]]
        return temp
    elif action == 2 and k == 0:
        temp=[[0, 0, 0, 0]]
        return temp    

delta2=0.001


actions2 = [1, 2, 3] #1 is shoot, 2 is dodge, 3 is recharge

gamma2 = 0.99

def penatly2(action):
    if action == 1:
        return -0.25
    else:
        return -2.5

dummy2 = 0.000
index2=0
f2 = open("outputs/task_2_part_1_trace.txt", "w+")
while True:
    f2.write("iteration="+str(index2)+"\n")
    for j2 in range(0, 4):
        for k2 in range(0, 3):
            f2.write("("+str(0)+","+str(j2)+","+str(k2)+"):-1=["+"%.3f"%dummy2+"]\n")
    count=0
    utilities2=utilities12+0
    val_array=[]
    for i in range(1, 5):
        for j in range(0, 4):
            for k in range(0, 3):
                maxVal=-92233720
                maxAction=0
                for action in actions2:
                    val=0
                    possibleMovements = findPossibleMovements2(i, j, k, action)
                    for temps in possibleMovements:
                        if i+temps[0]==0:
                            val+=((penatly2(action)+10+gamma2*utilities2[i+temps[0]][j+temps[1]][k+temps[2]])*temps[3])
                        else:
                            val+=((penatly2(action)+gamma2*(utilities2[i+temps[0]][j+temps[1]][k+temps[2]]))*temps[3])
                    if val!=0:
                        if maxVal < val:
                            maxAction = action
                            maxVal=val
                utilities12[i][j][k]=maxVal
                if maxAction==1:
                    f2.write("("+str(i)+","+str(j)+","+str(k)+"):SHOOT=["+"%.3f"%round(maxVal, 3)+"]\n")
                elif maxAction==2:
                    f2.write("("+str(i)+","+str(j)+","+str(k)+"):DODGE=["+"%.3f"%round(maxVal, 3)+"]\n")
                elif maxAction==3:
                    f2.write("("+str(i)+","+str(j)+","+str(k)+"):RECHARGE=["+"%.3f"%round(maxVal, 3)+"]\n")
                if abs(utilities12[i][j][k]-utilities2[i][j][k])<delta2:
                    count+=1
    index2+=1
    f2.write("\n")
    f2.write("\n")
    if count == 48:
        break
f2.close()

#task2 part 2

utilities3 = np.zeros((5, 4, 3))
utilities13 = np.zeros((5, 4, 3))

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
        temp=[[0, 0, 0, 0]]
        return temp
    elif action == 2 and k == 0:
        temp=[[0, 0, 0, 0]]
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
                    if val!=0:
                        if maxVal < val:
                            maxAction = action
                            maxVal=val
                utilities13[i][j][k]=maxVal
                if maxAction==1:
                    f3.write("("+str(i)+","+str(j)+","+str(k)+"):SHOOT=["+"%.3f"%round(maxVal, 3)+"]\n")
                elif maxAction==2:
                    f3.write("("+str(i)+","+str(j)+","+str(k)+"):DODGE=["+"%.3f"%round(maxVal, 3)+"]\n")
                elif maxAction==3:
                    f3.write("("+str(i)+","+str(j)+","+str(k)+"):RECHARGE=["+"%.3f"%round(maxVal, 3)+"]\n")

                if abs(utilities13[i][j][k]-utilities3[i][j][k])<delta3:
                    count+=1
    index3+=1
    f3.write("\n")
    f3.write("\n")
    if count == 48:
        break
f3.close()

#task2 part3
utilities4 = np.zeros((5, 4, 3))
utilities14 = np.zeros((5, 4, 3))

def findPossibleMovements4(i, j, k, action):
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
        temp=[[0, 0, 0, 0]]
        return temp
    elif action == 2 and k == 0:
        temp=[[0, 0, 0, 0]]
        return temp    

delta4=0.0000000001


actions4 = [1, 2, 3] #1 is shoot, 2 is dodge, 3 is recharge

gamma4 = 0.1

penalty4 =-2.5
dummy4 = 0.000
index4=0
f4 = open("outputs/task_2_part_3_trace.txt", "w+")
while True:
    f4.write("iteration="+str(index4)+"\n")
    for j2 in range(0, 4):
        for k2 in range(0, 3):
            f4.write("("+str(0)+","+str(j2)+","+str(k2)+"):-1=["+"%.3f"%dummy4+"]\n")
    count=0
    utilities4=utilities14+0
    val_array=[]
    for i in range(1, 5):
        for j in range(0, 4):
            for k in range(0, 3):
                maxVal=-92233720
                maxAction=0
                for action in actions4:
                    val=0
                    possibleMovements = findPossibleMovements4(i, j, k, action)
                    for temps in possibleMovements:
                        if i+temps[0]==0:
                            val+=((penalty4+10+gamma4*utilities4[i+temps[0]][j+temps[1]][k+temps[2]])*temps[3])
                        else:
                            val+=((penalty4+gamma4*(utilities4[i+temps[0]][j+temps[1]][k+temps[2]]))*temps[3])
                    if val!=0:
                        if maxVal < val:
                            maxAction = action
                            maxVal=val
                utilities14[i][j][k]=maxVal
                if maxAction==1:
                    f4.write("("+str(i)+","+str(j)+","+str(k)+"):SHOOT=["+"%.3f"%round(maxVal, 3)+"]\n")
                elif maxAction==2:
                    f4.write("("+str(i)+","+str(j)+","+str(k)+"):DODGE=["+"%.3f"%round(maxVal, 3)+"]\n")
                elif maxAction==3:
                    f4.write("("+str(i)+","+str(j)+","+str(k)+"):RECHARGE=["+"%.3f"%round(maxVal, 3)+"]\n")

                if abs(utilities14[i][j][k]-utilities4[i][j][k])<delta4:
                    count+=1
    index4+=1
    f4.write("\n")
    f4.write("\n")
    if count == 48:
        break
f4.close()
