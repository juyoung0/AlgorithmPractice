#include <iostream>
#include <stack>
#include <queue>
#include <stdio.h>
#include <algorithm>

using namespace std;

vector<int> *adj;
int* visited;
int* step;
queue<int> vqueue;


//use queue
void bfs(int v, int total){
    int curr_v;
    if(visited[v]==0){
        visited[v]=1;
        vqueue.push(v);
        step[0] = 1;
    }

    while(!vqueue.empty()){
        curr_v = vqueue.front();
        vqueue.pop();

        if(curr_v==total){
            cout << step[curr_v] << endl;
            break;
        }

        for(int i=0; i<adj[curr_v].size(); i++){
            if(visited[adj[curr_v][i]]==0){
                visited[adj[curr_v][i]]=1;
                vqueue.push(adj[curr_v][i]);
               // if(step[adj[curr_v][i]] > step[curr_v]+1)
                step[adj[curr_v][i]] = step[curr_v]+1;
            }
        }
    }
}

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);
    int maze[n][m];
    char s[m+1];
    adj = new vector<int>[n*m];
    visited = new int[n*m];
    step = new int[n*m];

    //get input
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            scanf("%1d", &maze[i][j]);
        }
    }

    //make graph (check 0 / 1)
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
                if(maze[i][j]!=0){
                    //way to down
                    if(i!=(n-1) && maze[i+1][j]==1){
                            adj[i*m+j].push_back((i+1)*m+j);
                    }
                    //way to right
                    if(j!=(m-1) && maze[i][j+1]==1){
                            adj[i*m+j].push_back(i*m+j+1);
                    }
                    //way to up
                    if(i!=0 && maze[i-1][j]==1){
                            adj[i*m+j].push_back((i-1)*m+j);
                    }
                    //way to left
                    if(j!=0 && maze[i][j-1]==1){
                            adj[i*m+j].push_back(i*m+j-1);
                    }
                }
        }
    }

    for(int i=0; i<n*m; i++){
        visited[i]=0;
        step[i]=0;
    }

    bfs(0, n*m-1);

    return 0;
}
