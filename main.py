import pygame as pyg

pyg.init()
screen = pyg.display.set_mode((1000,1000))
clock = pyg.time.Clock()
running = True
clicks = 0
positions = []
starting_point = []
ending_point = []
second_point = []
third_point = []
white = pyg.Color(255,255,255)
black = pyg.Color(0,0,0)
screen.fill(white)
clock.tick(60)
pyg.display.update()
last_click_value = False
while running:
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

pyg.quit()