#include<iostream>
#include<vector>
using namespace std;

int map[100][100];
int N, L;
int pass = 0;

void findRoad(int num, bool Column) {
	int path[100];
	int diff = 0;
	int sameHeight = 1;
	bool blocked = false;

	for (int i = 0; i < N; ++i) {
		if (Column) {
			path[i] = map[i][num];
		}
		else {
			path[i] = map[num][i];
		}
	}
	int j = 0;
//	cout << endl;
//	cout << num << endl;
	for (; j < N-1; ++j) {
		diff = path[j + 1] - path[j];
		if (diff == 0) {
			sameHeight++;
		}
		else if (diff == 1) {
			if (sameHeight >= L) {
				sameHeight = 1;
			}
			else {
				blocked = true;
			}
		}
		else if (diff >= 2) {
			blocked = true;
		}
		else if (diff == -1) {
			if (N - 1 - j < L)
				blocked = true;
			else {
				if (L == 1)
					sameHeight = 0;
				else {
					int k = 1;
					for (; k < L; ++k) {
						if (path[j + k] != path[j + k + 1]) {
							blocked = true;
							k = L;
						}
						if (k == L - 1) {
							j += (L - 1);
							sameHeight = 0;
						}
					}
				}
			}
		}
		else if (diff <= -2) {
			blocked = true;
		}

		if (blocked == true) {
			break;
		}
	}
	if (j == N - 1)
		pass++;
}

int main() {
	cin >> N;
	cin >> L;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			cin >> map[i][j];
		}
	}

	for (int i = 0; i < N; ++i) {
		findRoad(i, false);
		findRoad(i, true);
	}

	cout << pass;
}