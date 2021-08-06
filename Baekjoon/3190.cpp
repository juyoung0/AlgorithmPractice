#include <iostream>
#include<fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <cstdio>
#include <queue>
bool apple[101][101]; //true, false
std::queue<std::pair<int, char> > turn; //0:no, 1:left, 2:right
bool snake[101][101]; //true, false
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int n=0;
int x=1, y=1;
std::queue<std::pair<int,int> > snake_body;

using namespace std;

bool move_snake(int heading){
    int next_x = x+dx[heading];
    int next_y = y+dy[heading];
    int tail_x, tail_y;
    if(next_x>0 && next_x<=n &&next_y>0 &&next_y<=n){
        if(snake[next_x][next_y]==false){
            x = next_x;
            y = next_y;
            snake[x][y]=true;
            snake_body.push(make_pair(x,y));

            if(apple[x][y]==true){ //eat apple;
                apple[x][y]=false;
            }else{  //remove tail

                tail_x = snake_body.front().first;
                tail_y = snake_body.front().second;
                snake[tail_x][tail_y] = false;
                snake_body.pop();
            }
        }else{ //die
            return false;
        }
    }else{ //die
        return false;
    }
    return true;
}

int start_count(){
    int sec=1;
    int heading = 0; //0:E, 1:S, 2:W, 3:N
    int success = false;

    while(true){
        success = move_snake(heading);

        if(success){
            if(!turn.empty() && turn.front().first==sec){
                if(turn.front().second==1){ //turn left
                    heading = (heading+3)%4;
                }else{ //turn right
                    heading = (heading+1)%4;
                }
                turn.pop();
            }
            sec+=1;
        }else{
            break;
        }

    }
    return sec;
}

int main()
{
    int k, apple_x, apple_y;
    cin>> n >> k;

    //initialize
    for (int i=0; i<101; ++i){
        for(int j=0; j<101; ++j){
            apple[i][j] = false;
            snake[i][j] = false;
        }
    }

    for (int i = 0; i < k; ++i) {
        cin >> apple_x >> apple_y;
        apple[apple_x][apple_y] = true;
    }
    snake[1][1]=true;
    snake_body.push(make_pair(1,1));

    int l, time;
    char direction;

    cin >>l;

    for(int i=0; i<l; ++i){
        cin >> time;
        cin >> direction;
        if(direction=='L')
            turn.push(make_pair(time,1));
        else
            turn.push(make_pair(time,2));
    }

    cout <<start_count();

    return 0;
}
