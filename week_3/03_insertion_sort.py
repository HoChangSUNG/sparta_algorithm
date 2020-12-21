input = [4, 6, 2, 9, 1]
# 1단계 [4 6 2 9 1]
#        <-
# 2단계 [4 6 2 9 1]
#        <-<-
# 3단계 [2 4 6 9 1]
#        <-<-<-
# 4단계 [2 4 6 9 1]
#        <-<-<-<-
# 결과   [1 2 4 6 9]

# for i in range(1,5) :
#     for j in range(i):
#         print(i-j)
# insertion_sort는 bubble_sort,selection_sort보다 조금마한 시간복잡도 이득을 볼 수 있음
# break문이 있기 때문.
# 만약 거의 정렬된 배열이 들어온다면 최대 O(N)만큼의 시간 복잡도만 가질수도 있음
def insertion_sort(array): #O(N^2)
    n=len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i-j-1]>array[i-j] :
                array[i - j - 1],array[i-j]=array[i-j],array[i - j - 1]
            else :
                break


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!