#!/usr/bin/env python3

import random

#winner is A or B, microbe is species
def output_statement(user_winner, microbe_winner):
    microbe_statement = ''
    user_winner = user_winner
    microbe_winner = microbe_winner

    #winning headers list
    winning_headers = ["Good choice! That's a strong microbe", "Nice going - you're super smart", "Wowwww, your microbe crushed it"]

    #losing headers list
    losing_headers = ["Nice try! Better luck next time", "Ooof, that was a tough opponent", "Wow, your opponent was really strong"]

    #if microbe winner is me, add random winning header to string, if microbe winner is other, add random losing eader to string
    if user_winner == 'A':
        header = random.choice(winning_headers)
        microbe_statement = header + '\n'

    if user_winner == 'B':
        header = random.choice(losing_headers)
        microbe_statement = header + '\n'

    if user_winner == 'tie':
        header = 'That was a good fight! The microbes were tied.'
        microbe_statement = header + '\n'

    winner_statement = f'{microbe_winner} wins!'
    microbe_statement = microbe_statement + '\n' + winner_statement + '\n'
    
    #if the fight is a tie, the microbe winner will have 'and' in it so don't add anything else to the microbe statement
    if "and" in microbe_winner:
        microbe_statement = microbe_statement
    
    else:
        #open species_info.txt file and extract line with microbe name listed, store in microbe_info
        with open("species_info.txt", "r") as species_info_in:
            for line in species_info_in:
                line = line.rstrip()
                if line.startswith(microbe_winner):
                    microbe_info = line

        #extract microbe info from microbe_info excluding everything outside the quotes ""
        start_index = 1 + int(microbe_info.index('\"')) #extract index of first quote "
        microbe_info = microbe_info[start_index:-1] #extract substring from microbe info

        microbe_statement = microbe_statement + '\n' + microbe_info + '\n'
    
    return microbe_statement
