#include <bits/stdc++.h>

using namespace std;

vector<vector<int> > gear;
vector<int> rotated;
vector<int> north_idx;
vector<pair<int, int> > turn; //gear number, direction
queue<pair<int, int> > next_rotate;
int cnt=0;

void rotate_gear(int loc, int dir){
    if(dir==1)
        north_idx[loc-1] = (north_idx[loc-1]+7)%8;
    else
        north_idx[loc-1] = (north_idx[loc-1]+1)%8;
  //  cout<<"loc idx changed to "<<north_idx[loc-1]<<endl;
}

void check_gear(){
    while(!next_rotate.empty()){
        int loc=next_rotate.front().first, dir=next_rotate.front().second;
    //    cout<<"turn gear : "<<loc<<", dir : " <<dir<<endl;
        rotated[loc-1] = 1;
        next_rotate.pop();

        if(loc!=1){ //check left
            if(gear[loc-1][(north_idx[loc-1]+6)%8]!=gear[loc-2][(north_idx[loc-2]+2)%8] && rotated[loc-2]==0){
                if(dir==1)
                    next_rotate.push(make_pair(loc-1, -1));
                else
                    next_rotate.push(make_pair(loc-1, 1));
            }
        }
        if(loc!=4){ //check right
             if(gear[loc-1][(north_idx[loc-1]+2)%8]!=gear[loc][(north_idx[loc]+6)%8] && rotated[loc]==0){
                if(dir==1)
                    next_rotate.push(make_pair(loc+1, -1));
                else
                    next_rotate.push(make_pair(loc+1, 1));
            }
        }

        rotate_gear(loc, dir);
    }
}

int main()
{
    int num, m, loc, dir;
    string nums;
    for(int i=0; i<4; ++i){
        vector<int> local_gear;
        rotated.push_back(0);
        north_idx.push_back(0);
        cin >> nums;
        for(int j=0; j<8; ++j){
            local_gear.push_back(int(nums[j])-48);
        }
        gear.push_back(local_gear);
    }
    cin >> m;
    for(int i=0; i<m; ++i){
        cin >> loc >> dir;
        turn.push_back(make_pair(loc, dir));
    }

    for(int i=0; i<m; ++i){
     //   cout<<"======"<<endl;
        next_rotate.push(turn[i]);
        check_gear();
        for(int j=0; j<4; ++j)
        rotated[j] = 0;
    }

    int sum=0;
    for(int i=0; i<north_idx.size(); ++i){
     //   cout<<"gear : " << i+1 <<" val is  "<<gear[i][north_idx[i]]<<endl;
        if(gear[i][north_idx[i]]==1)
            sum += pow(2, i);
    }
    cout <<sum;
}
