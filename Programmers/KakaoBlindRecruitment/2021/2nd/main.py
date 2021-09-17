from lib.restapi import API
import datetime

class Simulator():
    def __init__(self, url, token, problem):
        self.api = API(url, token)
        self.api.get_start(problem)
        self.status = "ready"
        self.time = 0
        self.dir = True
        if problem == 1:
            self.truck_n = 5
            self.mean_n = 4
            self.garage_n = 5
        else:
            self.truck_n = 10
            self.mean_n = 3
            self.garage_n = 60
        self.garage = []  # [(i, 0) for i in range(5*5)]
        self.truck = [{'location': -1, "bikes": 0} for _ in range(self.truck_n)]

    def get_location(self):
        res = self.api.get('/locations')
        self.garage = []
        for r in res['locations']:
            self.garage.append((r['id'], r['located_bikes_count']))
        return res

    def get_truck(self):
        res = self.api.get('/trucks')
        for r in res['trucks']:
            self.truck[r['id']]['location'] = r['location_id']
            self.truck[r['id']]['bikes'] = r['loaded_bikes_count']
        return res

    def get_score(self):
        res = self.api.get('/score')
        return res['score']

    def put_simulate(self, data):
        res = self.api.put('/simulate', data)
        self.status = res['status']
        self.time = res['time']
        return res

    def find_route(self, t, s, f):
        # s에서 f로 가는 경로 찾기 (가는 길에 킥보드가 많은 장소에서 수거한다)
        route = []
        cnt = 0
        max_val, max_loc, max_i = -1, -1, -1
        #s < f 면 오른쪽으로 가거나, 위로 가거나
        #s > f 면 왼쪽으로 가거나, 아래쪽으로 가거나
        #s == f면 경로 반환
        while s != f:
            cnt += 1
            if max_val < self.garage[s][1]:
                max_val = self.garage[s][1]
                max_loc = s
                max_i = cnt
            if s < f:
                if f - s >= self.garage_n:
                    # 오른쪽으로 이동
                    route.append(2)
                    s += self.garage_n
                else:
                    # 위로 이동
                    route.append(1)
                    s += 1
            else:
                if s - f >= self.garage_n:
                    # 왼쪽으로 이동
                    route.append(4)
                    s -= self.garage_n
                else:
                    # 아래로 이동
                    route.append(3)
                    s -= 1

        # 만약 자전거를 싣거나 내릴수 없다면 다른 트럭을 보낸다
        if len(route) >= 10:
            return None
        elif len(route) == 9:
            # 만약 트럭에 자전거가 있다면 1대는 내릴 수 있다
            if self.truck[t]['bikes'] > 0:
                # 자전거를 하차한다
                route.append(6)
                return route
            else:
                return None

        # 트럭에 자전거가 있다면 목적지에 내려야 한다
        for i in range(self.truck[t]['bikes']):
            if len(route) <= 10:
                route.append(6)

        # 만약 60초 이내에 더 움직일 수 있다면 자전거 더 옮긴다 (최대 10번 명령 가능함)
        poss = self.garage[max_loc][1]
        if len(route) <= 8:
            if poss > 0:
                # 자전거가 많았던 장소에서 수거하도록함
                route.insert(max_i, 5)
                poss -= 1
                # 자전거를 하차한다
                route.append(6)

        return route

    def move_truck(self):
        print(self.time)
        command = { "commands": [] }

        # 수량 부족한 곳을 찾는다 (트럭갯수만큼)
        # 불균형 방지를 위해 매번 앞, 뒤 반대로 탐색해준다
        lack = sorted(self.garage, key=lambda x: x[0], reverse=self.dir)
        lack = sorted(lack, key=lambda x: x[1])[:self.truck_n]
        routes = {}

        route_cnt = [0 for _ in range(self.truck_n)]
        for l in lack:
            routes[l[0]] = [[] for _ in range(self.truck_n)]
            # 평균 자전거 갯수보다 적은 경우에만 재배치를 한다
            if l[1] < self.mean_n:
                for i, t in enumerate(self.truck):
                    route = self.find_route(i, t['location'], l[0])
                    if route:
                        routes[l[0]][i] = route
                        route_cnt[i] += 1

        # 각 장소별 트럭을 배치해준다
        for _routes in routes.values():
            min_i, min_r = -1, len(lack)
            # 갈 수 있는 경로가 적은 트럭부터 배치한다
            for i, _route in enumerate(_routes):
                if len(_route) > 0 and min_r >= route_cnt[i]:
                    min_i = i
                    min_r = route_cnt[i]

            if min_i != -1:
                # 트럭의 루트를 넣어주고, 다음에 배치되지 않도록 route_cnt를 높은 수로 지정해준다
                command['commands'].append({"truck_id": min_i, "command": _routes[min_i]})
                route_cnt[min_i] = len(lack) + 1

        print(routes)
        print(command)
        # command = {
        #     "commands": [
        #          { "truck_id": 0, "command": [2, 5, 4, 1, 6] },
        #          { "truck_id": 1, "command": [2, 5, 4, 1, 6] }
        #        ]
        # }

        return command

if __name__ == '__main__':
    url = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
    token = "dbe380885e47e8d412fc2fa5fb7cf336"
    simulator = Simulator(url, token, 1)
    cnt = 0
    now = datetime.datetime.now()
    print("Start : ", now)
    while simulator.status == "ready":
        cnt += 1
        simulator.get_location()
        simulator.get_truck()
        simulator.dir = not simulator.dir
        command = simulator.move_truck()
        simulator.put_simulate(command)
        # print(simulator.truck)
        # print(simulator.garage)

    print("Score : ", simulator.get_score())
    now = datetime.datetime.now()
    print("Finished : ", now)
