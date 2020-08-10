
#player_1 = "Sam"
#player_2 = "Alex"
#current_round = 1

#print("Game on")
#print(f"Player 1: {player_1}")
#print(f"Player 2: {player_2}")
#print("--------------------------")

#if True:
#    pass

#print(f"Round {current_round}!")
#player_1_score = 10
#player_2_score = 13

#print(f"{player_2} wins with {player_2_score} to {player_1_score}")
#print("--------------------------")
#print(f"Round {current_round + 1}!")



print("Hello")
result_1 = input("Write number: ")
if result_1.replace(".", "", 1).replace("-", "", 1).isnumeric():
    result_1 = float(result_1)
    list = ["+", "-", "*", "/", "square", "sqrt"]
    print(list)
    oper = input("What do you want to do? ")
    if oper == list[0] or oper == list[1] or oper == list[2] or oper == list[3] or oper == list[4] or oper == list[5]:
        while oper != "=":
            list = ["+", "-", "*", "/", "square", "sqrt"]
            if oper == list[0] or oper == list[1] or oper == list[2] or oper == list[3] or oper == list[4] or oper ==list[5]:
                result_1 = result_1
            else:
                print("Learn to write!")
                break
            if oper == list[0] or oper == list[1] or oper == list[2] or oper == list[3]:
                num_2 = input("Write a number: ")
                if num_2.replace(".", "", 1).replace("-", "", 1).isnumeric():
                    num_2 = float(num_2)
                else:
                    print("Please write number!")
                    break

            def add(result_1, num_2):
                return result_1 + num_2

            def sub(result_1, num_2):
                return result_1 - num_2

            def mult(result_1, num_2):
                return result_1 * num_2

            def div(result_1, num_2):
                if num_2 == 0:
                    num_2 = num_2
                else:
                    return result_1 / num_2

            def square(result_1):
                return pow(result_1, 2)

            def sqrt(result_1):
                if result_1 < 0:
                    oper_1 = 0
                else:
                    return pow(result_1, 0.5)

            if oper == list[0]:
                result = add(result_1, num_2)
            elif oper == list[1]:
                result = sub(result_1, num_2)
            elif oper == list[2]:
                result = mult(result_1, num_2)
            elif oper == list[3]:
                result = div(result_1, num_2)
            elif oper == list[4]:
                result = square(result_1)
            else:
                result = sqrt(result_1)
            oper_1 = "+"
            if oper == list[3] and num_2 == 0:
                oper_1 = "="
            elif oper == list[5] and result_1 < 0:
                oper_1 = "="
            else:
                oper = input("What do you want to do? ")
                result_1 = 0 + float(result)
            if oper_1 == "=":
                print("Learn MATH!")
                break
            elif oper_1 == "+":
                num_2 = num_2
            elif oper == "=":
                print(result_1)
        if oper == "=":
            print(result_1)
    else:
        print("Learn to write!")
else:
    print("Please write number!")
