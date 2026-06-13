# Name: Devin G. Hyden
# Date: 12 June 2026
# Assignment: Module 1.3 Assignment
# Purpose of Code: Recreate the counting song 100 bottles of beer on the wall

def beer_counting_song(bottles):
    # Loop backwards from the starting number down to 1
    for current_bottles in range (bottles, 0, -1):
        # Checks if we are on the last bottle to change bottles to bottle
        if current_bottles == 1:
            print(f'{current_bottles} bottle of beer on the wall, {current_bottles} bottle of beer.')
        else:
            print(f'{current_bottles} bottles of beer on the wall, {current_bottles} bottle(s) of beer.')
        # Calculate the remaining bottles for the other half of the lyric
        remaining = current_bottles -1
        print(f'Take one down and pass it around, {remaining} bottle(s) of beer on the wall.\n')


def main():
    # Prompt the user for the number of bottles while converting it from a sting to an integer
    user_input = int(input("Enter number of bottles: "))
    beer_counting_song(user_input)
    # Main function resumes here after the beer_counting_song function finishes counting down
    print("Time to buy more bottles of beer.")


# Makes sure the main program runs when the script is executed
if __name__ == "__main__":
    main()
