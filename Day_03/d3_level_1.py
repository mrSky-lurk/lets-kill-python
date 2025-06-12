import math

# my_age = int(input("Enter your age: "))
# my_height = float(input("Enter your height: "))
# complex_num = input("Enter a complex number: ")
# if complex_num is complex:
#     print(complex_num, " -- Correct its complex!")
# else:
#     print(complex_num," is not complex!")
# ========================================================================================
# Find Perimeter and Area of a right-angle triangle
# tri_height = float(input("Enter height of the right-angle triangle: "))
# tri_base = float(input("Enter base of the right-angle triangle: "))
# tri_hypoteneus = math.sqrt(tri_base ** 2 + tri_height ** 2)
# tri_area = 0.5 * tri_base * tri_height
# tri_perimeter = tri_height + tri_base + tri_hypoteneus
# print("hypoteneus of triangle:: ", tri_hypoteneus)
# print("Area of triangle:: ", tri_area)
# ========================================================================================
# Find Euclidean Dist b/w two points - dist = sqroot(sq(x1-x2) + sq(y1-y2))
loc_p = list(input("Enter the co-ordinates of point P: ").split(","))
loc_q = list(input("Enter the co-ordinates of point Q: ").split(","))
dist_x = abs(int(loc_p[0])-int(loc_q[0]))
dist_y = abs(int(loc_p[1])-int(loc_q[1]))
# st line equation -> y= mx+c
# where m = slope; c= constant; if c=0 the line passes through origin
# slope = (y1-y2) / (x1-x2); if x1 = x2, line is vertical line with slope Undefined
# X-intercept = where the line touches the x axis; means y=0
# Y -intercept = where the line touches the y axis
dist = math.sqrt(dist_x ** 2 + dist_y ** 2)
print("Euclidean Distance between these two points: ", dist)
# ========================================================================================

