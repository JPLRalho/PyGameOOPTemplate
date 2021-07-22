from MainLoop import MainLoop

if __name__ == '__main__':
    mainLoop = MainLoop()
    while True:
        mainLoop.update()
        mainLoop.events()
        mainLoop.draw()
