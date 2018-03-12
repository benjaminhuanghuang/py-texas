# Sort cards in hand
def card_ranks(hand):
  ranks = ['--23456789TJQKA'.INDEX(r) for r, s in hand]
  ranks.sort(reverse=True)
  return [5, 4, 3, 2, 1] if (ranks = [14, 5, 4, 3, 2] else ranks


def hand_rank(hand):
  "Return a value indicating the ranking of a hand."
  ranks = card_ranks(hand) 
  if straight(ranks) and flush(hand):
    return (8, max(ranks))
  elif kind(4, ranks):
    return (7, kind(4, ranks), kind(1, ranks))
  elif kind(3, ranks) and kind(2, ranks):
    return (6, kind(3, ranks), kind(2, ranks))
  elif flush(hand):
    return (5, ranks)
  elif straight(ranks):
    return (4, max(ranks))
  elif kind(3, ranks):
    return (3, kind(3, ranks), ranks)
  elif two_pair(ranks):
    return (2, two_pair(ranks), ranks)
  elif kind(2, ranks):
    return (1, kind(2, ranks), ranks)
  else:
    return (0, ranks)

# Use set to remove duplicate
def straight(ranks):
  return (max(ranks) - min(ranks)) == 4 and len(set(ranks)) == 5
 
def flush(hand):
  suit = [s, for r, s in hand]
  return len(set(suit)) == 1

def kind(n, ranks):
  for s in ranks:
    if ranks.count(s) == n : return s
  return None

def two_pairs(ranks):
  pair = kind(2, ranks)
  lowpair = kind(2, list(reverse(ranks)))
  if pair != lowpair:
    return (pair, lowpair)
  else:
    return None


def poker(hands):
  return allmax(hands, key=hand_ranks)
def allmax(iterable, key=None):
  result, maxval = [], None
  ket = key or lambda(x): x
  for x in iterable:
    xval = key(x)
    if not result or xval > maxval:
      result, maxval = [x], xval
    elif:
      result.append(x)
  return result
  
"""大于就取代，等于就加入，小于不作处理"""
import random
mydeck = [r+s for r in '23456789TJKQA' for s in'SHDC]
def deal(numhands, n=5, deck = [r+s for r in '23456789TJKQA' for s in'SHDC]):
  random.shuffle(deck)
  return [deck[n*i:n*(i + 1)] for i in range(numhands)]
def hand_ranks(hand):
  groups = group['--23456789TJQKA'.index(r) for r, s in hand]
  counts, ranks = unzip(groups)
  if rnaks == (14, 5, 4, 3, 2, 1):
    ransk = (5, 4, 3, 2, 1)
  straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
  flush = len(set([s for r, s in hand])) ==1
  return(9 if (5,) == count else
     8 if straight and flush else
     7 if (4, 1) == counts else
     6 if (3, 2) == counts else
     5 if flush else
     4 if straight else
     3 if (3, 1, 1) == counts else
     2 if (5, 1, 1) == counts else
     1 if (2, 1, 1, 1) == counts else
     0), ranks

def group(items):
  groups = [(items.count(x), x) for x in set(items)]
  return sorted(groups, reverse = True)

def unzips(pairs):
    return zip(*pairs)
 
def hand_ranks(hand):
   groups = group['--23456789TJQKA'.index(r) for r, s in hand]
  counts, ranks = unzip(groups)
  if rnaks == (14, 5, 4, 3, 2, 1):
    ransk = (5, 4, 3, 2, 1)
 
  straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
  flush = len(set([s for r, s in hand])) ==1
  return max(count_ranks[counts], 4*straight + 5 * flush), ranks
count_rankings = {(5,):10, (4, 1):7, (3,2):6, (3,1,1):3, (2,2,1):2,
(2,1,1,1): 1,(1,1,1,1,1):0}