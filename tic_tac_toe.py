from random import shuffle

from models.dashboard import Dashboard
from models.player import Player,VALID_OPTIONS


def get_players():
    player_list = []
    count = 1
    while len(player_list) < 2:
        name = input(f"Please insert your name, player {count} (optional): ")
        if not len(name):
            name = f'player {count}'
            count = count + 1

        if not len(player_list):
            selection = input("Please insert your selection to play, {name} ('x' or 'o' optional): ")

            while selection not in VALID_OPTIONS and selection != "":
                selection = input(f"Please select a valid option 'x' or 'o', not {selection}.")

        else:
            selection = 'x' if 'x' not in player_list[0].mark else 'o'

        new_player = Player.create(mark=selection, name=name)
        player_list.append(new_player)

    return player_list

def play():
    player1, player2 = get_players()
    print("\033[H\033[2J", end="")
    print(f"Wellcome Players!\n{player1.name} ({player1.mark}) vs {player2.name} ({player2.mark})\nLet's go!!\n")
    dashboard = Dashboard()

    turns = [True, False]
    shuffle(turns)
    player1.my_turn, player2.my_turn = turns

    while not player1.winner and not player2.winner and not dashboard.full:
        cell = False

        player = player1 if player1.my_turn else player2

        print(f"It's your turn {player.name}, playing with {player.mark}.")
        mark = player.mark

        while cell not in dashboard.valid_cells and len(dashboard.valid_cells):
            cell = input(f"Please, select a cell to play.\n{dashboard.valid_cells}: ")

        print("\033[H\033[2J", end="")

        position = '({}, {})'.format(cell[0], cell[1])
        print(f"{player.name}, you have selected '{mark}' for position {position}\n\n")

        dashboard.update_valid_cells(cell)

        if cell == "11":
            dashboard.x11 = mark

        elif cell == "12":
            dashboard.x12 = mark

        elif cell == "13":
            dashboard.x13 = mark

        if cell == "21":
            dashboard.x21 = mark

        elif cell == "22":
            dashboard.x22 = mark

        elif cell == "23":
            dashboard.x23 = mark

        if cell == "31":
            dashboard.x31 = mark

        elif cell == "32":
            dashboard.x32 = mark

        elif cell == "33":
            dashboard.x33 = mark

        player1.winner, player2.winner = ([True, False]
                                          if dashboard.win(player1.mark)
                                          else [False, True]
                                          if dashboard.win(player2.mark)
                                          else [False, False]
        )

        player1.my_turn, player2.my_turn = [False, True] if player1.my_turn else [True, False]

    winner = player1.name if player1.winner else player2.name if player2.winner else False

    if winner:
        print(f"Congratulations {winner}!!\n\n")
    elif dashboard.full:
        print("DRAW!!\n\n")

def main():
    continue_playing = True
    while continue_playing:
        continue_playing = False
        play()
        yes_answer = ["s", "S", "y", "Y", "Si", "SI", "si", "Yes", "yes", "YES"]
        no_answer = ["n", "N", "No", "NO", "no"]
        valid_answer = []
        valid_answer.extend(yes_answer)
        valid_answer.extend(no_answer)
        answer = input("Another game? [y/n]: ")
        count = 0

        while answer not in valid_answer and count < 3:
            answer = input("Another game? [y/n]: ")
            count = count + 1

        if count == 3:
            print("Too many bad answers. Bye!")

        if answer in yes_answer:
            continue_playing = True

    print("Bye!")


if __name__ == "__main__":
    main()
    
