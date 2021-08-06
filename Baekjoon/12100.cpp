#include <iostream>
#include<fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <cstdio>
#include <queue>

int dx[4] = {0, 1, 0, -1}; //E, S, W, N
int dy[4] = {1, 0, -1, 0};
int n=0; //max 20
std::vector<std::vector<int> > board;

using namespace std;

/* 인접한 두개만 검사하지 말 것 */
vector<int> merge_line(vector<int> line){
 //   int *merged = new int[n+1]; //important!!!!!
    vector<int> merged;
    int cell_cnt = 0;
    int prev = -1;

    for(int i=0; i<n; i++){
        if(prev==-1)
            prev = i;
        else{
            if(line.at(prev)==0){
                prev = i;
            }
            else{
                if(line.at(i)!=0){
                    if(line.at(i)==line.at(prev)){ //same number
                    //    merged[cell_cnt] = line[i]+line[prev];
                        merged.push_back(line.at(i)*2);
                        cell_cnt += 1;
                        prev = -1;
                    }else{ //different number
                     //   merged[cell_cnt] = line[prev];
                        merged.push_back(line.at(prev));
                        cell_cnt += 1;
                        prev = i;
                    }
                }
            }
        }
    }

    if(prev!=-1){
        merged.push_back(line.at(prev));
        cell_cnt += 1;
    }
    //merged[n] = line[n];

    for(int j=cell_cnt; j<n; ++j)
        merged.push_back(0);

    return merged;
}

//heading = 0:E, 1:S, 2:W, 3:N
//int moving(int local_board[21][21], int heading, int trial){
int moving(vector<vector<int> > local_board, int heading, int trial){
    int max1=0, max2=0, max3=0, max4=0, max_total=0;
    vector<int> temp;
    vector<int> merged;
//    int* temp = new int[21];
 //   int* merged;
    int idx=0;
  //  cout <<"heading : "<<heading << " trial : "<<trial<<endl;

    if(trial==6){
        //return max value
        for (int i=1; i<=n; ++i){
            for(int j=1; j<=n; ++j){
                max_total = max(max_total, local_board[i-1][j-1]);
            }
        }

        return max_total;
    }

    if(heading==0){
        for(int i=1; i<=n; ++i){
            for(int j=n; j>0; --j){
                    temp.push_back(local_board[i-1][j-1]);
                   // temp[idx] = local_board[i][j];
            }
            merged = merge_line(temp);
            idx = 0;
            for(int j=n; j>0; --j){
                    local_board[i-1][j-1] = merged.at(idx);
                    idx += 1;
            }
            merged.clear();
            temp.clear();
        }
    }else if(heading==1){
        for(int j=1; j<=n; ++j){
            for(int i=n; i>0; --i){
                    temp.push_back(local_board[i-1][j-1]);
            }
            merged = merge_line(temp);
            idx = 0;

            for(int i=n; i>0; --i){
                    local_board[i-1][j-1] = merged.at(idx);
                    idx += 1;
            }
            merged.clear();
            temp.clear();
        }
    }else if(heading==2){
        for (int i=1; i<=n; ++i){
            for(int j=1; j<=n; ++j){
                    temp.push_back(local_board[i-1][j-1]);
            }
            merged = merge_line(temp);
            idx = 0;
            for(int j=1; j<=n; ++j){
                    local_board[i-1][j-1] =merged.at(idx);
                    idx += 1;
            }
            merged.clear();
            temp.clear();
        }
    }
    else if(heading==3){
        for(int j=1; j<=n; ++j){
            for(int i=1; i<=n; ++i){
                    temp.push_back(local_board[i-1][j-1]);
            }
            merged = merge_line(temp);
            idx = 0;
            for(int i=1; i<=n; ++i){
                    local_board[i-1][j-1] = merged.at(idx);
                    idx += 1;
            }
            merged.clear();
            temp.clear();
        }
    }

    /*
    cout <<"heading : "<<heading << " trial : "<<trial<<endl;
    for (int i=1; i<=n; ++i){
        for(int j=1; j<=n; ++j){
            cout <<local_board[i-1][j-1];
        }
        cout<<endl;
    }*/

    max1 = moving(local_board, 0, trial+1);
    max2 = moving(local_board, 1, trial+1);
    max3 = moving(local_board, 2, trial+1);
    max4 = moving(local_board, 3, trial+1);
    max_total = max(max1, max2);
    max_total = max(max_total, max3);
    max_total = max(max_total, max4);
    return max_total;
}

int main()
{
    int max1, max2, max_total, elem;
  //  int board[21][21]; //true, false

    cin>> n;

    //initialize
    for (int i=1; i<=n; ++i){
        vector<int> element;
        for(int j=1; j<=n; ++j){
            cin >> elem;
            element.push_back(elem);
        }
        board.push_back(element);
    }

    max1 = max(moving(board, 0, 1), moving(board, 1, 1));
    max2 = max(moving(board, 2, 1), moving(board, 3, 1));
    max_total = max(max1, max2);

    cout << max_total;

    return 0;
}
