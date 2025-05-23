---
title: 770-Basic-Calculator-Iv
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/basic-calculator-iv


```
import pyutil as pyu
pyu.get_local_pyinfo()
```


```
print(pyu.ps2("python-dotenv"))
```


```
from typing import List
```


```
class Poly:
  def __init__(self, term: str = None, coef: int = None):
    if term and coef:
      self.terms = Counter({term: coef})
    else:
      self.terms = Counter()

  def __add__(self, other):
    for term, coef in other.terms.items():
      self.terms[term] += coef
    return self

  def __sub__(self, other):
    for term, coef in other.terms.items():
      self.terms[term] -= coef
    return self

  def __mul__(self, other):
    res = Poly()
    for a, aCoef in self.terms.items():
      for b, bCoef in other.terms.items():
        res.terms[self._merge(a, b)] += aCoef * bCoef
    return res

  # Def __str__(self):
  #   res = []
  #   for term, coef in self.terms.items():
  #     res.append(term + ': ' + str(coef))
  #   return '{' + ', '.join(res) + '}'

  def toList(self) -> List[str]:
    for term in list(self.terms.keys()):
      if not self.terms[term]:
        del self.terms[term]

    def cmp(term: str) -> tuple:
      # Smallest degree is the last
      if term == '1':
        return (0,)
      var = term.split('*')
      # Largest degree is the first
      # Breaking ties by lexicographic order
      return (-len(var), term)

    def concat(term: str) -> str:
      if term == '1':
        return str(self.terms[term])
      return str(self.terms[term]) + '*' + term

    terms = list(self.terms.keys())
    terms.sort(key=cmp)
    return [concat(term) for term in terms]

  def _merge(self, a: str, b: str) -> str:
    if a == '1':
      return b
    if b == '1':
      return a
    res = []
    A = a.split('*')
    B = b.split('*')
    i = 0  # A's index
    j = 0  # B's index
    while i < len(A) and j < len(B):
      if A[i] < B[j]:
        res.append(A[i])
        i += 1
      else:
        res.append(B[j])
        j += 1
    return '*'.join(res + A[i:] + B[j:])


class Solution:
  def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
    tokens = list(self._getTokens(expression))
    evalMap = {a: b for a, b in zip(evalvars, evalints)}

    for i, token in enumerate(tokens):
      if token in evalMap:
        tokens[i] = str(evalMap[token])

    postfix = self._infixToPostfix(tokens)
    return self._evaluate(postfix).toList()

  def _getTokens(self, s: str) -> Iterator[str]:
    i = 0
    for j, c in enumerate(s):
      if c == ' ':
        if i < j:
          yield s[i:j]
        i = j + 1
      elif c in '()+-*':
        if i < j:
          yield s[i:j]
        yield c
        i = j + 1
    if i < len(s):
      yield s[i:]

  def _infixToPostfix(self, tokens: List[str]) -> List[str]:
    postfix = []
    ops = []

    def precedes(prevOp: chr, currOp: chr) -> bool:
      if prevOp == '(':
        return False
      return prevOp == '*' or currOp in '+-'

    for token in tokens:
      if token == '(':
        ops.append(token)
      elif token == ')':
        while ops[-1] != '(':
          postfix.append(ops.pop())
        ops.pop()
      elif token in '+-*':  # IsOperator(token)
        while ops and precedes(ops[-1], token):
          postfix.append(ops.pop())
        ops.append(token)
      else:  # IsOperand(token)
        postfix.append(token)
    return postfix + ops[::-1]

  def _evaluate(self, postfix: List[str]) -> Poly:
    polys: List[Poly] = []
    for token in postfix:
      if token in '+-*':
        b = polys.pop()
        a = polys.pop()
        if token == '+':
          polys.append(a + b)
        elif token == '-':
          polys.append(a - b)
        else:  # Token == '*'
          polys.append(a * b)
      elif token.lstrip('-').isnumeric():
        polys.append(Poly("1", int(token)))
      else:
        polys.append(Poly(token, 1))
    return polys[0]
```


```
new Solution().basicCalculatorIV()
```


---
**Score: 5**