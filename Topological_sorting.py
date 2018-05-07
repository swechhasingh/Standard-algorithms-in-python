
import Queue

print "no. of vertices: "
n = int(raw_input()) 
adj_matrix = [[int(j) for j in raw_input().split(" ")] for i in range(n)]

def Topological_sorting(matrix, v):

	visited = [0]*v
	queue = in_degree(matrix,visited,v)
	count = 0
	
	while count < v:
		vertex = queue.get()
		print vertex
		visited[vertex] = 1
		count += 1
		for j in range(v):
			matrix[vertex][j] = 0
		queue = in_degree(matrix,visited,v)


def in_degree(matrix,visit,v):

	q = Queue.Queue()
	for i in range(v):
		count = 0
		for j in range(v):
			if matrix[j][i] == 0 :
				count += 1
		if count == v and visit[i] == 0:
			q.put(i)	
	return q




Topological_sorting(adj_matrix, n)