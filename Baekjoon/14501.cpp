#include <iostream>
#include <algorithm>

using namespace std;
int maxval=0;
int val=0;
int *work, *pay, n, ans;
int *maxlist; //for memorizatin

void dfs(int day){
    int i = day;

    if(i+work[i]-1<=n){
        maxval = pay[i];

        i = i+work[i];

        if(i <=n ){ //finish day
            maxval += maxlist[i];
        }

    }
}

int main()
{
    cin >> n;
    //duration, reward
    work = new int[n+1];
    pay = new int[n+1];
    ans = 0;
    maxval = 0;
    maxlist = new int[n+1];

    for(int i=1; i<=n; i++){
        cin >> work[i] >> pay[i];
    }

    if(work[n]==1)
        maxlist[n]=pay[n];
    else
        maxlist[n]=0;

    for(int i=n;i>=1;i--)
	{
        dfs(i);
        maxlist[i]=maxval;

        if(maxval>ans)
            ans = maxval;
        else
            maxlist[i]=ans;

        maxval = 0;
      //  val = 0;
	}

    cout << ans;

    return 0;
}
