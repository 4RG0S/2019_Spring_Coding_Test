// Problem URL -> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <map>
#include <queue>

using namespace std;

vector<int>* split(string str);
void rtrim(string& str, const string& delimiters = " \f\n\r\t\v");
void ltrim(string& str, const string& delimiters = " \f\n\r\t\v");
void trim(string& str, const string& delimiters = " \f\n\r\t\v");

class Vertex {
private:
	int number;
	int hop;
	
public:
	Vertex(int number, int hop);
	~Vertex();
	int getNumber();
	int getHop();
};

int main() {
	ifstream ifs;
	ifs.open("contact_input.txt", ios_base::in);
	
	int data_length;
	int start_point;
	string temp;					// ���ڿ� �Է¹��� �� �̿�Ǵ� temp ����
	
	vector<int>* input_data;		// �Է¹��� ���ڿ��� split�� �� ������ ���� ������ ����
	for (int testcase_number = 1; testcase_number <= 10; testcase_number++) {
		map<int, vector<int>> graph;
		bool visited[100];
		fill_n(visited, 100, false);		// visited �迭�� ��� ���Ҹ� false��

		getline(ifs, temp);
		trim(temp);
		input_data = split(temp);
		
		
		data_length = input_data->at(0);
		start_point = input_data->at(1);
		delete input_data;

		getline(ifs, temp);
		trim(temp);
		input_data = split(temp);
	
		for (int i = 0; i < data_length; i += 2) {
			int from_vertex = input_data->at(i);
			int to_vertex = input_data->at(i+1);
			
			if (graph.find(from_vertex) == graph.end()) {
				vector<int> to_vertex_list;
				to_vertex_list.push_back(to_vertex);
				graph.insert(pair<int, vector<int>>(from_vertex, to_vertex_list));
			}
			else {
				vector<int> to_vertex_list = graph.at(from_vertex);
				vector<int>::iterator iter;
				iter = find(to_vertex_list.begin(), to_vertex_list.end(), to_vertex);
			
				if (iter == to_vertex_list.end()) {
					graph.at(from_vertex).push_back(to_vertex);
				}
			}	
		}

		delete input_data;

		/*
		map�� Ű���� list�� ����ϴ� �ڵ�
		
		map<int, vector<int>>::iterator iter;
		for (iter = graph.begin(); iter != graph.end(); iter++) {
			vector<int> to_vertex_list = iter->second;
			
			cout << "key : " << iter->first << endl;
			cout << "value : ";
			vector<int>::iterator to_vertex_iter;
			for (to_vertex_iter = to_vertex_list.begin(); to_vertex_iter != to_vertex_list.end(); to_vertex_iter++) {
				cout << *to_vertex_iter << " ";
			}
			cout << endl;
		}
		*/
		

		// BFS�� ���� �ذ�
		int result = -1;
		int maxhop = -1;
		
		queue<Vertex> queue;			// bfs�� ť
		visited[start_point] = true;
		queue.push(Vertex(start_point, 0));

		while (!queue.empty()) {
			Vertex poped_vertex = queue.front();
			queue.pop();

			if (poped_vertex.getHop() > maxhop) {			// �ֱٿ� �������� ����� ����
				maxhop = poped_vertex.getHop();
				result = poped_vertex.getNumber();
			}
			else if (poped_vertex.getHop() == maxhop && poped_vertex.getNumber() > result) {	// �ֱٿ� �������� �ο��� �ټ��� ��� ���� ū ������ ����
				result = poped_vertex.getNumber();
			}

			if (graph.find(poped_vertex.getNumber()) == graph.end()) {
				continue;
			}

			vector<int> to_vertex_list = graph.at(poped_vertex.getNumber());
			for (int vertex_num : to_vertex_list) {								// �湮�� ������ ���� �������� ť�� �߰��ϱ�
				if (visited[vertex_num - 1] == false) {
					visited[vertex_num - 1] = true;
					queue.push(Vertex(vertex_num, poped_vertex.getHop() + 1));
				}
			}
		}
		
		cout << "#" << testcase_number << " " << result << endl;
	}
	ifs.close();

	return 0;
}

int Vertex::getNumber() {
	return number;
}

int Vertex::getHop() {
	return hop;
}

Vertex::Vertex(int number, int hop) {
	this->number = number;
	this->hop = hop;
}

Vertex::~Vertex(){}

vector<int>* split(string str) {
	istringstream iss(str);
	//vector<string>* results = new vector<string>(istream_iterator<string>(iss), istream_iterator<string>());
	//vector<string> results((istream_iterator<string>(iss)), istream_iterator<string>());
	
	vector<int>* results = new vector<int>(istream_iterator<int>(iss), istream_iterator<int>());
	return results;
}

void rtrim(string& str, const string& delimiters) {
	size_t found = str.find_last_not_of(delimiters);
	if (found != string::npos) {
		str.erase(found + 1);
	}
	else {
		str.clear();
	}
}

void ltrim(string& str, const string& delimiters) {
	size_t found = str.find_first_not_of(delimiters);
	if (found != string::npos) {
		str.erase(0, found);
	}
	else {
		str.clear();
	}
	
}

void trim(string& str, const string& delimiters) {
	ltrim(str);
	rtrim(str);
}
