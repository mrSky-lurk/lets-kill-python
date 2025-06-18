# Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Join A and B
# ================================================================================================================
print("Joining A and B:: ", A.union(B)) # Works both ways

# Find A intersection B
print("Intersection A and B:: ", A.intersection(B)) # Works both ways
print("Intersection B and A:: ", B.intersection(A))

# Is A subset of B
print('Is A subset of B?? - ', A.issubset(B))
print('Is B subset of A?? - ', B.issubset(A))

# Are A and B disjoint sets
print("A & B disjoint set(can not be joined)?? - ", A.isdisjoint(B)) # Works both ways

# Join A with B and B with A
# ================================================================================================================
print("Joining A and B:: ", A.union(B)) # Works both ways
print("Joining B and A:: ", B.union(A))

# What is the symmetric difference between A and B
# ================================================================================================================
print("Symmetric difference between A and B:: ", A.symmetric_difference(B)) # Works both ways
print("Symmetric difference between B and A:: ", B.symmetric_difference(A))
# Delete the sets completely
del A
del B