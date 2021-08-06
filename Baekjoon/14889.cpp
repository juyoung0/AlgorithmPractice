#include <iostream>
#include <bits/stdc++.h>

using namespace std;
int skill[21][21];
int n=0;
/*next_permutation 순열 생성기 이용도 좋은 아이디어임!반은 0, 반은 1 */
int test_case(vector<int> team, int num, int start_sk, int link_sk, int start_mem, int link_mem){
    int min_diff1=100, min_diff2=100;
    int start_skill= start_sk, link_skill= link_sk;

    if(start_mem < n/2){
        team.push_back(1);
        for(int i=1; i<=num; ++i){
            // same team
            if(team[i]==1){
                start_skill += skill[i][num+1];
                start_skill += skill[num+1][i];
            }
        }
        min_diff1 = test_case(team, num+1, start_skill, link_sk, start_mem+1, link_mem);
        team.pop_back();
    }

    if(link_mem < n/2){
        team.push_back(2);
        for(int i=1; i<=num; ++i){
            // same team
            if(team[i]==2){
                link_skill += skill[i][num+1];
                link_skill += skill[num+1][i];
            }
        }
        min_diff2 = test_case(team, num+1, start_sk, link_skill, start_mem, link_mem+1);
    }

    if(num==n){
        return abs(start_skill - link_skill);
    }else{
        return(min(min_diff1, min_diff2));
    }
}

int main()
{
    vector<int> team; //1:start, 2:link
    int min_diff=100, min_diff1=100, min_diff2=100;

    cin >> n;
    team.push_back(0); //ignore index 0
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            cin >> skill[i][j];
        }
    }

    team.push_back(1);
    //team start
    min_diff1 = test_case(team, 1, 0, 0, 1, 0);
    team.pop_back();
    team.push_back(2);
    //team link
    min_diff2 = test_case(team, 1, 0, 0, 0, 1);

    min_diff = min(min_diff1, min_diff2);

    cout << min_diff << endl;
    return 0;
}
