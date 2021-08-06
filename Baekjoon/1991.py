node_num = int(input().split()[0])
node_list = {}
pre_list = []
in_list = []
post_list = []


def pre_order(node):
    if node != None:
        pre_list.append(node)
        pre_order(node_list[node]["left"])
        pre_order(node_list[node]["right"])


def in_order(node):
    if node != None:
        in_order(node_list[node]["left"])
        in_list.append(node)
        in_order(node_list[node]["right"])


def post_order(node):
    if node != None:
        post_order(node_list[node]["left"])
        post_order(node_list[node]["right"])
        post_list.append(node)


for i in range(node_num):
    nodes = list(map(str, input().split()))
    node_list[nodes[0]] = {}
    if nodes[1] == ".":
        nodes[1] = None
    if nodes[2] == ".":
        nodes[2] = None
    node_list[nodes[0]]["left"] = nodes[1]
    node_list[nodes[0]]["right"] = nodes[2]

pre_order("A")
in_order("A")
post_order("A")

answer = ""
for n in pre_list:
    answer += n
print(answer)
answer = ""
for n in in_list:
    answer += n
print(answer)
answer = ""
for n in post_list:
    answer += n
print(answer)