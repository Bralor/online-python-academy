import random

def main():

    player = add_player()
    secret_word = choose_secret_word()
    progress, turns = hide_word(secret_word)

    while turns:
        state = show_current_state(player, progress, turns)
        turn = players_guess()
        return_word = evaluate(turn, secret_word, progress, turns)
        turns -= 1

        if '_' not in progress:
            show_current_state(player, progress, turns)
            print(f'Great, {player}! You are winner!')
            break
    
        elif '_' in progress and turns == 0:
            print(f'Unfortunatelly, {player}, you lose!')


def add_player():
    """Take string input as player name"""
    return input("Whats your name: ")


def choose_secret_word():
    """Choose a secret word from list/file and then return string"""
    loaded_words = open('words.txt', 'r')
    words_in_list = [w.strip() for w in loaded_words.readlines() if w.strip()]
    loaded_words.close()
    return random.choice(words_in_list)


def hide_word(word):
    """Take string as input a return hidden word"""
    return ['_'] * len(word), round(1.3 * len(word), 0)


def show_current_state(plr, prog, turn):
    """
    Inputs:
        1. plr - string player,
        2. prog - list progress,
        3. turn - float turns
    
    Output:
        Announce current state of the game.
    """
    txt = f'Player: {plr} | Hidden word: {prog} | Turns: {turn} |'
    sep = len(txt) * '-'
    print(sep, txt, sep, sep='\n')


def players_guess():
    """
    Inputs:
        -
    Outputs:
        Return user's input with guess
    """
    return input('Guess word: ')


def evaluate(guess, word, prog, turns):
    """
    Inputs: 
        1. guess - string turn,
        2. word - string secret_word,
        3. prog - list progress,
        4. turns - float turns
    
    Outputs:
        If the user's input is correct, return new updated var. progress.
        Otherwise do nothing
    """
    for index, letter in enumerate(word):
        if letter in guess:
            prog[index] = guess


main()