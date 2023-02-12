import turtle
import pandas

screen = turtle.Screen()
screen.title("Indonesia Province Game")
img = "D:\Documents/Haikal/Project Python/Indonesia Province Game/blank_Indo_img.gif"
screen.addshape(img)
turtle.shape(img)


def name_of_island():
    global turtle
    global t
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(-139, 82)
    t.write("Kalimantan", font=("Courier", 8, "bold"))
    t.goto(66, -8)
    t.write("Sulawesi", font=("Courier", 8, "bold"))
name_of_island()


data = pandas.read_csv(
    "D:\Documents/Haikal/Project Python/Indonesia Province Game/11_Province.csv")
all_province = data.province.to_list()
guess = []


while len(guess) < 11:
    user_guess = screen.textinput(
        title=f"{len(guess)}/11 Guess the Province", prompt="Enter a guess").title()

    if user_guess == "Exit":
        missing_province = []
        for province in all_province:
            if province not in guess:
                missing_province.append(province)
        new_data = pandas.DataFrame(missing_province)
        new_data.to_csv("Missing_province.csv")
        break
    
    if user_guess in all_province:
        guess.append(user_guess)
        t.penup()
        t.hideturtle()
        new_data = data[data.province == user_guess]
        t.goto(int(new_data.x), int(new_data.y))
        t.write(user_guess)