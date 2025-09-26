import random

def generate_nz_lotto():
    # Generate 6 unique main numbers from 1 to 40
    main_numbers = random.sample(range(1, 41), 6)
    main_numbers.sort()

    # Generate a bonus number from the remaining pool
    remaining_numbers = list(set(range(1, 41)) - set(main_numbers))
    bonus_number = random.choice(remaining_numbers)

    # Generate a Powerball number from 1 to 10
    powerball = random.randint(1, 10)

    return {
        "Main Numbers": main_numbers,
        "Bonus Number": bonus_number,
        "Powerball": powerball
    }

# Example usage
lotto_numbers = generate_nz_lotto()
print("🎟 Your NZ Lotto Numbers:")
print("Main:", lotto_numbers["Main Numbers"])
print("Bonus:", lotto_numbers["Bonus Number"])
print("Powerball:", lotto_numbers["Powerball"])


def generate_nz_lotto():
    # Generate 6 unique main numbers from 1 to 40
    main_numbers = random.sample(range(1, 41), 6)
    main_numbers.sort()

    # Generate a bonus number from the remaining pool
    remaining_numbers = list(set(range(1, 41)) - set(main_numbers))
    bonus_number = random.choice(remaining_numbers)

    # Generate a Powerball number from 1 to 10
    powerball = random.randint(1, 10)

    return {
        "Main Numbers": main_numbers,
        "Bonus Number": bonus_number,
        "Powerball": powerball
    }

# Example usage
lotto_numbers = generate_nz_lotto()
print("🎟 Your NZ Lotto Numbers:")
print("Main:", lotto_numbers["Main Numbers"])
print("Bonus:", lotto_numbers["Bonus Number"])
print("Powerball:", lotto_numbers["Powerball"])
