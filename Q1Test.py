import numpy as np

utilities = np.zeros((2, 2, 2))
utilities1 = np.zeros((2, 2, 2))


def findPossibleMovements(i, j, k, action):
    if action == 1 and i==1 and j==1 and k==1:
        temp=[[-1, -1, -1, 0.5], [0, -1, -1, 0.5]]
        return temp
    # elif action == 2 and k == 2 and j <= 2:
    #     temp=[[0, +1, -1, 0.64], [0, 0, -1, 0.16], [0, +1, -2, 0.16], [0, 0, -2, 0.04]]
    #     return temp
    # elif action == 2 and k == 2 and j > 2:
    #     temp=[[0, 0, -1, 0.8], [0, 0, -2, 0.2]]
    #     return temp
    elif action == 2 and k == 1 and j == 0:
        temp=[[0, +1, -1, 0.8], [0, 0, -1, 0.2]]
        return temp
    elif action ==2 and k == 1 and j==1:
        temp=[[0, 0, -1, 1]]
        return temp
    # elif action == 2 and k == 1 and j > 2:
    #     temp=[[0, 0, -1, 1]]
    #     return temp
    elif action == 3 and k == 0:
        temp=[[0, 0, +1, 0.8], [0, 0, 0, 0.2]]
        return temp
    elif action == 3 and k == 1:
        temp=[[0, 0, 0, 1]]
        return temp
    elif action == 1 and ( j == 0 or k == 0 ):
        temp=[[0, 0, 0, 1]]
        return temp
    elif action == 2 and k == 0:
        temp=[[0, 0, 0, 1]]
        return temp    

delta=0.0000000001


actions = [1, 2, 3] #1 is shoot, 2 is dodge, 3 is recharge

gamma = 0.1

X = 4

penalty = -10/X

print("penalty is",penalty)

index=0

while True:
    print("iteration:", index)
    for j2 in range(0, 2):
        for k2 in range(0, 2):
            print("("+str(0)+","+str(j2)+","+str(k2)+"):-1=["+str(round(0., 3))+"]")
    count=0
    utilities=utilities1+0
    val_array=[]
    for i in range(1, 2):
        for j in range(0, 2):
            for k in range(0, 2):
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
                if abs(utilities[i][j][k]-utilities1[i][j][k]) < delta:
                    count+=1
    ind=0
    for i in range(1, 2):
        for j in range(0, 2):
            for k in range(0, 2):
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
                        print("("+str(i)+","+str(j)+","+str(k)+"):SHOOT=["+"%.3f"%round(val_array[ind], 3)+"]")
                    else:
                        print("("+str(i)+","+str(j)+","+str(k)+"):RECHARGE=["+"%.3f"%round(val_array[ind], 3)+"]")
                else:
                    if maxValArray[1]>=maxValArray[2]:
                        print("("+str(i)+","+str(j)+","+str(k)+"):DODGE=["+"%.3f"%round(val_array[ind], 3)+"]")
                    else:
                        print("("+str(i)+","+str(j)+","+str(k)+"):RECHARGE=["+"%.3f"%round(val_array[ind], 3)+"]")
                ind+=1
    index+=1
    print()
    print()
    if count == 48:
        break

