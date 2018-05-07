import turtle

turtle.speed(0) # これがないとスピードめちゃ遅い

for i in range(100): # for文で動的描画を可能に
    turtle.circle(5*i) # 半径を等比数列に

turtle.exitonclick() # クリックでウィンドウ削除
