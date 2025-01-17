import random

# Define an array of weapons with increasing levels of strength
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]


# Function to roll the dice (1-6) and validate input
def roll_dice():
    try:
        # Simulate rolling a six-sided die
        weaponRoll = random.randint(1, 6)
        print(f"You rolled a {weaponRoll}.")
        return weaponRoll
    except Exception as e:
        print(f"An error occurred while rolling the dice: {e}")
        return None


# Main execution
try:
    # Roll the dice to determine the selected weapon
    weaponRoll = roll_dice()
    if weaponRoll is None:
        raise ValueError("Invalid weapon roll.")

    # Hero's combat strength initially set to 0 + weaponRoll
    hero_combat_strength = weaponRoll

    # Use weaponRoll as an index to pick the weapon from the array
    selected_weapon = weapons[weaponRoll - 1]  # Adjust for 0-based indexing
    print(f"Your weapon is: {selected_weapon}")

    # Display weapon strength commentary based on conditions
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    # If the weapon rolled is not a Fist, display an additional message
    if selected_weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

except ValueError as ve:
    # Handle invalid dice roll or other value-related errors
    print(f"Error: Please enter a valid integer value: {ve}")
except IndexError:
    # This error will occur if weaponRoll is out of bounds
    print("Error: Invalid dice roll index. Please roll a value between 1 and 6.")
except Exception as e:
    # Handle unexpected errors
    print(f"An unexpected error occurred: {e}")
