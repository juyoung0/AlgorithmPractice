#include <iostream>

using namespace std;
int dp[10001][3];

int main()
{
    int n;
    cin>>n;
    int cup[n+1];

    for(int i=1; i<=n; i++){
        cin>>cup[i];
    }

    dp[1][0]=0;
    dp[1][1]=cup[1];
    dp[1][2]=cup[1];
    dp[2][0]=cup[1];
    dp[2][1]=cup[1]+cup[2];
    dp[2][2]=cup[2];
    dp[3][0]=cup[1]+cup[2];
    dp[3][1]=cup[2]+cup[3];
    dp[3][2]=cup[1]+cup[3];


    for(int j=3; j<=n; j++){
        //not drink n cup (max of n-1 cup)
        dp[j][0]=max(max(dp[j-1][0],dp[j-1][1]),dp[j-1][2]);
        //drink n-1, n cup and max of n-3 cup
        dp[j][1]=max(max(dp[j-3][0],dp[j-3][1]),dp[j-3][2])+cup[j-1]+cup[j];
        //drink n cup and max of n-2 cup
        dp[j][2]=max(max(dp[j-2][0],dp[j-2][1]),dp[j-2][2])+cup[j];
    }
    cout<<max(max(dp[n][0],dp[n][1]),dp[n][2]);
    return 0;
}
