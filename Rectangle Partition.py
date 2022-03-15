from collections import Counter
w, h, len_x, len_y = [int(i) for i in input().split()]
x_list = [int(i) for i in input().split()] + [w]
y_list = [int(i) for i in input().split()] + [h]
cross_points = [x + y for x in x_list for y in y_list]
all_points = x_list + y_list + cross_points
squares_counter = 0
for n in Counter(all_points).values():
    if n > 1:
        squares_counter += int(n * (n - 1) / 2)
print(squares_counter)
