

from typing import List
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
        
def twoSum(nums: List[int], target: int) -> List[int]:
    prevMap = {}

    logging.debug(f'nums: {nums}')
    logging.debug(f'target: {target}')
    for i, n in enumerate(nums):
        diff = target - n

        logging.debug(f'difference(target - n): {diff}')
        logging.debug(f'iteration: {i}')
        logging.debug(f'current num: {n}')
        logging.debug(f'current hashmap: {prevMap}')
        if diff in prevMap:
            logging.debug(f'match: (index {prevMap[diff]}: {nums[prevMap[diff]]}, index {i}: {n}), for nums that sum to {target}')
            logging.debug(f" Updated hashmap state: {prevMap}")
            return [prevMap[diff], i]
        prevMap[n] = i

twoSum([2,7,11,15], 9)




