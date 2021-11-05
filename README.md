# coding_study
## 📌 코딩 테스트 대비 알고리즘 study 

💻💻 사용할 언어: 파이썬, 자바스크립트

2021.08.27 지금까지 공부했던 자료구조 정리

🎈2021.08.28 DFS,BFS 개념정리 + 관련 인강듣고 구현 코드 짜보기

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


🎬 2021.09.04 정렬 알고리즘 개념 정리 


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

> 파이썬에서 빠르게 정보를 입력받는법

: import sys

input_data = sys.stdin.readline().rstrip()

📁 2021.09.07 다이나믹 프로그래밍 개념정리 

🩹 2021.09.08 다이나믹 프로그래밍(=동적 계획법), 분할정복 추가 공부 


🎹 2021.09.09 다이나믹 프로그래밍 연습문제, 최단경로 , 다익스트라 알고리즘개념 정리 


🍫 2021.09.10 다익스트라 프로그래밍, 최단경로 관련 인강 듣고 내용 정리

- heapq 라이브러리 활용을 통해 우선순위 큐 사용하여 풀기 (in 파이썬)

import heapq     queue = []

heapq.heappush(queue,[거리,노드])  ->queue리스트에 heap형태로 데이터를 넣는다는 의미 

heapq.heappop(queue) -> 데이터를 하나씩 뽑는다 (value가 작은 순서대로 정렬이 되어서 데이터가 출력이 된다)

🍟 2021.09.12 다익스트라 시간복잡도, 플로이드 위셜 알고리즘 개념정리 

🥢 2021.09.13 최소신장트리 ,그래프 등 개념정리

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

📎 2021.10.12 프로그래머스 

- 숫자를 자리수에 상관없이 정렬하고 싶을때 

 예를들어 9, 14, 34, 11 이라는 숫자를 int형 그대로 값끼리 비교하면 34, 14, 11, 9가 되게 된다 하지만 해당 원소들을 모두 문자형으로 바꾼후 sort하게 되면 
 숫자가 아닌 문자로 취급되어 정렬하게 되면 9, 34, 14, 11 식으로 정렬되게 된다 값에 상관 없이 해당 원소들의 맨앞에 오는 숫자끼리 비교를 하기 때문이다 
 (*주의점: 14, 11과 같이 앞자리 숫자가 동일하게 1, 1 이라면 원하는대로 정렬이 되지 않을 수 있으므로 추가적인 작업을 해주어야 한다)  

예시)number = [str(num) for num in numbers]   number.sort(reverse=True) 를 차례대로 해주게 되면 9, 34, 14 ,11 형식으로 배열이 된다 

- 문자타입으로 된 숫자 비교하는 방법 :  number.sort(key = lambda x:x*3, reverse=True) 
예를들어 [3, 30, 34, 5, 9] 배열을 ['9', '5', '34', '3', '30']로 정렬을 하고 싶다면 (1000 전까지의 숫자가 온다는 가정하에 ) 
x:x*3으로 처리하여 비교를 한다 문자타입을 가진 원소를 *3 을 하게 되면 [999, 555, 343434, 333, 303030]식으로 문자가 3번 반복된다 그리고 해당 원소들을 가진 배열을 sort하게 되면 
333과 303030의 경우에 첫번째 자리 숫자부터 비교를 시작하면 3과 30으로 비교를 할 때에는 30이 앞으로 정렬이 되지만 333, 303030의 경우 두번째 자리에서 비교시 3이 0보다 크기 때문에 
3이 30보다 앞에 정렬되게 된다 

🎈 2021.10.13 프로그래머스 문제 / 파이썬 itertools 라이브러리 공부 

itertools: 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리 

- permutations: 리스트와 같은 iterable 객체에서 r 개의 데이터를 뽑아 일렬로 나열하는 모둔 경우를 계산 해준다 permutation은 클래스 이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다 

순서를 고려했을 때의 예시
```
from itertools import permutations 
data = ['A', 'B', 'C'] 
result = list(permutations(data,3)) #3개의 원소로 집합을 만들 었을때의 모든 경우의 수

result [('A','B','C'), ('A','C','B'), ('B','A','C'), ('B','C','A'), ('C','A','B'), ('C','B','A')] 
```

