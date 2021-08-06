#include <bits/stdc++.h>

using namespace std;

#define MIN 3
#define MAX 20

int matrix[MAX][MAX];
int visited[MAX][MAX];
int safeArea = 0;
int n, m;
int first=0;
queue< pair<int, int> > virusPos;
queue< pair<int, int> > infected;
pair<int, int> dir[] = {make_pair(-1,0),make_pair(0,1),make_pair(1,0),make_pair(0,-1)};

void bfs(int x, int y){
    visited[x][y] = 2;
    int posx=x, posy=y;
    for(int i=0; i<4; i++){
        posx+=dir[i].first;
        posy+=dir[i].second;
        if(0<=posx && posx<n && 0<=posy && posy<m){
            if(visited[posx][posy]==0){
                bfs(posx, posy);
            }
        }
        posx-=dir[i].first;
        posy-=dir[i].second;
    }
}
//virus spread, max : max various area
int virusSpread(){
    int safety = 0;
    queue< pair<int, int> > tempPos = virusPos;
    pair<int, int> vPos;
    vPos = virusPos.front();

    //virus spread from each position
    while(virusPos.size()>0){
        virusPos.pop();

        bfs(vPos.first, vPos.second);

        /*
        if(new_min > minV){
            virusPos = tempPos;
            return -1;
        }
        */
        vPos = virusPos.front();
    }
    //remake queue
    virusPos = tempPos;
    for(int i=0; i < n; i++){
        for(int j=0; j < m; j++){
            if(visited[i][j] == 0)
                safety+=1;
        }
    }
    return safety;
}

//dfs
void makeWall(int x, int y, int wallNum){
    int tempArea = 0;

    if(wallNum==3){
        for(int i=0; i < n; i++){
            for(int j=0; j < m; j++){
                visited[i][j] = matrix[i][j];
            }
        }

        tempArea = virusSpread();
/*
            if(first<5){
                for(int i=0; i < n; i++){
                    for(int j=0; j < m; j++){
                        cout << visited[i][j];
                    }
                    cout<<endl;
                }
                cout<<"safeArea is " <<safeArea<<endl;
                cout<<"================="<<endl;
                first += 1;
            }*/
        if(tempArea > safeArea){
            safeArea = tempArea;

        }
        return;
    }

    //first wall (x,y) then next make wall
    for(int i=x; i<n; i++){
        if(y<m){
            for(int j=y; j<m; j++){
                if(matrix[i][j]==0){
                    matrix[i][j]=3;
                    makeWall(i,j,wallNum+1);
                    matrix[i][j]=0;
                }
            }
            y=0;
        }else{
            y=0;
        }
    }
    return;
}

int main()
{
    //freopen("input3.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    scanf("%d%d", &n, &m);

    for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> matrix[i][j];
			if(matrix[i][j] == 2)
                    virusPos.push(make_pair(i, j));
		}
	}

    makeWall(0, 0, 0);

    cout << safeArea;

    return 0;
}
