import random, sys, time

PAUSE = 0.15

# These are the individual rows of the DNA animation:
ROWS = [
    #123456789 <- This is to measure the number of spaces:
    '         ##',  # Index 0 has no {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',  # Index 9 has no {}.
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']
    #123456789 <- This is to measure the number of spaces:

try:
    print('DNA Visualization')
    print('Press Ctrl-C to quit')
    time.sleep(2)
    row_index = 0

    while True:   # Main program loop.
        # Increment row_index to draw next row:
        row_index += 1
        if row_index == len(ROWS):
            row_index = 0
        # Row indexes 0 and 9 don't have nucleotides:
        if row_index == 0 or row_index == 9:
            print(ROWS[row_index])
            continue

        # Select random nucleotide pairs, guanine-cytosine and
        # adenine-thymine:
        random_selection = random.randint(1, 4)
        if random_selection == 1:
            left_nucleotide, right_nucleotide = 'A', 'T'
        elif random_selection == 2:
            left_nucleotide, right_nucleotide = 'T', 'A'
        elif random_selection == 3:
            left_nucleotide, right_nucleotide = 'C', 'G'
        elif random_selection == 4:
            left_nucleotide, right_nucleotide = 'G', 'C'
        
        # Print the row.
        print(ROWS[row_index].format(left_nucleotide, right_nucleotide))
        time.sleep(PAUSE)  # Add a slight pause.
except KeyboardInterrupt:
    sys.exit() # When Ctrl-C is pressed, end the program.
            

    
    