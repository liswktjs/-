# coding_study
## 📌 코딩 테스트 대비 알고리즘 study 

💻💻 사용할 언어: 파이썬, 자바스크립트

2021.08.27 지금까지 공부했던 자료구조 정리

> 그리드 알고리즘 

'현재 상황에서 가장 좋아보이는 것 선택', 매 순간 가장 좋아보이는 것을 선택하며 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않는다 

> 구현 알고리즘

완전탐색 '모든 경우의 수를 다 계산하는 해결 방법' , 시뮬레이션 '문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행하는 방식' 

> stack

선입후출(Fist In Last Out), 데이터가 쌓이는 형식의 구조로 처음으로 입력된 데이터는 맨 아래에 위치하고 마지막에 입력된 데이터는 맨 위에 놓여져 있다. 만약, 유저가 데이터를 하나 빼오고자 한다면, 마지막에 위치한 데이터를 제일 먼저 받아볼 수 있다.
- 파이썬에서의 구현 

파이썬에서는 리스트로 구현을 한다 stack = [] 

stack.append(데이터변수이름): 데이터 추가시 사용, 맨 뒤에 데이터가 추가 된다

statck.pop(): 데이터를 추출하고자 할 때 사용 맨뒤에 있는 데이터가 꺼내진다 /  stack.pop([::-1]) 일때에는 최상단(맨 앞)의 원소가 추출되게 된다 

> queue 

선입선출(First In Fisrt Out), 주로 대기줄에 비유되는 데이터 구조로 처음으로 입력된 데이터 뒤로 후에 입력되는 데이터들이 삽입된다. 만약, 유저가 데이터 하나를 빼고자 한다면 맨 앞(처음으로 삽입이 되었던) 데이터 부터 추출이 가능하다. 
- 파이썬에서의 구현 

파이썬에서는 queue를 구현하기 위해서 라이브러리를 사용한다 

from collection import deque : 라이브러리 추가 queue = deque() 로 queue 형태 데이터 자료구조 생성 

queue.append(데이터변수이름): 데이터 추가시 사용, 맨 뒤에 데이터가 추가 된다 

queue.popleft(): 맨 앞에 있는 데이터가 꺼내 진다 

🎈2021.08.28 DFS,BFS 개념정리 + 관련 인강듣고 구현 코드 짜보기
> DFS (Depth-Frist Search) 

깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다 DFS는 그래프 탐색을 위한 알고리즘인데 이때 그래프 탐색이란 하나의 노드를 시작으로 노드들을 방문하는 것을 말한다

*그래프 : 노드(Node)와 간선(Edge)로 표현되며 노드를 정점(Vertex)라고도 말한다. 

- 그래프를 파이썬에서 구현하는 방법 
1) 인접행렬 방식: 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식 /  
연결되어 있지 않은 노드끼리는 무한비용이라고 가정한다 

장점) 인접한 노드만을 저장하므로 메모리가 상대적으로 적게 소요된다 

단점) 특정한 두 노드가 연결되어 있는지에 대한 정보 획득이 느리다 

2) 인접리스트 방식: 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장한다 

장점) 모든 관계를 저장하므로 정보 획득이 빠르다 

단점) 노드 개수가 많을수록 메모리가 불필요하게 낭비될 수 있다 

- stack 활용한 DFS 동작과정 
: 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다 -> 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를한다 (만약 방문하지 않은 인접노드가 없다면 스택에서 최상단 노르를 꺼낸다) -> 앞선 과정을 더 이상 수행할 수 없을 때 까지 반복한다 

-> 데이터 개수가 N개인 경우 O(N)시간이 소요됨

> BFS (Breath First Search)

너비 우선 탐색, 멀리 있는 노드 부터 우선으로 탐색하는 DFS와 달리 가까운 노드부터 탐색하는 알고리즘이다 

- queue를 활용한 BFS 동작과정
: 탐색시작 노드를 큐에 삽입하고 방문처리를 한다 -> 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 한다 => 앞선 과정을 더 이상 수행할 수 없을 때까지 반복한다 

-> O(N)시간 소요 / 일반적인 경우 DFS보다는 수행시간이 더 좋은편이다 

😣 2021.09.01 이것이 코딩테스트다 with 파이썬 책에 있는 문제 풀이 

> 오늘 공부 한 것 중 자주 쓰일 것들 정리 

리스트 형태로 입력을 받을 때에  plans = input().split()

