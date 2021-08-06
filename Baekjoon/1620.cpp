#include <iostream>
#include <string.h>
#include <map>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>


using namespace std;

int main()
{
    int n, q;
    cin >> n >> q;
    //input :name, output0 :key
    map<string, int> m;
    map<int, string> m2;
    //input :key, output: name
    char name[22];
    char query[22];

    for(int i=0; i<n; i++){
        scanf("%s", name);
        m[name]=i+1;
        m2[i]=name;
    }


    for(int j=0; j<q; j++){
        scanf("%s", query);
        if(isdigit(query[0])){
            printf("%s\n", m2[atoi(query)-1].c_str());
        }else{
            printf("%d\n", m[query]);
        }
    }
    return 0;
}
