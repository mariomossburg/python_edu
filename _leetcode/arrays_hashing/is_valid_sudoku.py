print("-----leetcode: is valid sudoku-----")
from collections import defaultdict
from typing import List

def func(board: List[List[str]])-> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)
    # automatically creates a new set for any new key, 
    # so you don’t have to check if the key exists before adding to it
    
    # The tuple (r//3, c//3) uniquely identifies each 3x3 sub-box. 
    # For example, cell (4,5) is in square (1,1)
    
    # why default dict here? automatic buckets(new empty set's created)
    # O(1) membership set can't hold duplicates
    
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])
    return True
                
                
                
                
         