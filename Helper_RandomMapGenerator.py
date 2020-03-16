import random
import json

#GENERATING RANDOM 2D MAP: Args: Height, Width , file to write in
def Genrate_Random_Map(Height, Width ,fileName):
    myMap = []
    with open(fileName,'w') as f:
        for i in range(Height):
            myMap.append({})
            for j in range(Width):
                myMap[i][str(j)] = random.randint(0,1)
        myMap[0]['0'] = 'S'
        myMap[-1][str(Width-1)] = 'G'
        json.dump(myMap,f)

def Print_MapJSON_Pretty(myMap):
    fileName = myMap.split('.')[0] + "Pretty.txt"
    with open(myMap,'r') as w:
        x = json.load(w)
    with open(fileName,'w') as f:
        for i in range(len(x)):
            for j in range(len(x[0])):
                f.write(str(x[i][str(j)]))
            f.write('\n')
