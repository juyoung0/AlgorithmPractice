#include <bits/stdc++.h>

using namespace std;

int world[51][51];
int visited[51][51];
int dx[4]={1, 0, -1, 0};
int dy[4]={0,1,0,-1};
int n, L, R;
int moving=0;
int num_union=0;
bool moved = true;

void bfs(int i, int j){
    int curr_i, curr_j, next_i, next_j, diff, people;
    vector<pair<int,int> > unify;
    queue<pair<int,int> > vqueue;
    vqueue.push(make_pair(i,j));
    unify.push_back(make_pair(i,j));
    visited[i][j] = num_union;
    people = world[i][j];

    while(!vqueue.empty()){
        curr_i = vqueue.front().first;
        curr_j = vqueue.front().second;
        vqueue.pop();
        for(int k=0; k<4; ++k){
            next_i = curr_i +dx[k];
            next_j = curr_j +dy[k];
            if(next_i>=1 &&next_i <=n &&next_j>=1 &&next_j<=n && visited[next_i][next_j]==0){
                diff = abs(world[curr_i][curr_j]-world[next_i][next_j]);
                if(diff>=L && diff<=R){
                    moved = true;
                    visited[next_i][next_j] = num_union;
                    vqueue.push(make_pair(next_i,next_j));
                    unify.push_back(make_pair(next_i,next_j));
                    people += world[next_i][next_j];
                }
            }

        }
    }
    for(int l=0; l<unify.size(); ++l){
        world[unify[l].first][unify[l].second] = people/unify.size();
    }
}

void start_moving(){
    while(moved){
        moved = false;
        for(int i=1; i<=n; ++i){
            for(int j=1; j<=n; ++j){
                if(visited[i][j]==0){
                    num_union+=1;
                    bfs(i,j);
                }
            }
        }
        if(moved)
            moving+=1;
        num_union=0;
        for(int i=1; i<=n; ++i){
            for(int j=1; j<=n; ++j){
                visited[i][j]=0;
            }
        }
    }
}

int main()
{
    cin >>n >> L>>R;
    for(int i=1; i<=n; ++i){
        for(int j=1; j<=n; ++j){
            cin >> world[i][j];
            visited[i][j]=0;
        }
    }
    start_moving();
    cout << moving;
    return 0;
}
