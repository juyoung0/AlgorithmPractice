#include <iostream>

using namespace std;
int dp[1000001];

int main()
{
    int n, temp;
    cin >> n;
    dp[0]=0;
    dp[1]=0;
    dp[2]=1;
    dp[3]=1;

    for(int i=4; i<=n; i++){
        dp[i]=dp[i-1]+1;
        if(i%3==0){
            temp=dp[i/3]+1;
            if(temp<dp[i])
                dp[i]=temp;
        }
        if(i%2==0){
            temp=dp[i/2]+1;
            if(temp<dp[i])
                dp[i]=temp;
        }
    }
    cout << dp[n];
    return 0;
}
