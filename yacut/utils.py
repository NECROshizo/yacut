from random import choices
from string import ascii_letters, digits


def get_unique_short_id(quantity=6):
    simbol = ascii_letters + digits
    return ''.join(choices(simbol, k=quantity))