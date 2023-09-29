##############################################
# -------------- Introduction -------------- #
##############################################

# In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to
# organize players, words, and points. We have provided you with two lists, letters and points. We would like to
# combine these two into a dictionary that would map a letter to its point value.


################## Scrabble ##################


letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
    "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


# let's create a dictionary, called letter_to_points, that has the elements of letters as the keys and the elements of
# points as the values by using zip, then add an element to the letter_to_points dictionary that has a key of " " and
# a point value of 0.


letters += [letter.lower() for letter in letters]
points *= 2
letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0


# Let's define a function, called score_word, that takes in a parameter word. It'll return how many points that word
# is worth.


def score_word(word):
    point_total = 0
    for letter in word:
        if letter in letter_to_points:
            point_total += letter_to_points.get(letter, 0)
    return point_total


# Let’s test this function!


print(score_word("BROWNIE"))  # 15


# Then create a dictionary, called player_to_words, that maps players to a list of the words they have played. This
# table represents the data to transcribe into our dictionary. Then create an empty dictionary called player_to_points
# to calculate the points:


player_to_words = {"player1": ["Blue", "TENNIS", "EXIT"],
                   "player2": ["EARTH", "EYES", "MACHINE"],
                   "player3": ["ERASER", "BELLY", "HUSKY"],
                   "player4": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}


# Then iterate through the items in player_to_words. Call each player and each list of words. Within our loop, create
# a variable called player_points and set it to 0.


def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
            player_to_points[player] = player_points
    return update_point_totals


# Our next funtcion would be play_word(). This function would take in a player and a word, and add that word to the list
# of words they’ve played


def play_word(player, word):
    if not word in player_to_words.values():
        if player in player_to_words:
            player_to_words[player].append(word)
            update_point_totals()
    return play_word


play_word("player1", "patates")
print(player_to_words)
print(player_to_points)
