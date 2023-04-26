def drawRomb(size=5, element=0):
    if element == size:
        return
    print(" " * (size-element-1) + "* " * (element + 1))
    drawRomb(size, element+1)
    print(" " * (size-element-1) + "* " * (element + 1))
drawRomb(5)