두개의 정수를 입력 받을 때에 n, m = map(int,input().split()) 

개수가 정해진 2차원 배열을 입력 받을 떄에 

for i in range(n):
  array.append(list(map(int,input().split())))
  
모든 원소의 값이 0으로 초기화된 2차원 배열을 만들 때 d = [[0] * m  for_ in range(n)]

> 지도나 체스판등의 2차원 배열의 형태를 지닌 곳에서 유저가 움직이는 문제들일때 

x, y를 통해서 초기 유저의 위치를 표기하고, dx, dy 각각 문제에서 제시되는 이동하는 방법에 대해서 배열을 만들어 

nx,ny라는 임시변수를 만들어 dx+x dy+y가 문제에서 제시되는 조건을 충족시키는지 확인한다 

👓 2021.09.02 dfs, bfs 그래프 직접 구현해보기 

> dfs 구현시 
1) 제시된 시작 노드를 방문 처리한다 
2) 시간 노드에 인접한 노드 중에서 

-> 방문하지 않은 노드가 있으면, 해당 노드를 스택에 push하고 방문처리를 한다 후에 2 방문 

-> 방문하지 않은 노드가 없다면, 스택에서 노드를 pop하여 방문하지 않은 인접 노드가 나오면 방문처리를 한다

3) 스택이 공백이 될 때 까지 2를 반복한다 

> 그래프 구현시 

list나 dict형태를 활용해서 구현이 가능하다 

📝 2021.09.03 bfs 예제문제 풀기 / 정렬 개념 정리

>  정렬알고리즘 

정렬 알고리즘이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다 
/ 데이터를 사전에 정렬해 두면 후에 이진 탐색이 가능해진다 

종류) 선택저렬, 삽입정렬, 퀵정렬, 계수 정렬 등이 있다 

> 선택 정렬 (Selection Sort) 

'가장 작은 것을 선택 한다'라는 아이디어를 기본으로 하는 알고리즘이다 

시간 복잡도

선택정렬은 첫번째 원소를 기준으로 다른 모든 원소와 비교를 하여 가장 작은 원소와 교체하는 방식으로 진행을 하기 때문에

만일 원소들이 순서대로 정렬이 되어 있는 배열이라도 최소 n-1번의 비교작업이 필요하다 

평균적으로 생각헤 볼 때에는 총 N (N + 1) / 2번의 연신아 수행된다 그러므로 빅오 표기법으로는 O(n^2)이다 

> 삽입 정렬 (Insertion Sort) 

데이터를 하나씩 확인하여 적절한 위치에 삽입시킨다 

시간 복잡도 

반복문이 2번 중첩되어 사용되므로 시간 복잡도는 O(n^2)이다 

만일 사전에 데이터가 거의 정려이 되어 있다면, O(N)이라는 시간 복잡도를 가질 수 있다 

🎬 2021.09.04 정렬 알고리즘 개념 정리 

> 퀵 정렬 (Quick Sort)

기준데이터(피봇Pivot)을 설정하고 원소들을 pivot과 비교해 작은 것과 큰 것을 비교해 원소 위치를 바꾼다 

pivot을 어떻게 설정 하냐에 따라서 방법이 조금 씩 바뀐다 

+ 첫번째 데이터를 pivot으로 설절하는 것을 호어분할 방식이라고 한다 

종료 조건은 pivot을 이용해 분류할 데이터의 개수가 1개일 때이다 

시간 복잡도 : 평균) O(NlogN)   최악일때) O(N^2)  

🥓 2021.09.05 퀵 알고리즘 구현

퀵알고리즘의 경우 피봇을 기준으로 데이터 리스트를 절반으로 나누어 다시 또 비교 작업을 통해서 나누는 방식으로 똑같은 작업이 진행된다 

같은 작업을 계속 반복되므로 재귀함수를 써야 구현하기가 쉽다 

그런데 아직 재귀적으로 코드를 구현하는 것이 어렵다 재귀적으로 코드를 짜는 연습이 필요하다

- 파이썬에서 리스트 원소 내림차순으로 정렬하는 방법 

: array = sorted(array, reverse=True) 

- 파이썬에서 리스트의 원소로 리스트나 튜플이 있을때 내림차순으로 정렬하는 방법

(*튜플: 튜플의 경우 한번 선언이 되면 변경이 불가능하다  ()를 사용하여 선언을 한다)

