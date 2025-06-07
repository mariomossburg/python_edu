# print('hello world')

# Sliding window real world use case
# first pair of users who liked the same post



# Two pointers 
likes = [(1,101), (2,101), (3,102), (4,105), (5,105)]

def find_pair_same_post(likes: list[tuple]):
    l,r = 0, 1
    while r < len(likes):
        if likes[l][1] == likes [r][1]:
            return likes[l][0], likes[r][0]
        l+=1
        r+=1
    return None

print(find_pair_same_post(likes))




timestamps = [1,2,3,4,6,7,10]

def max_likes_in_window(timestamps, k=3):
    l = 0
    max_likes = 0
    for r in range(len(timestamps)):
        while timestamps[r] - timestamps[l] > k:
            l +=1
        max_likes = max(max_likes, r - l + 1)
    return max_likes

print(max_likes_in_window(timestamps))


# binary search
post_times = [1,2,4,6,8,10]

def first_post_after(posts, target):
    l,r = 0, len(posts) - 1
    res= -1
    while l <= r:
        mid = (l + r) // 2
        if posts[mid] > target:
            res = posts[mid]
            r = mid - 1
        else:
            l = mid + 1
    return res

print(first_post_after(post_times, 5))