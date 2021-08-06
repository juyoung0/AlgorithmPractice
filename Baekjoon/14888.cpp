#include <bits/stdc++.h>
using namespace std;

int n;
long long max_val=-1000000000, min_val=1000000000;
vector<int> number;
vector<int> opt; //+:1, -:2, x:3, /:4

void calcul(){
    long long local_val = number[0];
    for(int i=0; i<opt.size(); ++i){
        switch(opt[i]){
        case 1:
            local_val += number[i+1];
            break;
        case 2:
            local_val -= number[i+1];
            break;
        case 3:
            local_val *= number[i+1];
            break;
        case 4:
            local_val /= number[i+1];
            break;
        }
    }
    if(local_val>max_val)
        max_val = local_val;
    if(local_val<min_val)
        min_val = local_val;
}

int main(){
	int num, m;
    cin >> n;
	for(int i=0; i<n; i++){
        cin >> num;
        number.push_back(num);
	}

    for(int i=1; i<5; i++){
        cin >> m;
        for(int j=0; j<m; ++j){
            opt.push_back(i);
        }
	}

	sort(opt.begin(), opt.end());


	do{
        calcul();
	}while(next_permutation(opt.begin(),opt.end()));

	cout << max_val << endl;
	cout << min_val;
}
