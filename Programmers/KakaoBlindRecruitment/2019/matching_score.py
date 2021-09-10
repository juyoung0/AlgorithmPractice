import re
from collections import defaultdict

### pages 에는 없지만, 링크 되고 되는 페이지가 있따?! 예외처리 필요하다!!!!!!
def solution(word, pages):
    page_dict = defaultdict(dict)
    # basic_scroe, link_from(외부링크수), link_to, self_link_score, link_score, match_score

    # html 페이지 파싱
    for i, page in enumerate(pages):
        url = re.search(r'<meta.+?content="(https://.+?)"', page, re.I | re.S).group(1)
        page_dict[url]['index'] = i
        page_dict[url]['basic_score'] = len(re.findall(r'(?<=[^a-xA-Z])'+str(word)+r'[^a-xA-Z]', page, re.I | re.S))
        page_dict[url]['link_to'] = re.findall(r'<a href="(https://.+?)">', page, re.I | re.S)
        if 'link_from' not in page_dict[url]:
            page_dict[url]['link_from'] = []

        for link in page_dict[url]['link_to']:
            if 'link_from' not in page_dict[link]:
                page_dict[link]['link_from'] = []
            page_dict[link]['link_from'].append(url)

    # link_score 계산
    highest_score = (0, 0) # (페이지 번호, link_score)
    for key in page_dict.keys():
        page = page_dict[key]
        link_score = 0
        if "link_to" in page:
            for link in page["link_to"]:
                if link in page_dict:
                    if "self_link_score" not in page_dict[link]:
                        # pages 에 포함되어 있지 않은 페이지 점수는 0으로 처리
                        if "basic_score" in page_dict[link]:
                            page_dict[link]["self_link_score"] = page_dict[link]["basic_score"] / len(page_dict[link]["link_from"])
                            link_score += page_dict[link]["self_link_score"]
            match_score = page["basic_score"] + link_score
            if match_score > highest_score[1]:
                highest_score = (page["index"], match_score)
    return highest_score[0]

print(solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]), 0)
print(solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]), 1)