: result = sorted(array, key = lambda value: value[1], reverse=True) 

(*key=lambda value: value[1] 에서의 lambda는 람다 함수로 lambda 매개변수 : 결과(return 값) 이다) 

📈 2021.09.06 탐색 알고리즘 개념 정리

> 이진 탐색 (Binary Search)

배열의 원소들이 정렬이 되어 있어야 사용할 수 있는 알고리즘이다 

이진탐색의 경우 탐색 범위를 절반씩 좁혀가며 데이터를 탐색한다는 특징이 있다

+문제의 조건에서 데이터의 개수가 많을때 이진탐색을 우선적으로 고려해볼것!!

탐색의 기준이 되는 변수는 시작점, 중간점, 끝점으로 3가지 있다. 찾으려는 데이터와 중간점 위치에 있는 데이터를 비교하는 작업을 반복적으로 수행함으로써 원하는 데이터의 위치를 찾아낸다 

시간복잡도

한번 이진탐색을 진행할 때마다 탐색 대상이 되는 데이터의 개수가 절반씩 줄기 때문에 시간 복잡도는 O(logN)이다 

> 트리 자료 구조 

트리구조의 경우 대용량 데이터 처리에 적합하므로 주요 쓰인다 

이진 탐색 트리 
: 왼쪽 자식 노드의 값 < 부모노드의 값 < 오른쪽 자식 노드의 값 이 성립해야 이진 탐색 트리라고 할 수 있다 

> 파이썬에서 빠르게 정보를 입력받는법

: import sys

input_data = sys.stdin.readline().rstrip()

📁 2021.09.07 다이나믹 프로그래밍 개념정리 

> 다이나믹 프로그래밍 

: 이미 해결된 부분 문제에 대한 답을 저장한 후, 해당 문제에 대해서는 더 이상 해결을 진행하지 않고 반환한다 

다이나믹 프로그래밍으로 해결할 수 있는 문제 예시로 피보나치 수열이 있다.

피보나치 수열의 경우 재귀함수로 구현할 경우 n이 커지면 커질 수록 수행 시간이 기하급수적으로 늘어난다 

- 다이나믹 프로그래밍을 적용할 수 있는 문제 조건 

1) 큰 문제를 작은 문제로 나눌 수 있다 
2) 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다 

다이나믹 프로그래밍을 구현하는 방법 중 하나: 메모이제이션(한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법, 메모이제이션은 값을 저장하는 방법이므로 캐싱이라고도 한다)

- 시간복잡도 : O(N), 첫 단계에서 푼 결과가 다음 단계 풀이에 활용되고 한번 구한 결과는 다시 구해지지 않으므로 데이터 수가 늘어날 수록 복잡도가 증가하는 형태이다

- 다이나믹 프로그래밍 소스코드 작성하는 방법 

1) 탑다운 방식 (Top-Down) (=하향식): 재귀함수를 활용하여 작성하는 방법 
2) 보텀업 방식 (Bottom-Up) (=상향식): 반복물을 활용하여 작성하는 방법 

🩹 2021.09.08 다이나믹 프로그래밍(=동적 계획법), 분할정복 추가 공부 

> 다이나믹 프로그래밍(=동적 계획법)

: 입력 크기가 작은 부분 문제들을 해결한 후, 해당 부분 문제의 해를 활용해서 보다 큰 크기의 부분 문제를 해결 

상향식 접근법으로 memoization기법을 활용한다 

- 다이나믹 프로그래밍의 경우 작은 문제를 해결한 후 다음 문제를 해결해야하므로 보통 cache = [0 for index in range(100)] 식으로 0으로 초기화한 배열을 생성하여 값들을 해당 배열에 저장한다

> 분할 정복 

: 문제를 나눌 수 없을 때 까지 나누어서 각각을 풀어서 다시 합병하여 문제의 답을 얻는 알고리즘 

하향식 접근법으로 일반적으로 재귀 함수로 구현을 한다 

- 다이나믹 프로그래밍과 분할 정복 비교 

공통점: 문제를 쪼개서 가장 작은 단위로 분할한다 

차이점 : 동적계획법) 부분 문제는 중복되어 상위 문제 해결시 재활용 된다 / 메모이제이션 기법을 활용한다 

분할정복) 부분문제가 서로 중복되지 않고 메모이제이션 기법을 활용하지도 않는다 

