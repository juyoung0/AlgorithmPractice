#include <bits/stdc++.h>

using namespace std;
int n, m, cnt=0;
int city[51][51];
int global_min=9999;
vector<vector<int> > dist;
vector<pair<int, int> > chicken;
vector<pair<int, int> > house;

int get_local_min(vector<pair<int, int> > c_list){
    int total_dist=0, min_dist=9999, diff=0;
    for(int h=0; h<house.size(); ++h){
        min_dist=9999;
        for(int c=0; c<c_list.size(); ++c){
            diff = abs(c_list[c].first-house[h].first)+abs(c_list[c].second-house[h].second);
           // cout<<"house " << h+1<<" : " <<diff<<endl;
            min_dist = min(min_dist, diff);
        }
        //cout<<"house " << h+1<<" min : " <<min_dist<<endl;
        total_dist += min_dist;
    }
    return total_dist;
}

void dfs(int store, vector<pair<int, int> > c_list, int cnt){
    int local_min=9999;

    if(store < chicken.size() && cnt<=m){
        local_min = get_local_min(c_list);
        //cout<<"store : "<<store<<", cnt : " <<cnt << ", local min : " <<local_min<<endl;
        if(global_min>local_min)
            global_min=local_min;

        if(store+1==chicken.size() && cnt==0){

        }else
            dfs(store+1, c_list, cnt);
        c_list.push_back(chicken[store+1]);
        dfs(store+1, c_list, cnt+1);
    }
}

int main()
{
    int store=0;
    vector<pair<int, int> > c_list;
    cin >>n >> m;
    for(int i=1; i<=n; ++i){
        for(int j=1; j<=n; ++j){
            cin >> city[i][j];
            if(city[i][j]==2)
                chicken.push_back(make_pair(i,j));
            else if(city[i][j]==1)
                house.push_back(make_pair(i,j));
        }
    }
    dfs(store, c_list, cnt);
    c_list.push_back(chicken[store]);
    dfs(store, c_list, cnt+1);
    cout << global_min;
}
