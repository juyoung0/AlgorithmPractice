def solution(genres, plays):
    genre_list = list(set(genres))
    genre_ranking = {genre: 0 for genre in genre_list}
    album = {genre: [] for genre in genre_list}
    answer = []
    for i, play in enumerate(plays):
        genre = genres[i]
        genre_ranking[genre] += play
        album[genre].append((i, play))
        album[genre].sort(key=lambda x: x[1], reverse=True)
        album[genre] = album[genre][0:2]

    genre_ranking = sorted(genre_ranking.items(), key=lambda x: x[1], reverse=True)

    for genre in genre_ranking:
        answer.extend([x[0] for x in album[genre[0]]])
    return answer