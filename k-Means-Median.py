import math
# Point class
# has name, x, y
class Point:
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

# has name, x, y, list of points
class Cluster:
    def __init__(self, name, coords, points):
        self.name = name
        self.coords = coords
        self.points = points
    
    def clearPoints(self):
        self.points.clear()


class Clustering:
    def __init__(self, alg, dim, pointList, clusterList, steps):
        self.alg = alg
        self.dim = dim 
        self.pointList = pointList
        self.clusterList = clusterList
        self.steps = steps


    # Euclidean distance (with square root)
    def euclidean(self, point1, point2):
        # sum of squares under square root
        squareSum = 0

        for i in range(self.dim):
            squareSum += pow(point2.coords[i] - point1.coords[i], 2)
        
        return math.sqrt(squareSum)

    # Manhattan distance (with absolute value)
    def manhattan(self, point1, point2):
        manhat = 0

        for i in range(self.dim):
            manhat += abs(point2.coords[i] - point1.coords[i])

        return manhat

    def assignPoints(self):
        # clear clusters before assigning new points
        self.clearClusters()

        # find closest cluster for each point 
        for point in self.pointList:
            desiredCluster = None
            minDistance = math.inf

            # compare distances of the current point to each cluster
            for cluster in self.clusterList:
                distPointCluster = None
                if self.alg == "kmeans":
                    distPointCluster = self.euclidean(point, cluster)
                else:
                    distPointCluster = self.manhattan(point, cluster)

                if minDistance > distPointCluster:
                    minDistance = distPointCluster
                    desiredCluster = cluster

            # add the point to the closest cluster
            desiredCluster.points.append(point)         
            
            
    def clearClusters(self):
        for cluster in self.clusterList:
            cluster.clearPoints()

    def recalculateClusters(self):
        for cluster in self.clusterList:
            newAvgCoords = [0] * self.dim

            for point in cluster.points:
                for i in range(self.dim):
                    newAvgCoords[i] += point.coords[i]

            numberOfPoints = len(cluster.points)
            if numberOfPoints > 0:
                cluster.coords = [coord / numberOfPoints for coord in newAvgCoords]

    def printClusters(self):
        for cluster in self.clusterList:
            print("Cluster: " + cluster.name + "\nCentroid: ", end="")
            
            for coord in cluster.coords:
                print(coord, end = " ")

            print("\nPoints: ", end = "")

            for point in cluster.points:
                print(point.name, end = " ") 
            print("\n")

    def printClusterCoords(self):
        for cluster in self.clusterList:
            print("Cluster: " + cluster.name + "\nCentroid: ", end="")
            
            for coord in cluster.coords:
                print(coord, end = " ")

            print("\n")

    def printClusterPoints(self):
        for cluster in self.clusterList:
            print("Cluster: " + cluster.name+ "\nPoints: ", end = "")
            
            for point in cluster.points:
                print(point.name, end = " ") 
            print("\n")

    def start(self):
        print('Running {algorithm} algorithm:\n'.format(algorithm = self.alg))

        # print("################################")
        # print("# Iteration: 0 (initial setup) #")
        # print("################################\n")
        
        # self.printClusters()
        
        for i in range(1, self.steps):  
            # print("#################")
            # print("# Iteration: ", i, "#")
            # print("#################\n")
            
            self.assignPoints()
            print("Assignment {i}:".format(i = i))
            self.printClusterPoints()

            # self.printClusters()

            self.recalculateClusters()
            print("Update {i}:".format(i = i))
            self.printClusterCoords()

            print("\n")

# Change here any parameter of the algorithm
def setup():
    alg = "kmeans" # can choose between "kmeans" and "kmedian"
    dimensions = 3
    steps = 5

    # Add points of type Point("name", [x, y, ... ]); template: Point("A", [2.0, 1.1])
    pointList = [
                Point("x0", [3.0, 3.0, 3.0]),
                Point("x1", [1.0, 1.0, 0.0]), 
                Point("x2", [2.0, 0.0, 1.0]), 
                Point("x3", [1.0, -2.0, 0.0]), 
                Point("x4", [1.0, 0.0, 0.0]),
                Point("x5", [2.0, 3.0, 3.0])
            ]

    # Add initial clusters of type Cluster("name", [x, y, ... ], empty list of points); template: Cluster("C", [1.1, 3.4], list())
    clusterList = [
                Cluster("C0", [2.0, 2.0, 0.0], list()), 
                Cluster("C1", [2.0, 0.5, 0.0], list())
            ]

    clustering_alg = Clustering(alg, dimensions,pointList, clusterList, steps)
    clustering_alg.start()

# run with py k (and press tab)
setup()