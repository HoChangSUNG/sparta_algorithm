class LinkedTuple :
    def __init__(self):
        self.items=list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k ==key :
                return v
    def getvalues(self,key):
        values=[]
        for k, v in self.items :
            if(k==key) :
                values.append(v)
        return values
class LinkedDict:
    def __init__(self):
        self.items=[]
        for i in range(8) :
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key)%len(self.items)
        self.items[index].add(key, value)

    def get(self, key) :
        index = hash(key)%len(self.items)
        return self.items[index].get(key)

    def getvalues(self,key):
        index = hash(key)%len(self.items)
        return self.items[index].getvalues(key)

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    linked_dict= LinkedDict()
    answer=[]
    genre_1=genres[0]
    genre_2=None

    for idx in range(len(genres)) : #genre 결정 및 dictionary에 입력
        linked_dict.put(genres[idx], plays[idx])
        if genre_1 != genres[idx] and genre_2 is None :
            genre_2 = genres[idx]

    # print(genre_1,genre_2)

    genre_1_play=linked_dict.getvalues(genre_1) #genre_1의 재생횟수 리스트 반환
    genre_2_play=linked_dict.getvalues(genre_2) #genre_2의 재생횟수 리스트 반환
    genre_1_play.sort(reverse=True) #genre_1의 재생횟수 리스트 내림차순 정렬
    genre_2_play.sort(reverse=True)#genre_2의 재생횟수 리스트 내림차순 정렬

    if genre_1_play[0] > genre_2_play[0] : #많이 재생된 장르가 genre_1일 경우
        for i in range(len(genre_1_play)) :
            if i>1 : #노래 개수가 2개 이상일 때
                break
            answer.append(plays.index(genre_1_play[i]))
        for i in range(len(genre_2_play)) :
            if i >1 : #노래 개수가 2개 이상일 때
                break
            answer.append(plays.index(genre_2_play[i]))
    else : #많이 재생된 장르가 genre_2일 경우
        for i in range(len(genre_2_play)) :
            if i>1 : #노래 개수가 2개 이상일 때
                break
            answer.append(plays.index(genre_2_play[i]))
        for i in range(len(genre_1_play)):
            if i>1 : #노래 개수가 2개 이상일 때
                break
            answer.append(plays.index(genre_1_play[i]))

    return answer
print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!