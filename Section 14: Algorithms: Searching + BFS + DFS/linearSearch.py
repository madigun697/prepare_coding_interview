beasts = ['Centaur', 'Godzilla', 'Mosura', 'Minotaur', 'Hydra', 'Nessie']

print(beasts.index('Godzilla'))

print([idx for idx, beast in enumerate(beasts) if beast == 'Godzilla'][0])

print([beast for beast in beasts if beast == 'Godzilla'][0])

print('Godzilla' in beasts)