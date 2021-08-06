#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int rotation[6] = {4, 2, 4, 4, 1};
int dir[6][4] = {{1,0,0,0},{1,0,1,0},{1,0,0,1},{1,0,1,1},{1,1,1,1}}; //E,S,W,N

int n, m, c=0;
int global_danger;

vector<pair<int, int> > cctv;

void room_check(int cnt, int danger, vector< vector<int> > room){

    //last cctv
    if(cnt == c){
       /* cout <<"-------"<<cnt<<"--------"<<endl;
        cout<<"danger" <<danger<<endl;
        for(int i=0; i<n; ++i){
            for(int j=0; j<m; ++j){
                cout<<room[i][j]<<" ";
            }
            cout<<endl;
        }*/

        global_danger = min(danger, global_danger);
        return;
    }

    int cctv_x = cctv[cnt].first;
    int cctv_y = cctv[cnt].second;
    int cctv_type = room[cctv_x][cctv_y]-1;

    for(int i=0; i<rotation[cctv_type]; ++i){
        int local_danger = danger;
      //  cout<<"rotate " << i << endl;
        vector< vector<int> > local_room(room);

        for(int j=0; j<4; ++j){
        //    cout <<"dir "<<(j+i)%4<<endl;
            if(dir[cctv_type][(j+i)%4] == 1){
                if(j == 0){
                    for(int k=cctv_y+1; k<m; ++k){
                        if(local_room[cctv_x][k]==6)
                            k=m;
                        else{
                            if(local_room[cctv_x][k]==0){
                                local_room[cctv_x][k] = 7;
                                local_danger--;
                            }
                        }
                    }
                }else if(j == 1){
                    for(int k=cctv_x+1; k<n; ++k){
                        if(local_room[k][cctv_y]==6)
                            k=n;
                        else{
                            if(local_room[k][cctv_y]==0){
                                local_room[k][cctv_y] = 7;
                                local_danger--;
                            }
                        }
                    }
                }else if(j == 2){
                     for(int k=cctv_y-1; k>=0; --k){
                        if(local_room[cctv_x][k]==6)
                            k=-1;
                        else{
                            if(local_room[cctv_x][k]==0){
                                local_room[cctv_x][k] = 7;
                               local_danger--;
                            }
                        }
                    }
                }else if(j == 3){
                    for(int k=cctv_x-1; k>=0; --k){
                        if(local_room[k][cctv_y]==6)
                            k=-1;
                        else{
                            if(local_room[k][cctv_y]==0){
                                local_room[k][cctv_y] = 7;
                                local_danger--;
                            }
                        }
                    }
                }
            }
        }
        //if(local_danger < global_danger)
        room_check(cnt+1, local_danger, local_room);
    }
}

int main()
{
    vector< vector<int> > room;
    cin >>n >> m;
    int v;
    int danger = m*n;

    for(int i=0; i<n; ++i){
        vector<int> row;
        for(int j=0; j<m; ++j){
            cin >> v;
            row.push_back(v);

            if(v > 0 && v <6){
                cctv.push_back(make_pair(i,j));
                c++;
                danger--;
            }else if(v == 6)
                danger--;
        }
        room.push_back(row);
    }
    global_danger = danger;
    room_check(0, danger, room);
    cout << global_danger<<endl;
    //return 0;
}
