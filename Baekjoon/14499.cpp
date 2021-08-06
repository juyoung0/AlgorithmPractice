#include <iostream>
#include<fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <cstdio>
using namespace std;
int mymap[20][20];
int order[1000];

class Dice{
    public:
        void set_value(int v){
            this->value = v;
        }
        int get_value(){
            return this->value;
        }
        Dice(){value = 0;}
    private:
        int value;
};

Dice dice_map[6];
Dice dice1, dice2, dice3, dice4, dice5, dice6;

void init_dice(){
    dice_map[0]=dice1;
    dice_map[1]=dice2;
    dice_map[2]=dice3;
    dice_map[3]=dice4;
    dice_map[4]=dice5;
    dice_map[5]=dice6;
}

int roll_dice(int m, int n, int x, int y, int k){
    Dice *dice = &dice_map[5]; //초기 바닥에는 dice6이 놓여있
    Dice temp;
    for(int i=0; i<k; ++i){

        switch(order[i]){
        case 1:
            if(y<n-1){
                temp = dice_map[0];
                dice_map[0] = dice_map[3];
                dice_map[3] = dice_map[5];
                dice_map[5] = dice_map[2];
                dice_map[2] = temp;
                dice = &dice_map[5];
                y += 1;
                cout<<dice_map[0].get_value();
                if(i<k-1){
                    cout <<'\n';
                }

        if(mymap[x][y]==0){
            mymap[x][y] = dice->get_value();
            //dice->set_value(0);
        }else{
            dice->set_value(mymap[x][y]);
            mymap[x][y] = 0;
        }
            }
            break;
        case 2:
            if(0<y){
                temp = dice_map[0];
                dice_map[0] = dice_map[2];
                dice_map[2] = dice_map[5];
                dice_map[5] = dice_map[3];
                dice_map[3] = temp;
                dice = &dice_map[5];
                y -= 1;
                cout<<dice_map[0].get_value();
                if(i<k-1){
                    cout <<'\n';
                }

        if(mymap[x][y]==0){
            mymap[x][y] = dice->get_value();
            //dice->set_value(0);
        }else{
            dice->set_value(mymap[x][y]);
            mymap[x][y] = 0;
        }
            }
            break;

        case 3:
            if(0<x){
                temp = dice_map[0];
                dice_map[0] = dice_map[4];
                dice_map[4] = dice_map[5];
                dice_map[5] = dice_map[1];
                dice_map[1] = temp;
                dice = &dice_map[5];
                x -= 1;
                cout<<dice_map[0].get_value();
                if(i<k-1){
                    cout <<'\n';
                }

        if(mymap[x][y]==0){
            mymap[x][y] = dice->get_value();
            //dice->set_value(0);
        }else{
            dice->set_value(mymap[x][y]);
            mymap[x][y] = 0;
        }
            }
            break;

        case 4:
            if(m-1>x){
                temp = dice_map[0];
                dice_map[0] = dice_map[1];
                dice_map[1] = dice_map[5];
                dice_map[5] = dice_map[4];
                dice_map[4] = temp;
                dice = &dice_map[5];
                x += 1;
                cout<<dice_map[0].get_value();
                if(i<k-1){
                    cout <<'\n';
                }

        if(mymap[x][y]==0){
            mymap[x][y] = dice->get_value();
            //dice->set_value(0);
        }else{
            dice->set_value(mymap[x][y]);
            mymap[x][y] = 0;
        }
            }
            break;

        }


    }
}

int main(int argc, char *argv[]) {

   // ifstream inFile;
  //  ofstream outFile;
    int m, n, x, y, k;
    init_dice();
  //  freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);

    cin>> n >> m >>x >>y >>k;
    for (int i = 0; i < n; ++i) {
        for (int j=0; j < m; ++j){
            cin >> mymap[i][j];
        }
    }

    for (int j=0; j<k; ++j){
        cin >> order[j];
    }

    roll_dice(n, m, x, y, k);

   // inFile.close();
    //outFile.close();
    return 0;
}
