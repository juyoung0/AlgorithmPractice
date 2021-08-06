#include <bits/stdc++.h>

using namespace std;

int money17[] = {500,300,300,200,200,200,50,50,50,50,30,30,30,30,30,10,10,10,10,10,10};
int money18[] = {512, 256, 256, 128, 128, 128, 128, 64, 64, 64, 64, 64, 64, 64, 64, 32, 32, 32, 32, 32, 32, 32, 32,32, 32, 32, 32,32, 32, 32, 32};

int _main(int TEST){
    int rank17, rank18, sum=0;
    scanf("%d%d", &rank17, &rank18);
    if(rank17 <= 21)
        sum += money17[rank17-1];
    if(rank18 <= 31)
        sum += money18[rank18-1];

    return sum*10000;
}

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        //cerr << i << endl;
        //printf("Case #%d: ", i);
        cout <<_main(i) << endl;
    }
    return 0;
}
