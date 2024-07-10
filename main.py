import pygame as pyg

pyg.init()
screen = pyg.display.set_mode((1000,1000))
clock = pyg.time.Clock()
running = True
clicks = 0
x_offset = 1000 # wanted values of 0 
y_offset = 1000
positions = []
starting_point = []
ending_point = []
second_point = []
third_point = []
a = None
b = None
c = None
d = None
white = pyg.Color(255,255,255)
black = pyg.Color(0,0,0)
screen.fill(white)
clock.tick(60)
pyg.display.update()
last_click_value = False
while running and clicks < 4:
    for event in pyg.event.get():
        if event.type == pyg.KEYDOWN and event.key == pyg.K_DELETE:
            running = False
    pyg.display.update()
    if clicks < 4:
        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN and not(last_click_value):
                positions.append(pyg.mouse.get_pos())
                print(positions)
                pyg.draw.circle(screen, black, positions[len(positions)-1], 3)
                last_click_value = True
                clicks += 1
                if clicks == 4:
                    x_values = []
                    x_orders = []
                    for i in range(4):
                        if len(x_values) != 0:
                            for j in range(i+1):
                                if j == i:
                                    x_values.insert(j, list(positions[i])[0])
                                    x_orders.insert(j, i)
                                    break
                                if list(positions[i])[0] < x_values[j]:
                                    x_values.insert(j, list(positions[i])[0])
                                    x_orders.insert(j, i)
                                    break
                                
                        else:
                            x_values.append(list(positions[i])[0])
                            x_orders.append(0)
                    starting_point = list(positions[x_orders[0]])
                    print(starting_point)
                    second_point = list(positions[x_orders[1]])
                    print(second_point)
                    third_point = list(positions[x_orders[2]])
                    print(third_point)
                    ending_point = list(positions[x_orders[3]])
                    print(ending_point)
            elif event.type == pyg.MOUSEBUTTONUP:
                last_click_value = False
points = [starting_point, second_point, third_point, ending_point]
for point in points:
    if point[0] < x_offset:
        x_offset = point[0]
    if point[1] < y_offset:
        y_offset = point[1]
#first_row = [(starting_point[0]-x_offset)**3, (starting_point[0]-x_offset)**2, starting_point[0]-x_offset, starting_point[1]-y_offset, starting_point[1]-y_offset]
#unneeded because d = y1
d = starting_point[1]-y_offset
#a, b, c, d, y value
second_row = [(second_point[0]-x_offset)**3, (second_point[0]-x_offset)**2, second_point[0]-x_offset, d, second_point[1]-y_offset]
third_row = [(third_point[0]-x_offset)**3, (third_point[0]-x_offset)**2, third_point[0]-x_offset, d, third_point[1]-y_offset]
fourth_row = [(ending_point[0]-x_offset)**3, (ending_point[0]-x_offset)**2, ending_point[0]-x_offset, d, ending_point[1]-y_offset]
print(second_row)
print(third_row)
print(fourth_row)
# clear first pivot column
factor = third_row[0]/second_row[0]
third_row = [third_row[0]-second_row[0]*factor, third_row[1]-second_row[1]*factor, third_row[2]-second_row[2]*factor, third_row[3]-second_row[3]*factor, third_row[4]-second_row[4]*factor]


factor = fourth_row[0]/second_row[0]
fourth_row = [fourth_row[0]-second_row[0]*factor, fourth_row[1]-second_row[1]*factor, fourth_row[2]-second_row[2]*factor, fourth_row[3]-second_row[3]*factor, fourth_row[4]-second_row[4]*factor]

# lead with 1
factor = 1/second_row[0]
second_row = [second_row[0]*factor, second_row[1]*factor, second_row[2]*factor, second_row[3]*factor, second_row[4]*factor]

# clear second pivot column
factor = fourth_row[1]/third_row[1]

fourth_row = [fourth_row[0]-third_row[0]*factor, fourth_row[1]-third_row[1]*factor, fourth_row[2]-third_row[2]*factor, fourth_row[3]-third_row[3]*factor, fourth_row[4]-third_row[4]*factor]

# lead with 1
factor = 1/third_row[1]
third_row = [third_row[0]*factor, third_row[1]*factor, third_row[2]*factor, third_row[3]*factor, third_row[4]*factor]

# lead with 1
factor = 1/fourth_row[2]
fourth_row = [fourth_row[0]*factor, fourth_row[1]*factor, fourth_row[2]*factor, fourth_row[3]*factor, fourth_row[4]*factor]
print("made pivots")
print(second_row)
print(third_row)
print(fourth_row)

# get rid of nasty stuff above the pivots
factor = third_row[2]/fourth_row[2]
third_row = [third_row[0]-fourth_row[0]*factor, third_row[1]-fourth_row[1]*factor, third_row[2]-fourth_row[2]*factor, third_row[3]-fourth_row[3]*factor, third_row[4]-fourth_row[4]*factor]

factor = second_row[2]/fourth_row[2]
second_row = [second_row[0]-fourth_row[0]*factor, second_row[1]-fourth_row[1]*factor, second_row[2]-fourth_row[2]*factor, second_row[3]-fourth_row[3]*factor, second_row[4]-fourth_row[4]*factor]

factor = second_row[1]/third_row[1]
second_row = [second_row[0]-third_row[0]*factor, second_row[1]-third_row[1]*factor, second_row[2]-third_row[2]*factor, second_row[3]-third_row[3]*factor, second_row[4]-third_row[4]*factor]

# find a b and c
a = second_row[4]-second_row[3]
b = third_row[4]-third_row[3]
c = fourth_row[4]-fourth_row[3]

print("reduced row echelon form")
print(second_row)
print(third_row)
print(fourth_row)
largest_x = 0
for i in range(4):
    if positions[i][0]-x_offset > largest_x:
        largest_x = positions[i][0]-x_offset
for i in range(1000):
    x = i
    y = x**3*a+x**2*b+c*x+d
    if x <= largest_x:
        pyg.draw.circle(screen, black, (x+x_offset,y+y_offset), 3)
        pyg.display.update()
    else:
        break
while running:
    for event in pyg.event.get():
        if event.type == pyg.KEYDOWN and event.key == pyg.K_DELETE:
            running = False
    pyg.display.update()

pyg.quit()