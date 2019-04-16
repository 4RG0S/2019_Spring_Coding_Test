# problem URL -> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15OZ4qAPICFAYD
import itertools

def main():
	testcase_count = int(input().strip())

	for testcase_num in range(1, testcase_count + 1):
		cusomter_count = int(input().strip())
		location_list = list(map(int, input().strip().split(' ')))
		customer_location_list = list()
			
		company_location = (location_list[0], location_list[1])
		home_location = (location_list[2], location_list[3])


		for i in range(4, len(location_list),2):
			customer_location_list.append((location_list[i], location_list[i+1]))				
			
		min_distance = float('inf')
		for case in itertools.permutations(customer_location_list):
			route = [company_location, *list(case) ,home_location]

			distance = 0
			for i in range(0, len(route) - 1):
				distance += abs(route[i][0] - route[i+1][0]) + abs(route[i][1] - route[i+1][1])

			if distance < min_distance:
				min_distance = distance

		print("#{} {}".format(testcase_num, min_distance))

if __name__ == "__main__":
	main()
