from Helper_RandomMapGenerator import *
import json
from collections import deque

class Node(object):
    def __init__(self,value):
        self.value = value
        self.ID = 0
        self.parent = None
        self.adjs = []
        self.coord = [None,None]
    def has_parent(self):
        return (self.parent != None)
    def set_value(self,value):
        self.value = value
    def get_value(self):
        return self.value
    def create_link(self,Node):
        self.adjs.append(Node)
    def get_adj_nodes(self):
        return self.adjs
    def set_parent(self,parent):
        self.parent = parent
    def get_parent(self):
        return self.parent
    def set_ID(self,ID):
        self.ID = ID
    def get_ID(self):
        return self.ID
    def set_Coord(self,x,y):
        self.coord[0] = x
        self.coord[1] = y
    def get_Coord(self):
        return self.coord

class Graph(object):
    def __init__(self,source):
        self.source = source
    def Shortest_Path_BFS(self):
        isVisited = {}
        pathFound = 0
        Q = deque()
        #Append Source
        Q.appendleft(self.source)
        isVisited[str(self.source.get_ID())] = True
        while len(Q):
            if pathFound:
                break
            currentNode = Q.pop()
            for adjNode in currentNode.get_adj_nodes():
                if (adjNode.get_value() != 1 and  not isVisited.get(str(adjNode.get_ID()))):
                    adjNode.set_parent(currentNode)
                    isVisited[str(adjNode.get_ID())] = True
                    if adjNode.get_value() == 'G':
                        pathFound = 1
                        isVisited['G'] = adjNode
                        break
                    Q.appendleft(adjNode)
        if not pathFound:
            return False
        else:
            return isVisited['G']


class MapToShortestPath(Graph):
    def __init__(self,mapHeight,mapWidth,fileName):
        self.mapHeight = mapHeight
        self.mapWidth  = mapWidth
        self.fileName  = fileName
    def generate_ID(self):
        i = 0
        while True:
            i = i+1
            yield i
    def Import_Map_File(self):
        #Create 2D Map
        mapArray = [[Node(0) for i in range(self.mapWidth+2)] for j in range(self.mapHeight+2)]

        #Create Walls
        for i in range(self.mapHeight+2):
            mapArray[i][0].set_value = 1
            mapArray[i][-1].set_value = 1
        for i in range(self.mapWidth+2):
            mapArray[0][i].set_value = 1
            mapArray[-1][i].set_value = 1
        
        #Read JSON Data
        with open(self.fileName,'r') as f:
            x = json.load(f)
        
        #Create Generator Object
        myGen = self.generate_ID()
        
        for i in range(1,self.mapHeight+1,1):
            for j in range(1,self.mapWidth+1,1):
                mapArray[i][j].set_value(x[i-1][str(j-1)])
                mapArray[i][j].create_link(mapArray[i+1][j])
                mapArray[i][j].create_link(mapArray[i][j+1])
                mapArray[i][j].create_link(mapArray[i-1][j])
                mapArray[i][j].create_link(mapArray[i][j-1])
                mapArray[i][j].set_ID(next(myGen))
                mapArray[i][j].set_Coord(i,j)
        return mapArray

    def Print_Map_To_File(self, myMap):
        fileName = self.fileName.split(".")[0] + "WithShortestPath.txt"
        fileNamePretty = self.fileName.split(".")[0] + "WithShortestPathPretty.txt"
        with open(fileNamePretty,'w') as f:
            for i in range(len(myMap)):
                for j in range(len(myMap[0])):
                    f.write(str(myMap[i][j].get_value()))
                f.write('\n')
        with open(fileName,'w') as f:
            mapJSON = []
            for i in range(len(myMap)):
                mapJSON.append({})
                for j in range(len(myMap[0])):
                    mapJSON[i][str(j)] = str(myMap[i][j].get_value())
            json.dump(mapJSON,f)

    def SearchforPath(self):
        refinedMap = self.Import_Map_File()
        self.source = refinedMap[1][1]
        Goal = self.Shortest_Path_BFS()
        if Goal:
            currentNode = Goal.get_parent()
            while currentNode.get_parent():
                coordinates = currentNode.get_Coord()
                refinedMap[coordinates[0]][coordinates[1]].set_value('*')
                currentNode = currentNode.get_parent()
                self.Print_Map_To_File(refinedMap)
            return "Found and File is generated"
        else:
            return "Not Found"

#Application
app = MapToShortestPath(4,4,"myMap.txt")
result = app.SearchforPath()
print(result)