#include <bits/stdc++.h>

using namespace std;
int n, m;
int matched[201];
int visited[201];
vector<vector<int> > hope;

bool dfs(int cow){
    if(cow==0)
        return true;

    if(visited[cow]==1)
        return false;

    visited[cow] = 1;

    vector<int> wish = hope[cow-1];

    for(int i=0; i<wish.size(); ++i){
        if(matched[wish[i]] != cow){
       //  cout <<"cow : "<<cow <<" wants " << wish[i]<<endl;
            if(matched[wish[i]]==0 || dfs(matched[wish[i]])){
                matched[wish[i]] = cow;
                return true;
            }
        }
    }
    return false;
}

int main()
{
    int k, temp;
    cin >>n>>m;
    for(int i=0; i<n; i++){
        vector<int> home;
        cin >> k;
        for(int j=0; j<k; ++j){
            cin >>temp;
            home.push_back(temp);
        }
        hope.push_back(home);
        visited[i+1] = 0;
    }

    for(int i=1; i<=m; ++i){
        matched[i] = 0;
    }
    for(int i=1; i<=n; ++i){
        for(int j=1; j<=n; ++j){
            visited[j] = 0;
        }
       // cout <<"dfs start : " << i <<endl;
        dfs(i);
    }
    int cnt=0;
    for(int i=1; i<=m; ++i){
        if(matched[i]!=0)
            cnt+=1;
    }

    cout << cnt << endl;
    return 0;
}
