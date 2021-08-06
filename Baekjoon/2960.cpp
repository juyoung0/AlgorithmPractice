//에라토스테네스의 체

#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int eratos(int n, int k){
    int nums[n];
    vector<int> erased;

    for(int i=0; i<n; i++){
        nums[i]=i+1;
    }

    for(int j=0; j<n; j++){
        if(nums[j]==1){
            continue;
        }
        if(nums[j]==0){
            continue;
        }

        for(int l=j+1; l<=n; l+=(j+1)){
            if(nums[l-1]!=0){
                erased.push_back(nums[l-1]);
                nums[l-1]=0;
            }
        }
    }

    return erased[k-1];
}

int main()
{
    int n, k;
    cin >> n >>k;

    cout << eratos(n, k);

    return 0;
}
