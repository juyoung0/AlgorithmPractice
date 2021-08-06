#include <bits/stdc++.h>

using namespace std;
int room[50][50];
int n, m;
int r, c, dir;
int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, 1, 0, -1};
int cleaned=0;

void clean(){
    int condition=0; //check left room : dirty ->1, clean -> 2
    int left=0, behind=0;
    int next_r, next_c;

    while(true){
        if(condition==0){
            condition += 1;
            cleaned += 1;
            room[r][c] = cleaned+1;
           // cout << "cleaned at "<<r <<","<<c<<endl;
        }

        if(condition>0 && condition<=4){
            left = (dir+3)%4;
            next_r = r+dr[left];
            next_c = c+dc[left];
            if(next_r>0 && next_r <n-1 && next_c>0 && next_c<m-1 && room[next_r][next_c]==0){
                    dir = (dir+3)%4; //rotate
                    r = next_r;
                    c = next_c;
                    condition = 0;
                    //cout << "rotate "<<dir<< endl;
                    continue;
                }
            dir = (dir+3)%4; //rotate
            condition += 1;
        }else if(condition==5){
        //check back is wall or not
            behind = (dir+2)%4;
            next_r = r+dr[behind];
            next_c = c+dc[behind];
            if(next_r>0 && next_r <n-1 && next_c>0 && next_c<m-1 && room[next_r][next_c]!=1){ //not wall
                r = next_r;
                c = next_c;
                condition = 1;
            }else{  //wall
                break;
            }
        }
    }
}

int main()
{
    cin >>n >>m;
    cin >> r>> c>> dir;
    for(int i=0; i<n; ++i){
        for(int j=0; j<m; ++j){
            cin >> room[i][j];
        }
    }
    clean();

    cout <<cleaned;
}
