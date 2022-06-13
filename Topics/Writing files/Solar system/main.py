with open('planets.txt', 'w', encoding='utf-8') as sample:
    sample.writelines([f'{p}\n' for p in [
        'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus',
        'Neptune',
    ]])
    sample.close()
