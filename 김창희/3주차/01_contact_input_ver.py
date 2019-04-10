# Problem URL -> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD
from collections import deque

class Vertex:
	def __init__(self, number, hop):
		self.number = number
		self.hop = hop


def main():
	for testcase_number in range(1, 11):
		graph = dict()
		visited = [False for i in range(100)]

		prolog = list(map(int, input().strip().split(' ')))	
		data_length = prolog[0]
		start_point = prolog[1]

		data_list = list(map(int, input().strip().split(' ')))
			
		for i in range(0, data_length, 2):
			from_vertex = data_list[i]
			to_vertex = data_list[i+1]

			if from_vertex not in graph:
				graph[from_vertex] = [to_vertex]
			elif to_vertex not in graph[from_vertex]:
				graph[from_vertex].append(to_vertex)


		# BFS를 통한 해결
		result = -1
		maxhop = -1

		queue = deque()				# BFS용 큐
			
		visited[start_point - 1] = True
		queue.append(Vertex(start_point, 0))

		while len(queue) > 0:
			temp_vertex = queue.popleft()
				
			if temp_vertex.hop > maxhop:
				maxhop = temp_vertex.hop
				result = temp_vertex.number
			elif temp_vertex.hop == maxhop and temp_vertex.number > result:
				result = temp_vertex.number
			
			if temp_vertex.number not in graph:
				continue

			to_list = graph[temp_vertex.number]
			for to in to_list:
				if visited[to - 1] == False:
					visited[to -1] = True
					queue.append(Vertex(to, temp_vertex.hop + 1))

		print("#{} {}".format(testcase_number, result))

if __name__ == "__main__":
	main()
