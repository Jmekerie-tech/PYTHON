# import turtle
# import random

# wn = turtle.Screen()
# wn.bgcolor("black")
# wn.tracer(1)


# ball = turtle.Turtle()
# ball.shape("circle")
# ball.color("red")
# ball.penup()
# ball.speed(5)
# x = random.randint(-290, 290)
# y = random.randint(200, 400)
# ball.goto(x, y)
# ball.dy = 0
# ball.dx = random.randint(-3, 3)

# gravity = 0.1

# while True:
#     wn.update()

#     ball.dy -= gravity
#     ball.sety(ball.ycor() + ball.dy)

#     ball.setx(ball.xcor() + ball.dx)

#     if ball.xcor() > 300:
#         ball.dx *= -1
#     if ball.xcor() < -300:
#         ball.dx *= -1
#     if ball.ycor() < -300:
#         ball.dy *= -1

# wn.mainloop()




# import random

# while True:
#     # alegeri posibile
#     alegeri = ["foarfece", "piatra", "hartie"]

#     # acilea este oponentul
#     calculator = random.choice(alegeri)

#     # acilea santem noi marii barosani
#     eu = input("ce alegi boss?: ")
#     if eu not in alegeri:
#         eu = input("oi, esti atat de prost incat nu poti sa pui raspus corect? ")
#         if eu not in alegeri: 
#             print("nu esti bun de nimic")
#             break

#     # afisam raspunsurile din cutia pandorei
#     print(calculator)

#     if eu==calculator:
#         print("egalitate")
#     elif eu=="foafece":
#         if calculator=="piatra":
#             print("hahahahahaha ce noob esti")
#         elif calculator=="hartie":
#             print("din greseala ai castigat")
#     elif eu=="hartie":
#         if calculator=="foarfece":
#             print("hahahahahaha ce noob esti")
#         elif calculator=="piatra":
#             print("din greseala ai castigat")
#     elif eu=="piatra":
#         if calculator=="hartie":
#             print("hahahahahaha ce noob esti")
#         elif calculator=="foarfece":
#             print("din greseala ai castigat")

#     #Mai jucam?
#     continuam = input("vrei sa mai joci?: ")
#     if continuam != "da":
#         break
