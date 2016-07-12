import turtle
import sys

turtle.speed('fast')

colors = ['red', 'green', 'blue', 'purple']


def main():
    for i in range(len(colors)):
        turtle.color(colors[i])
        x = 1
        for y in range(100):
            turtle.forward(10)
            turtle.right(100 - x)
            x += 1

    turtle.done()

if __name__ == '__main__':
    sys.exit(main())
