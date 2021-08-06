#include <iostream>
#include<fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <cstdio>

using namespace std;
int mymap[500][500];

using namespace std;

int Tetromino[19][4][2] = {
    {{0, 0}, {1, 0}, {2, 0}, {3, 0}},
    {{0, 0}, {0, 1}, {0, 2}, {0, 3}},
    {{0, 0}, {0, 1}, {1, 0}, {1, 1}},
    {{0, 0}, {1, 0}, {2, 0}, {2, 1}},
    {{0, 0}, {1, -2}, {1, -1}, {1, 0}},
    {{0, 0}, {0, 1}, {1, 1}, {2, 1}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 0}},
    {{0, 0}, {1, 0}, {2, 0}, {2, -1}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 2}},
    {{0, 0}, {0, 1}, {1, 0}, {2, 0}},
    {{0, 0}, {1, 0}, {1, 1}, {1, 2}},
    {{0, 0}, {1, 0}, {1, 1}, {2, 1}},
    {{0, 0}, {0, 1}, {1, -1}, {1, 0}},
    {{0, 0}, {1, -1}, {1, 0}, {2, -1}},
    {{0, 0}, {0, 1}, {1, 1}, {1, 2}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 1}},
    {{0, 0}, {1, 0}, {1, 1}, {2, 0}},
    {{0, 0}, {1, -1}, {1, 0}, {1, 1}},
    {{0, 0}, {1, -1}, {1, 0}, {2, 0}},
};

int test_case(int tetro[4][2],int n, int m){
    int local_sum=0;
    int local_max=0;
    int x=0, y=0;
    for (int i = 0; i < n; ++i) {
        for (int j=0; j < m; ++j){
            for(int k=0; k<4; ++k){
                x = tetro[k][0]+i;
                y = tetro[k][1]+j;
                if(x>=0 && x<n && y>=0 && y<m){
                    local_sum += mymap[x][y];
                    if(k==3){
                        local_max= max(local_max, local_sum);
                        local_sum= 0;
                    }
                }else{
                    local_sum = 0;
                    k = 5;
                }
            }
        }
    }
    return local_max;
}

int main()
{
    int n, m;
    cin>> n >> m;

    for (int i = 0; i < n; ++i) {
        for (int j=0; j < m; ++j){
            cin >> mymap[i][j];
        }
    }
    int local_max=0, global_max=0;

    for(int i=0; i<19; ++i){
        local_max = test_case(Tetromino[i], n, m);
        global_max = max(global_max, local_max);
    }

    cout <<global_max;
    return 0;
}
