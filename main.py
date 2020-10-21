import requests




def value_players(data):
    print("How many players?")
    amount_of_players = int(input())
    print("\n\n")

    #store players in array
    player_array = []

    players = data["elements"]
    for player in players:
        player_calculated = [""] * 8  # [ first_name, last_name, form, price, total_points, points_per_game, total_points/price, points_per_game/price ]
        player_calculated[0] = player["first_name"]
        player_calculated[1] = player["second_name"]
        player_calculated[2] = float(player["form"])
        player_calculated[3] = float(player["now_cost"]) * 100
        player_calculated[4] = float(player["total_points"])
        player_calculated[5] = float(player["points_per_game"])

        # These two are different --> 7 accounts only matches player played while 6 doesnt
        player_calculated[6] = round( (player_calculated[4] / player_calculated[3]), 6 )      #* 10000      # total_points/price
        player_calculated[7] = round( (player_calculated[5] / player_calculated[3]), 6 )    #* 10000    # points_per_game/price

        #append to player_array
        player_array.append(player_calculated)

    # sorting
    player_array.sort(key=lambda x: x[6])
    player_array.reverse()


    #print players
    for i, player in enumerate(player_array):
        if i == amount_of_players:
            break
        else:
            print(i+1, ": ", player[0], " ", player[1])
            print("Form: ", player[2])
            print("Cost: ", player[3])
            print("Total Points: ", player[4])
            print("Points per game: ", player[5])
            print("--------------------------------")
            print("Total_Points / Cost: ", player[6])
            print("Points_per_Game / Cost: ", player[7])
            print("\n\n")






if __name__ == '__main__':
    URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
    data = requests.get(url = URL).json()

    print("Welcome to premier league fantasy assistant\n This program can help you with your premier league fantasy journey in many ways\n\n")
    while(True):
        print("To list best players for therir value (Have gotten the most amount of points for their price), input number '1' and press enter ")
        input_option = input()

        if input_option == "1":
            # Show best n amount of players for their value (Points/value)
            value_players(data)

        print("\n\n\n\n")