🎹 2021.09.09 다이나믹 프로그래밍 연습문제, 최단경로 , 다익스트라 알고리즘개념 정리 

> 최단 경로 

가장 짧은 경로를 찾는 알고리즘으로 길 찾기 문제라고도 말한다 


- 다익스트라 최단 경로 알고리즘 : 그래프에서 여러개의 노드가 있을 때 특정한 노드에세 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘 

가장 비용이 적은 노드를 선택해서 임의의 과정을 반복하기 때문에 그리드 알고리즘 으로 분류 

- 다익스트라 최단 경로 알고리즘의 과정 

1) 출발 노드를 설정 
2) 최단 거리 테이블을 초기화 한다 
3) 방문하지 않은 노드중에서 최단 거리가 가장 짧은 노드를 선택 
4) 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다 
5) 3번과 4번을 반복한다 

->  각 노드에 대한 최단 거리 정보를 1차원 리스트에 저장하여 리스트를 갱신한다 

- 다익스트라 최단 경로 알고리즘 구현 방법 두가지 

1) 간단한 다익스트라 알고리즘 : O(V^2)의 시간복잡도를 가진다 (V는 노드의 개수)

: 각 노드에 대한 최단 거리를 담은 1차원 리스트 선언 -> 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소 순차탐색

2) 개선된 다익스트라 알고리즘 : O(ElogV) (V는 노드의 개수, E는 간선의 개수) 

:힙 자료구조를 사용하여 구현한다 

*힙 자료구조: 우선순위 큐(우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 것)을 구현하기 위해 사용된다 -> 파이썬에서는 PriorityQueue 또는 heapq를 사용한다 

*최소힙의 경우 우선순위가 가장 낮은 데이터가 먼저 삭제되고 최대힙의 경우 우선순위가 가장 높은 데이터가 먼저 삭제된다 최단경로에서는 최소힙을 사용하게 된다 

🍫 2021.09.10 다익스트라 프로그래밍, 최단경로 관련 인강 듣고 내용 정리

- heapq 라이브러리 활용을 통해 우선순위 큐 사용하여 풀기 (in 파이썬)

import heapq     queue = []

heapq.heappush(queue,[거리,노드])  ->queue리스트에 heap형태로 데이터를 넣는다는 의미 

heapq.heappop(queue) -> 데이터를 하나씩 뽑는다 (value가 작은 순서대로 정렬이 되어서 데이터가 출력이 된다)

🍟 2021.09.12 다익스트라 시간복잡도, 플로이드 위셜 알고리즘 개념정리 

- 다익스트라 알고리즘 시간복잡도 

다익스트라 알골지므은 크게 두 가지 과정을 거친다

과정1) 각 노드마다 인접한 간선들을 모두 검사하는 과정 
-> 각 노드는 최대 한번씩 방문하므로 O(간선의 개수) 

과정2) 우선순위 큐에 의해 노드/거리 정보를 넣고 삭제하는 과정 
-> 검색할때마다 간선을 검색하고 업데이트를 한다 그러므로 최대 O(간선의개수)가 걸리고, 새롭게 넣은 정보들을 우선순위 순서대로 업데이트하고 유지하기 위해서는 O(log간선의개수) 가 소요된다 최종적으로는 O(ElogE)

=> 따라서 최종 시간 복잡도는 (*E간선의 개수) O(E) + O(ElogE) 임으로 O(ElogE)가 된다 

- 플로이드 워셜 알고리즘 (다이나믹프로그래밍을 활용한 알고리즘)

: 모든 지점에서 다른 모든 지점까지의 최단경로를 모두 구해야 하는 경우에 사용할 수 있는 알고리즘 , 각 단계마다 해당 노드(단계별로 해당되는 노드)를 거쳐가는 경우를 계산하여 최단거리를 갱신한다 

다익스트라 알고리즘과 달리 출발노드가 1개가 아니므로 1차원 리스트가 아닌 2차원 리스트에 최단거리 정보를 저장해야한다 

노드의 개수가 N일때 알고리즘 상으로 N번의 단계를 수행하며, 단계마다 O(N^2)번의 연산을 통해 현재 노드를 거쳐가는 모든 경로를 고려하므로 총 시간복잡도는 O(N^3)이다 

🥢 2021.09.13 최소신장트리 ,그래프 등 개념정리

- 신장트리란? 

: spanning tree라고 불리며 3가지 조건을 만족해야한다 

