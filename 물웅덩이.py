n, m = map(int, input().split()) # n과 m 입력받기
graph = [] # graph 리스트 선언 ( 맵 )
for i in range(n): # n 번 반복
    graph.append(list(map(int, input()))) # 맵 입력받기

def puddle(x, y): # puddle 함수
    if x <= -1 or x >= n or y <= -1 or y >= m: # 만약 x좌표 또는 y좌표가 맵 공간을 벗어나면
        return False # False 반환
    if graph[x][y] == 0: # 만약 해당 좌표가 물웅덩이라면
        graph[x][y] = 1 # 해당 좌표는 탐색됐으니 1로 변환시킴
        puddle(x - 1, y) # 해당 좌표로부터 동, 서, 남, 북 모두 탐색
        puddle(x, y - 1) # puddle 함수 내에서 재귀하면 cnt 값 증감 없이
        puddle(x + 1, y) # 한 물웅덩이를 모두 1로 만들 수 있음.
        puddle(x, y + 1)
        return True # True 를 반환하여 물웅덩이 값 + 1
    return False # 해당 좌표가 물웅덩이가 아니면 False 반환

cnt = 0 # 물웅덩이의 개수를 저장하는 변수 선언
for i in range(n): # 맵의 모든 좌표를 한번씩 다 방문함
    for j in range(m):
        if puddle(i, j): # 만약 물웅덩이가 나왔다면
            cnt += 1 # 물웅덩이 개수 + 1
print(cnt) # 물웅덩이의 개수 출력