#include <iostream>
#include<fstream>
#include <algorithm>
#include <vector>
#include <list>

using namespace std;
long long room[1000000];
long long sv=0;

long long count_sv(long long n, long long b, long long c){
    long long num=0, left;
    for (long long i=0; i<n; ++i){
        if(room[i]>b){
            num = (room[i]-b)/c;
            sv += num;
            left = room[i]-b-num*c;
            if(left > 0)
                sv += 1;
        }
    }
    return sv;
}

int main(int argc, char *argv[]) {

   // ifstream inFile;
   // ofstream outFile;
    long long n, b, c;
    long long room_size;
   // freopen("input.txt", "r", stdin);
   // freopen("output.txt", "w", stdout);

    scanf("%lld",&n);

    for (long long i = 0; i < n; ++i) {
        scanf("%lld", &room_size);
        room[i] = room_size;
    }
    scanf("%lld",&b);
    scanf("%lld",&c);

    sv += n;
    count_sv(n, b, c);

    printf("%lld", sv);

   // inFile.close();
   // outFile.close();
    return 0;
}
