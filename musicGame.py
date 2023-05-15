import random

NOTES = {
    'C': 0, 
    'C#': 1, 'Db': 1, 
    'D': 2, 
    'D#': 3, 'Eb': 3, 
    'E': 4, 
    'F': 5, 
    'F#': 6, 'Gb': 6, 
    'G': 7, 
    'G#': 8, 'Ab': 8, 
    'A': 9, 
    'A#': 10, 'Bb': 10, 
    'B': 11
}

def get_random_notes():

    notes = list(NOTES.keys())
    note1, note2 = random.sample(notes, 2)
    return note1, note2

def get_semitones_between_notes(note1, note2):

    semitones = (NOTES[note2] - NOTES[note1]) % 12
    return semitones

def play_game():

    while True:
        note1, note2 = get_random_notes()
        answer = get_semitones_between_notes(note1, note2)
        guess = None
        while guess != answer:
            guess = input(f"How many semitones are between {note1} and {note2}? ")
            if guess.lower() == 'give up':
                print(f"The correct answer is {answer}.")
                break
            try:
                guess = int(guess)
                if guess == answer:
                    print("Correct!")
                else:
                    print("Incorrect. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number or 'give up'.")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() != 'y':
            break

if __name__ == '__main__':
    play_game()
