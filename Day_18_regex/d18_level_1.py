# #Exercises: Level 1
# What is the most frequent word in the following paragraph?
#     paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
#     [
#     (6, 'love'),
#     (5, 'you'),
#     (3, 'can'),
#     (2, 'what'),
#     (2, 'teaching'),
#     (2, 'not'),
#     (2, 'else'),
#     (2, 'do'),
#     (2, 'I'),
#     (1, 'which'),
#     (1, 'to'),
#     (1, 'the'),
#     (1, 'something'),
#     (1, 'if'),
#     (1, 'give'),
#     (1, 'develop'),
#     (1, 'capabilities'),
#     (1, 'application'),
#     (1, 'an'),
#     (1, 'all'),
#     (1, 'Python'),
#     (1, 'If')
#     ]
# ================================================================================================================
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love'
from collections import Counter
import re

word_list = re.split(r"[ .]", paragraph)
print(Counter(word_list))
print(sorted(Counter(word_list).items(), key=lambda x:x[1], reverse=True))

# The position of some particles on the horizontal x-axis are -
# -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.
# Extract these numbers from this whole text and find the distance between the two furthest particles.
# points = ['-12', '-4', '-3', '-1', '0', '4', '8']
# sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 -(-12) # 20
# ================================================================================================================
text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
x_axis_cods = re.findall(r'-\d+|\d+', text)
print("points::",x_axis_cods)
x_cods_to_int = [int(item) for item in x_axis_cods]
x_cods_to_int.sort()
print("sorted points::",x_cods_to_int)
print(f'Dist b/w two furthest points {x_cods_to_int[0]} to {x_cods_to_int[-1]} is {abs(x_cods_to_int[0] - x_cods_to_int[-1])}')
