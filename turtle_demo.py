from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(100)
    left(180-360/12)
    if abs(pos()) < 1:
        break
end_fill()
done()