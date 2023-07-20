# WGUPS-ROUTING: DATA STRUCTURES AND ALGORITHMS II — C950
This repo is the implementation phase of the WGUPS Routing Program and writeup requested for parts F-H

### Part F:
F. The algorithm used in the solution is a greedy algorithm. It uses a priority queue to prioritize package delivery based on the distance to the delivery location and the package's deadline. The algorithm continually delivers the package with the highest priority (smallest number, since a PriorityQueue in Python is a min-heap) until all packages have been delivered.(C950: Data Structures and Algorithms II, 2.3)

1. Strengths of the algorithm:
- Efficiency: The greedy algorithm is quite efficient as it continually chooses the next best option (package with the highest priority), which reduces the total distance traveled by the trucks. 
- Flexibility: My greedy algorithm can also accommodate changes in the input data (such as different packages, distances, or deadlines) without needing to be significantly altered or redesigned.
2. Verification of requirements:

- All packages are delivered within their respective deadlines since the algorithm prioritizes packages based on their deadlines.
The total distance traveled by the trucks is minimized as much as possible, as the algorithm chooses to deliver the packages that are closest first.
The algorithm can handle any number of packages and trucks, as they are not hardcoded into the algorithm. This allows the algorithm to be scalable and flexible.
3. Other Algorithms:

- Dijkstra's Algorithm: This algorithm could also be used to meet the requirements in the scenario. Dijkstra's Algorithm is a graph-based algorithm used to find the shortest path between two nodes.  (C950: Data Structures and Algorithms II, 5.9 )This could be applied to this scenario by treating each delivery location as a node and the distances between them as the weights of the edges connecting the nodes. The algorithm would then find the shortest path that visits all nodes, delivering all packages in the shortest total distance.
- Genetic Algorithm: A genetic algorithm could also be used to solve this problem. Genetic algorithms are based on the process of natural selection and can be used to find approximate solutions to optimization problems. (Genetic algorithm 2023) In this scenario, each "individual" in the population could be a different sequence of deliveries, and the "fitness" of each individual could be the total distance traveled to make those deliveries.
3. a. Difference from original algorithm:
- Dijkstra's Algorithm: Unlike the greedy algorithm used in the solution, Dijkstra's Algorithm does not make decisions based on local optima. Instead, it finds the globally optimal solution by considering all possible paths. (C950: Data Structures and Algorithms II, 5.9 )This could potentially lead to more efficient routes but at the cost of higher computational complexity.
- Genetic Algorithm: The genetic algorithm differs significantly from the original algorithm. Instead of making decisions based on local optima, the genetic algorithm evolves a population of solutions over time (Genetic algorithm 2023), using operations inspired by biological evolution such as mutation, crossover (recombination), and selection. Genetic algorithms are typically used for more complex optimization problems where the search space is large and the optimal solution is not clear.

### Part G:
- If I were to do this project again I would explore using different data structures for managing the packages and addresses. For example, using a graph data structure with the addresses as nodes and distances as edge weights could be beneficial for some operations. This might make it easier to implement more complex routing algorithms and to visualize the problem. I would also change the algorithm because the current greedy algorithm prioritizes packages based on the sum of the distance and deadline. Although this works well in most cases, there might be situations where a different prioritization strategy could yield better results. I would explore different ways to calculate package priority, possibly taking into account other factors such as package weight or delivery constraints.

### Part H:
1. One data structure that could accomplish the same requirements in the scenario is a balanced search trees. The balanced search tree structure provides efficient search, insertion, and deletion operations, which could be beneficial for managing the packages or the locations. In contrast to the hash table used in the solution, the BST maintains an order among the elements, which can make it easier to perform operations that require sorted data, such as finding the minimum or maximum, or performing range queries.
2. Another data structure that could accomplish the same thing could be a graph data structure. The implementation of a graph could be that each location could be a node in the graph, and there could be an edge between two nodes if there is a direct route between those locations. (C950: Data Structures and Algorithms II, 5.1)  The weight of the edge could represent the distance between the two locations. In contrast to the hash table used in my solution, the graph structure can naturally represent the distances between locations, which can make it easier to implement certain routing algorithms.

### Part I:
Sources:
- Lysecky, R., & Vahid, F. (2018, June). C950: Data Structures and Algorithms II. zyBooks.
Retrieved July 20, 2023, from  https://learn.zybooks.com/zybook/WGUC950AY20182019/

- Wikimedia Foundation. (2023, July 1). Genetic algorithm. Wikipedia. https://en.wikipedia.org/wiki/Genetic_algorithm 