print(*[
    '{} {}'.format(m, r - c)
    for m, r, c in zip(months, revenues, costs)
], sep='\n')
