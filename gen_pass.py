import random
import string

generated_password = []

def generator(longueur = 15):

    for _ in range(longueur):
        random_number = random.randint(0,9)
        random_letter = random.choice(string.ascii_letters)
        random_char = random.choice(string.punctuation)


        random_append = random.choice([random_number, random_letter, random_char])

        generated_password.append(str(random_append))

    final_password = ''.join(generated_password)

    return (final_password, len(generated_password))