첫째, 모집합의 그래프의 모든 노드를 포함해야 한다 둘째, 모든 노드가 서로 연결되어야 한다, 셋째 트리의 속성을 만족해야한다 (사이클이 존재하지 않는다)

- 최소신장트리란? : minimum spanning tree (MST)라느고 불리며 신장트리 중에서 간선의 가중치 합이 최소인 트리를 지칭한다

최소 신장 트리를 찾아낼 수 있는 알고리즘 종류: 크루스칼 알고리즘, 프림 알고리즘 

- 크루스칼 알고리즘 (그리드 알고리즘의 일종)

1) 모든 정점을 독립적인 집합으로 만든다 
2) 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 비교한다 
3) 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다 (사이클이 생기지 않기 위한 작업)

-> 사이클이 되지 않기 위해 사용하는 Union-Find 알고리즘

: Disioint Set을 표현할때 사용하는 알고리즘으로 트리 구조를 활용한다 
같은집합안에 있는 노드를 연결하게 되면 사이클이 발생할 수 있어 union-find알고리즘을 통해 이를 방지한다 

(*Disioint Set은 서로 중복되지 않은 부분 집합들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조, 한마디로 서로소 집합 자료구조이다) 

구현 순서 

1) n개의 원소가 개별집합으로 이뤄지도록 초기화 한다
2) 두개의 부분집합을 합해서 하나의 트리로 만듬 (두 부분집합의 최상단 노드 중 root노드가 될 것을 선정하여 나머지 그룹을 해당 트리의 자식트리로 연결한다)
3) 여러 노드가 존재할때, 두개의 노드를 선택해서 현재 두 노드가 같은 그래프에 속하는지 판별하기 위해 각 부분집합의 루트원소가 같은지 확인한다  

-> union-find 알고리즘의 고려할 점: union의 순서에 따라서 최악의 경우 링크드 리스트 형태가 될 수 있다 이를 해결하기 위해서 union-by-rank와 path compression기법을 사용한다 

+ union-by-rank 기법: 각 트리에 대해 높이를 기억해 두고, union시 rank(높이)가 다르면, 높이가 작은 트리를 높이가 큰 트리에 붙인다 (높이가 큰쪽이 root노드가 된다) 만약 트리가 높이가 같다면, 한쪽 트리의 rank를 높여준다 => 시간복잡도는 O(logN)으로 줄일 수 있다
+ path compression 기법 : find를 실행한 노드에서 거쳐간 노드를 루트에 바로 연결하는 방법 루트 노드를 한번에 알 수 있다 => 시간복잡도는 : O(Mlog*N) but 거의 O(1)에 가까운 시간복잡도를 가질 수 있다

크루스칼 알고리즘의 시간복잡도:
각 노드들을 부분집합하는 초기화 과정 O(v) + weight가 작은 순서대로 sort하는 과정 O(ElogE) + 각 간선에 대해서 중복되는 노드가 없는지 확인하고 합치는 과정 O(E) = O(ElogE)

🌸 2021.09.15

- 파이썬 zip 함수 : 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수이다 

ex) list(zip([1,2,3], [4,5,6)) -> [(1,4), (2,5), (3,6)]

- 파이썬 bin 함수 : 10진수를 2진수로 바꿔주는 역할을 하는 함수이다

ex) a= 46 bin(a) = '0b101110'

주의점: 해당함수의 경우 결과값 앞에 0b가 붙기때문에(이진수임을 알리기 위해서) [2:]등의 슬라이싱을 통해 결과값에 접근할 수 있다

- 파이썬 rjust함수 : 문자열을 오른쪽 정렬해서 출력할때 사용하는 함수 

문자열.rjust(전체 자리 숫자, 공백이 있을 경우 공백을 채울 리스트) 

-  파이썬 dict value값 기준으로 정렬하기 

sorted(dict.items(), key=lambda x : x[1]) 오름차순 / sorted(dict.items(), key=lambda x : x[1], reverse=True) 내림차순 

key를 기준으로 할때에는 sorted(dict.items(), key =lambda x : x[0])

- 위상정렬 

: 정렬 알고리즘의 일종, 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용하는 알고리즘으로 구체적으로는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 알고리즘이다. 

(*진입 차수: 특정한 노드로 들어오는 간선의 개수)

위상정렬 알고리즘의 순서 

