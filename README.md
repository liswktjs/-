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

>  정렬알고리즘 

정렬 알고리즘이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다 
/ 데이터를 사전에 정렬해 두면 후에 이진 탐색이 가능해진다 

종류) 선택저렬, 삽입정렬, 퀵정렬, 계수 정렬 등이 있다 

> 선택 정렬 (Selection Sort) 알고리즘 

'가장 작은 것을 선택 한다'라는 아이디어를 기본으로 하는 알고리즘이다 

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

