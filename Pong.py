import turtle
#ventana
vn = turtle.Screen()
vn.title("Pong by Cazaa")
vn.bgcolor("black")
vn.setup(width=800, height = 600)
vn.tracer(0)
#Marcador
marcadorA=0
marcadorB=0

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("jugadorA:      jugadorB: 0",align = "center", font=("courier",30,"normal"))
#JugadorA
jugadorA = turtle.Turtle()
jugadorA.speed(2)
jugadorA.shape("square")
jugadorA.color("White")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid=5 ,  stretch_len=1)

#JugadorB

jugadorB = turtle.Turtle()
jugadorB.speed(2)
jugadorB.shape("square")
jugadorB.color("White")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid=5 ,  stretch_len=1)

#Pelota

Pelota = turtle.Turtle()
Pelota.speed(0)
Pelota.shape("square")
Pelota.color("White")
Pelota.penup()
#Movimiento Pelota
Pelota.dx = 1
Pelota.dy = 1

#linea
division = turtle.Turtle()
division.color("White")
division.goto(0,400)
division.goto(0,-400)

#Funciones para movimiento
def jugadorA_up():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)
def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

def jugadorB_up():
        y = jugadorB.ycor()
        y += 20
        jugadorB.sety(y)

def jugadorB_down():
        y = jugadorB.ycor()
        y -= 20
        jugadorB.sety(y)
#tecladospam
vn.listen()
vn.onkeypress(jugadorA_up ,"w")
vn.onkeypress(jugadorA_down ,"s")
vn.onkeypress(jugadorB_up ,"Up")
vn.onkeypress(jugadorB_down ,"Down")


#Movimiento pelota



while True:
    vn.update()
    Pelota.setx(Pelota.xcor()+ Pelota.dx)
    Pelota.sety(Pelota.ycor()+ Pelota.dy)

#Bordes
    if Pelota.ycor() > 290:
        Pelota.dy *= -1
    if Pelota.ycor() < -290:
        Pelota.dy *= -1

    #Bordes de/izq
    if Pelota.xcor() > 390:
        Pelota.goto(0, 0)
        Pelota.dx *= -1
        marcadorA +=1
        pen.clear()
        pen.write("jugadorA: {}    jugadorB: {} ".format(marcadorA,marcadorB),align="center", font=("courier", 30, "normal"))

    if Pelota.xcor() < -390:
        Pelota.goto(0, 0)
        Pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write("jugadorA: {}    jugadorB: {} ".format(marcadorA, marcadorB), align="center",
                  font=("courier", 30, "normal"))







    #Colisiones
    if ((Pelota.xcor() > 340 and Pelota.xcor() < 350)
            and (Pelota.ycor() < jugadorB.ycor() + 50
            and Pelota.ycor() > jugadorB.ycor() - 50)):
        Pelota.dx *= -1

    if ((Pelota.xcor() < - 340 and Pelota.xcor() > - 350)
            and (Pelota.ycor() < jugadorA.ycor() + 50
            and Pelota.ycor() > jugadorA.ycor() - 50)):
        Pelota.dx *= -1
