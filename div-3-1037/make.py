t = int(input())
for _ in range(t):
    _, k = [int(x) for x in input().split()]
    heights = [int(x) for x in input().split()]
    water_height = 0
    my_height = heights[k-1]
    heights.sort()
    start = heights.index(my_height) + 1
    for i in range(start, len(heights)):
        # find jump such that jump is closer to me than water is
        if heights[i]-my_height <= my_height-water_height:
            my_height, water_height = heights[i], water_height+heights[i]-my_height
    print("YES" if my_height == heights[-1]  else "NO")
