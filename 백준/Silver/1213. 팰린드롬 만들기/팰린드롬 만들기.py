import sys
from collections import defaultdict
read = sys.stdin.readline

NAME = read().rstrip()

def findPalindrome():
  answer = ''

  # 이름의 단어들을 딕셔너리로 구성
  nameDict = defaultdict(int)
  for c in NAME:
    nameDict[c] += 1

  # 홀수인 이름의 단어와 개수 찾기
  oddChar = ""
  oddCount = 0
  for c in nameDict:
    if nameDict[c] % 2:
      oddCount += 1
      oddChar = c
      
  if(oddCount > 1):
    return "I'm Sorry Hansoo"
  
  # 이름의 단어들을 사전순 정렬
  nameDict = dict(sorted(nameDict.items()))

  # 팰린드롬 대칭 단어 조합
  for c in nameDict:
    half = (nameDict[c] // 2)
    answer += (c * half)
    nameDict[c] -= (half * 2)
  answer = answer + oddChar + answer[::-1]
  
  return answer
  
print(findPalindrome())