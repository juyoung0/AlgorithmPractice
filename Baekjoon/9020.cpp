//골드바흐

#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int *eratos(int n){
    int *nums = new int[n];

    for(int i=0; i<n; i++){
        nums[i]=i+1;
    }

    for(int j=0; j<n; j++){

        if(nums[j]==1){
            nums[j] = 0;
            continue;
        }
        if(nums[j]==0){
            continue;
        }

        for(int l=2*(j+1); l<=n; l+=(j+1)){
            if(nums[l-1]!=0){
                nums[l-1]=0;
            }
        }
    }

    return nums;
}

int goldbach(int n, int* primes){
    int p1, p2;
    p1 = n/2;
    p2 = n - p1;

    while(p1>1){

        if(primes[p1-1]!=0 && primes[p2-1]!=0)
            break;
        else{
            p1 -= 1;
            p2 += 1;
        }
    }
    cout <<p1 <<" " <<p2 <<endl;
    return 0;
}

int main()
{
    int n;
    int *primes;
    cin >> n;
    int nums[n];

    for(int i=0; i<n; i++)
        cin >> nums[i];


    for(int j=0; j<n; j++){
        primes = eratos(nums[j]);
        goldbach(nums[j], primes);
    }
    return 0;
}
