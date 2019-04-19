// Problem URL -> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141176AIwCFAYD
// ���� ���� ���� ����Ҷ�, ���� ������ ������ ������ int��� size_t ����ϱ�

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;
 
vector<string>* split(const string& str, char delimiter);
bool is_digit(string str);				// ���ڿ��� ���ڷ� ��ȯ �������� �˻�
void rtrim(string& str, const string& delimiters = " \f\n\r\t\v");
void ltrim(string& str, const string& delimiters = " \f\n\r\t\v");
void trim(string& str, const string& delimiters = " \f\n\r\t\v");

int main() {
	ifstream ifs;
	ifs.open("input.txt", ios_base::in);

	string temp;						// ������ �Է¹��� �� ����� ����
	int num_of_nodes;				// �� ���̽��� ����� ����
	for (int testcase = 1; testcase <= 10; testcase++) {
		/*
			�Է��� ���� ����Ʈ�� �̴�.

			��Ģ������ ��ȿ�� ����
			1. ��� ���� �ڽ��� ���ų� ���̾�� ��(��, �� ����� ������ ¦������ ��)
			2. ���� ����� data�� �����ڿ��� ��
			3. ���� ����� data�� ���ڿ��� ��
		*/

		// ����� ���� �Է� �ޱ�
		getline(ifs, temp);
		trim(temp);
		num_of_nodes = atoi(temp.c_str());

	
		vector<string>* node_info;		// �� ����� ����
		vector<bool> data_is_digit_vector(num_of_nodes);		// �� ����� data�� ��������, ������������ ������ ����
																// ������ ��� true, �������� ��� false ����
		

		for (int i = 0; i < num_of_nodes; i++) {
			// �� ����� ���� �Է¹ޱ�
			getline(ifs, temp);
			trim(temp);
			node_info = split(temp, ' ');

			data_is_digit_vector.at(i) = is_digit(node_info->at(1));
			delete node_info;
		}


		// ���� 1�� �������� ���� ���
		if (num_of_nodes % 2 == 0) {
			cout << "#" << testcase << " 0" << endl;
			continue;
		}


		// ù��° �������, 
		// ���� �� ����� ������ 1��(��Ʈ�� ����)�� ���, first_leaf_node = 0;
		int first_leaf_node = (num_of_nodes - 2) / 2 + 1; 
		
		bool effectiveness = true;		// ��ȿ��
		

		// ���� 2�� �������� ���� ���
		for (int node_number = 0; node_number < first_leaf_node; node_number++) {
			if (data_is_digit_vector.at(node_number) == true) {
				effectiveness = false;
				break;
			}
		}

		if (!effectiveness) {
			cout << "#" << testcase << " 0" << endl;
			continue;
		}




		// ���� 3�� �������� ���� ���
		for (int node_number = first_leaf_node; node_number < num_of_nodes; node_number++) {
			if (data_is_digit_vector.at(node_number) == false) {
				effectiveness = false;
				break;
			}
		}
		
		if (!effectiveness) {
			cout << "#" << testcase << " 0" << endl;
			continue;
		}

		

		// ���� 1, 2, 3 ��� �����ϸ� ��ȿ�� ��Ģ ����
		cout << "#" << testcase << " 1" << endl;
		
		

		/*
		�� ����� data�� ��������, ������������ ������ ���� ���
		
		vector<bool>::iterator iter;
		for (iter = data_is_digit_vector.begin(); iter != data_is_digit_vector.end(); iter++) {
			cout << *iter << " ";
		}
		cout << endl;
		*/
		

	}
	ifs.close();

	return 0;
}

bool is_digit(string str) {
	// str�� "0"�� ��쵵 ���
	return atoi(str.c_str()) != 0 || str.compare("0") == 0;
}

vector<string>* split(const string& str, char delimiter)
{
	vector<string>* tokens = new vector<string>();
	string token;

	istringstream tokenStream(str);
	while (getline(tokenStream, token, delimiter)) {
		tokens->push_back(token);
	}

	return tokens;
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