- combinations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산 combinations은 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다 

순서를 고려하지 않고 나열하는 모든 경우 예시 
```
from itertools import combinations 

data = ['a','b','c']
result = list(combinations(data,2))

result -> [('a','b'), ('a','c'), ('b','c')] 
```

-product: 리스트와 같은 iterable 객체에서 r 개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산한다. 단, 원소는 중복해서 넣어준다 product는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다 

예시
```
from itertools import product 

data = ['a','b','c']
result = list(product(data, repeat=2)) #2개를 뽑는 모든 순열

result -> [('a','a'), ('a','b') ...]
```

- combinations_with_replacement: 리스트와 같은 iterable 객체에서 r 개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산한다 다만 원소를 중복해서 뽑는다 combinations_width_replacement는 클래스 이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용해야 한다 

예시 
```
from itertools import combinations_with_replacement

data = ['a','b','c']
result = list(combinations_width_replacement(data,2)) #2개를 뽑는 모든 조합 

result -> [('a','a'), ('a','b') .... ] 
```
🍧 2021.10.14 프로그래머스 js level 1문제 3개 품 

🥨 2021.10.16 프로그래머스 py level 2 문제 백준 문제 

- 리스트 자료형으로 문제를 풀었는데 시간초과가 나왔을 경우 deque 사용하기!!!!!

deque 사용법 from collections import deque  arr = deque([1,2,3,4]) 식으로 라이브러리 import후 사용한다 

- 백준에서 js (node.js) 입력 받는 법 

```
1. 하나의 값을 입력받을 때 
const input = require('fs').readFileSync('dev/stdin').toString();

2. 공백으로 구분된 한줄 값 입력받을 때 
const input = require('fs').readFileSync('dev/stdin').toString().split(' ');

3. 여러 줄의 값들을 입력받을 때 
const input = require('fs').readFileSync("/dev/stdin").toString().split('\n');

4. 첫번째 줄에 자연수 n을 입력받고, 그 다음줄 부터 공백으로 구분된 n 개의 값들을 입력받을 때 
const [n, ...arr] = require('fs').readFileSync("/dev/stdin").toString().split(/\s/);

5. 첫번째 줄에 자연수 n을 입력바독, 그 다음줄 부터 n 개의 줄에 걸쳐 하나씩 값을 입력받을 때 
const n, ...arr] = require('fs').readFileSync("/dev/stdin").toString().split('\n');

6. 하나의 값 또는 공백으로 구분된 여러 값들을 여러 줄에 걸쳐 섞여서 입력받을 때 
const input = require('fs').readFileSync("/dev/stdin").toString().split(/\s/);
const n = input[0];
const n_arr = input.slice(1, n+1);
const [m, ...m_arr] = input.slice(n+1);
```

🤣 2021.10.17 자료구조 인강 수강 

- enumerate함수 : enumerate는 열거하다 라는 뜻으로 리스트가 있는 경우 순서와 리스트의 값을 전달하는 역할을 한다 순서가 있는 자료형 (list, set, tuple, dictionary, string)을 입력받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다 

예시 
```
data = enumerate([1,2,3])
for i, value in data:
  print(i,value)
  
-> 0,1 / 1, 2 / 2 ,3 
```
😀 2021.10.20 js level 1 문제 3개 

😶 2021.10.21 js level 1 문제 2개 

😏 2021.10.22 py level 2 해시 문제 2개

🍖 2021.10.26 py level 1 스택/큐 문제 1

🥗 2021.10.27 

for i in range(len(arr)) 보다 for i in arr가 시간 이 덜 소요 된다 

🎏 2021.11.02 py level 2 문제 3개 

🎁 2021.11.03 구름 level 2문제

🧵 2021.11.04 프로그래머스 2문제 

- n = n// 3 - (n%3 ==0) ->n%3이 0일 경우 true가 되어 1을 뺼 수 있다

🚚 2021.11.05 코딩테스트 유형별 전략 