1) 진입차수가 0인 노드를 큐에 넣는다
2) 큐가 빌 때 까지 다음의 과정을 반복한다 
    1) 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다
    2) 새롭게 진입차수가 0이 된 노드를 큐에 넣는다

위상정렬의 시간복잡도

: O(V + E) 위상정렬을 수행할 때에는 모든 노드를 확인하면서 해당 노드에 대한 간선을 제거해야하기 때문에 노드와 간선의 개수 만큼 시간이 걸리게 된다 
    
👓 2021.09.18 알고리즘 문제 풀이 

- zip을 통해서 두개의 배열을 순환하기 : for a1, a2 in zip(arr1,arr2) {} -> a1과 a2는 각각 arr1,arr2의 원소들을 가리킨다 

만약, for pair in zip (arr1, arr2) {} -> 식으로 식을 쓰게 된다면 pair을 출력했을 때 (arr1의 원소, arr2의 원소) 형식으로 출력이 된다

- zip 형식의 데이터를 사전형식으로 만들기 : dict(zip(arr1,arr2)) -> arr1의 원소가 key, arr2의 원소가 value의 역할을 하는 dict 자료형이 만들어진다

(* 만약, zip의 대상이 되는 배열의 길이가 서로 다를때에는 주의해야한다 더 긴 쪽의 배열의 원소들이 탈락되는 현상이 발생할 수 있다) 

- 다중 조건으로 배열하기 파이썬 
old_arr = [(1,2), (3,4), (5,6), (7,8)]

: new_arr = sorted(old_arr, key = lambda x : (x[0], -x[1]))

-> x[0]은 아이템의 첫번째 요소를 기준으로 오름차순, -x[1]은 아이템의 두번째 요소를 기준으로 내림차순

⏰ 2021.09.19 프로그래머스 알고리즘 문제풀이 (+ 외울만한 코드 정리)

- 최대공약수 구하기 in 파이썬 

: for i in range(min(a,b), 0, -1 ): 

    if a % i == 0 and b % i == 0: print(i) -> i가 최대 공약수 
    
- 최소공배수 구하기 in 파이썬 

: for i in range(max(a,b), (a*b)+1):

    if i%a == 0 and i % b == 0 : print(i) -> i가 최소 공배수 
    
  
- 런타임 에러 : 0으로 나눴을때와 같은 예외상황 처리 못해서 발생했을 수 있음

🎃 2021.09.20 프로그래머스 문제 3개 품

🎭 2021.09.21 해시 복습

- Hash 구조 

: key에 value를 저장하는 데이터 구조이다 / 파이썬의 딕셔너리 타입이 해쉬테이블의 대표적인 예이다 / 보통은 배열을 미리 hash table 사이즈 만큼 생성 한 후에 사용한다 

-> 파이썬에서는 따로 구현할 필요 없이 dict 자료형을 사용하면 된다 

- hash 용어 

hash ) 임의 값을 고정 길이로 변환하는 것 

hash table) 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조

hashing function ) key에 대한 산술 연산을 통해서 데이터 위치를 찾을 수 있는 함수

hash value (or hash address) ) key를 해싱 함수로 연산해서, 해쉬값을 알아내고 이를 기반으로 key의 데이터 위치를 찾을 수 있다 

slot ) 한개의 데이터를 저장할 수 있는 공간 

(*저장한 데이터에 대해 key를 추출할 수 있는 별도 함수도 존재할 수 있다) 

- enumerate 함수 : 리스트가 있는 경우 index와 value를 전달하는 기능을 가진 함수이다 

ex) for i , value in enumerate(list변수 이름) : 

- collections 모듈의 Counter함수 

: collections 모듈을 import하면 Counter함수를 사용할 수 있다 이때 파라미터로 배열 데이터를 넘겨되면 각각의 element가 해당 배열에 몇개 있는지 count한 값을 'element':개수 식으로 return한다 

collections의 Counter에서 반환되는 값끼리 - 이 가능하다 

예를 들어 두가지 배열에서 차집합을 구하고 싶을때 활용할 수 있다 

import collections

answer = collections.Counter(participant) - collections.Counter(completion) 

list(answer.keys()) -> 차집합 원소가 든 리스트 (*단 두 배열간의 길이 차이가 1일때 가능)

🧶 2021.09.22 프로그래머스 문제 품 

