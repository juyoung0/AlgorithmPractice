# 210823 : 풀이시간 23분

def check_word(word, type):
    if type == 0:
        if 48 <= ord(word) <= 57 or 97 <= ord(word) <= 122 or word == '-' or word == '_' or word == '.':
            return True
        else:
            return False
    if type == 1:
        if 48 <= ord(word) <= 57 or 97 <= ord(word) <= 122 or word == '-' or word == '_':
            return True
        else:
            return False


def solution(new_id):
    # step 1
    new_id = new_id.lower()
    # step 2, 3, 4
    temp = ''
    prev_dot_flag = False

    for i in range(len(new_id)):
        # step 4
        if len(temp) == 0 or i == len(new_id) - 1:
            if check_word(new_id[i], 1):
                temp += new_id[i]
        # step 2
        else:
            if check_word(new_id[i], 0):
                if check_word(new_id[i], 1):
                    temp += new_id[i]
                    prev_dot_flag = False
                else:
                    # step 3
                    if not prev_dot_flag:
                        temp += new_id[i]
                        prev_dot_flag = True
    # step 5, 6
    if len(temp) == 0:
        temp = 'a'
    elif len(temp) >= 16:
        temp = temp[:15]

    while temp[-1] == '.':
        temp = temp[:len(temp) - 1]

    # step 7
    if len(temp) <= 2:
        last = temp[-1]
        while len(temp) < 3:
            temp += last
    return temp


# 정규식 풀이
# import re
#
# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st

# 다른 풀이
# def solution(new_id):
#     answer = ''
#     # 1
#     new_id = new_id.lower()
#     # 2
#     for c in new_id:
#         if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
#             answer += c
#     # 3
#     while '..' in answer:
#         answer = answer.replace('..', '.')
#     # 4
#     if answer[0] == '.':
#         answer = answer[1:] if len(answer) > 1 else '.'
#     if answer[-1] == '.':
#         answer = answer[:-1]
#     # 5
#     if answer == '':
#         answer = 'a'
#     # 6
#     if len(answer) > 15:
#         answer = answer[:15]
#         if answer[-1] == '.':
#             answer = answer[:-1]
#     # 7
#     while len(answer) < 3:
#         answer += answer[-1]
#     return answer