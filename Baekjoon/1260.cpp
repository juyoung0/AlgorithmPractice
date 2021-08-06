#include <iostream>
#include <stack>
#include <queue>
#include <stdio.h>
#include <algorithm>

using namespace std;

vector<int> *adj;
int* visited;
int* visited2;
stack<int> vstack;
queue<int> vqueue;

//use stack
void dfs(int v){
    int curr_v;
    visited[v]=1;
    vstack.push(v);
    cout << v <<" ";


    //while(!vstack.empty()){
    curr_v = vstack.top();
    vstack.pop();
    for(int i=0; i<adj[curr_v].size(); i++){
        if(visited[adj[curr_v][i]]==0){
            //visited[adj[curr_v][i]]=1;
            //vstack.push(adj[curr_v][i]);
            //cout << adj[curr_v][i] <<" ";
            dfs(adj[curr_v][i]);
        }
    }
   // }
}

//use queue
void bfs(int v){
    int curr_v;
    if(visited2[v]==0){
        visited2[v]=1;
        vqueue.push(v);
        cout << v <<" ";
    }

    while(!vqueue.empty()){
        curr_v = vqueue.front();
        vqueue.pop();
        for(int i=0; i<adj[curr_v].size(); i++){
            if(visited2[adj[curr_v][i]]==0){
                visited2[adj[curr_v][i]]=1;
                vqueue.push(adj[curr_v][i]);
                cout << adj[curr_v][i] <<" ";
            }
        }
    }
}

int main()
{
    int v, e, start, v1, v2;
    scanf("%d %d %d", &v, &e, &start);\
    adj = new vector<int>[v+1];
    visited = new int[v+1];
    visited2 = new int[v+1];
    for(int i=0; i<e; i++){
        scanf("%d %d", &v1, &v2);
        adj[v1].push_back(v2);
        adj[v2].push_back(v1);
    }

    //small number first
    for(int i=0; i<v; i++){
        sort(adj[i+1].begin(), adj[i+1].end());
        visited[i+1]=0;
        visited2[i+1]=0;
    }

    dfs(start);
    cout <<endl;
    bfs(start);

    return 0;
}