- 만약 어떤 연산을 통해서 나온 결과를 리스트에 저장하여 활용할 경우, 해당 리스트의 길이가 문제가 될 수 있다. 예를들어 for문을 통해서 결과값을 저장해두는 리스트의 원소를 비교해야할 때 만약 연산의 결과가 아직 없거나 false일때는 해당 리스트는 비어 있기 때문에 len을 통해서 해당 리스트가 비어있는지 확인 절차를 걸쳐야 error을 피할 수 있다. 이럴때에는 결과값을 저장해두는 리스트에 결과값과 전혀 상관없는 값을 임시로 하나 저장을 해두면 len을 통하지 않고 search가 가능해진다 

- 파이썬 자바스크립트에서 split함수를 사용할때에 해당 함수의 파라미터로 문자열을 넣어줄 수 있다 예를들어 'onetwothreefour'에서 two를 지우고 싶다면 원소를 차례대로 접근할 필요 없이 arr = arr.split('one') 이라고 하면된다 (split을 사용하는 경우 반환되는 값은 ["",'twothreefour'] 임을 주의해야 한다) 추가적으로 만약 one을 1로 교체하고 싶을 때에는 arr = arr.replace('one',1) 식으로 하면 된다 

☕ 2021.09.24 프로그래머스 문제 품 

- 파이썬에서 replace , lstrip, rstrip 등 풀이 방법 중 하나로 생각해보기 노력해보기 + 정규표현식 공부 

🍰 2021.09.26 피보나치 수 구하기 코드 외우기! 

방법1) 재귀함수 이용하기 / 단점: n이 커지면 커질 수록 수행 시간이 기하급수적으로 늘어난다 

```
  def fibo(x):
    if x == 1 or x == 2:
      return 1 
    return fibo(x-1) + fibo(x-2)
```

방법2) 메모제이션을 활용하여 풀기 

```
  d = [0] * 100
  
  def fibo(x):
    if x == 1 or x == 2:
      return 1
    if d[x] != 0:
      return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
```

방법3 ) 반복문을 사용하여 풀기 

```
  d = [0] * (n+1)
  d[1] = 1
  d[2] = 1
  
  for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
   
  return d[n]
```

- 리스트의 자료형 map사용하여서 변환하기 : str->int 형으로 a = list(map(int,a)) or a = list(map(int,a.split(' '))

🥗 2021.09.27 프로그래머스 2문제 품

🥪 2021.09.28 프로그래머스 2문제 품 

🧶 2021.09.09 프로그래머스 2문제 품 

- 서로 다른 배열을 합쳐서 하나의 사전으로 만들기 : example = dict(zip(arr1, arr2))  "zip"을 활용한다!

- decorate-sort-undecorate (장식-정렬-복원)
1) 초기 리스트가 정렬 순서를 제어 하는 새로운 값으로 장식된다
2) 장식된 리스트를 정렬한다 
3) 장식을 제거하여 새 순서로 초깃값만 포함하는 리스트를 만든다 

이점: 정렬이 안정적이다(두 항목이 같은 키를 가지면 그들의 순서가 정렬된 리스트에 유지된다), 장식된 튜플의 순서는 최대 처음 두 항목에 의해 결정되므로 원래 항목은 비교 가능할 필요가 없다 

-> 파이썬이 정렬에서 key함수를 제공하여 해당 기법은 자주 필요하지 않음 

*파이썬의 key 함수 

: list.sort()와 sorted()는 모두 비교하기 전에 각 리스트 요소에 대해 호출할 함수를 지정하는 key 매개변수를 가지고 있다 

예시) 대소문자를 구분하지 않은 문자열 비교 
arr = sorted(arr.split(), key=str.lower) 

- 여러 레코드가 같은 키를 가질 때 원래의 순서가 유지되는 정렬 

ex)
``` 
data = [('red',1),('blue',2),('red',2),('blue',2)]
sorted(data, key=itemgetter(0)) // blue는 원래 순서대로 1과 1 이 나옴 
[('blue',1),('blue',2),('red',1),('red',2)]
```

🎁 2021.10.03 프로그래머스 한문제 

🔍 2021.10.09 프로그래머스 코딩 문제 풀이 + 트리 자료구조 복습 

💡 2021.10.10 프로그래머스 코딩 문제 

- 파이썬에서 사전형 자료 구조 초기화 선언 쉽게 하는 방법 

```
  dict = {x : x**2 for x in {2,4,6,8}} 
  student = { x: 0 for x in range(n) }
  dict2 = {zip(keys,items)}
```

