#include <iostream>

using namespace std;
int dp[10001][2];

int main()
{
    int n;
    cin>>n;
    int stair[n+1];

    for(int i=1; i<=n; i++){
        cin>>stair[i];
    }

    dp[1][0]=stair[1];
    dp[2][0]=stair[1]+stair[2];
    dp[2][1]=stair[2];

    for(int j=3; j<=n; j++){
        dp[j][0]=dp[j-1][1]+stair[j];
        dp[j][1]=max(dp[j-2][0],dp[j-2][1])+stair[j];
    }

    cout <<max(dp[n][0],dp[n][1]);
    return 0;
}
