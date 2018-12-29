# List of samples
test_samples = [
    {
        'before': (1, 1, 1, 0),
        'instruction': (4, 1, 0, 0),
        'after': (1, 1, 1, 0)
    },
    {
        'before': (1, 1, 0, 1),
        'instruction': (5, 1, 3, 3),
        'after': (1, 1, 0, 1)
    },
    {
        'before': (3, 2, 3, 1),
        'instruction': (14, 2, 1, 3),
        'after': (3, 2, 3, 2)
    },
    {
        'before': (0, 1, 2, 1),
        'instruction': (5, 1, 3, 0),
        'after': (1, 1, 2, 1)
    },
    {
        'before': (2, 1, 2, 3),
        'instruction': (1, 3, 3, 2),
        'after': (2, 1, 3, 3)
    },
    {
        'before': (1, 0, 2, 0),
        'instruction': (11, 0, 2, 1),
        'after': (1, 2, 2, 0)
    },
    {
        'before': (1, 2, 1, 1),
        'instruction': (8, 2, 3, 0),
        'after': (1, 2, 1, 1)
    },
    {
        'before': (1, 0, 3, 2),
        'instruction': (10, 0, 3, 3),
        'after': (1, 0, 3, 3)
    },
    {
        'before': (0, 1, 3, 1),
        'instruction': (3, 0, 0, 0),
        'after': (0, 1, 3, 1)
    },
    {
        'before': (2, 1, 3, 2),
        'instruction': (15, 0, 1, 2),
        'after': (2, 1, 3, 2)
    },
    {
        'before': (2, 1, 2, 1),
        'instruction': (1, 2, 0, 2),
        'after': (2, 1, 2, 1)
    },
    {
        'before': (0, 0, 2, 0),
        'instruction': (3, 0, 0, 2),
        'after': (0, 0, 0, 0)
    },
    {
        'before': (1, 1, 3, 2),
        'instruction': (10, 0, 3, 3),
        'after': (1, 1, 3, 3)
    },
    {
        'before': (2, 3, 2, 3),
        'instruction': (14, 3, 2, 3),
        'after': (2, 3, 2, 2)
    },
    {
        'before': (0, 1, 3, 2),
        'instruction': (10, 1, 3, 0),
        'after': (3, 1, 3, 2)
    },
    {
        'before': (1, 1, 1, 0),
        'instruction': (4, 1, 0, 2),
        'after': (1, 1, 1, 0)
    },
    {
        'before': (1, 2, 3, 2),
        'instruction': (12, 2, 2, 3),
        'after': (1, 2, 3, 2)
    },
    {
        'before': (3, 2, 1, 1),
        'instruction': (8, 2, 3, 3),
        'after': (3, 2, 1, 1)
    },
    {
        'before': (0, 1, 3, 2),
        'instruction': (10, 1, 3, 2),
        'after': (0, 1, 3, 2)
    },
    {
        'before': (0, 3, 3, 0),
        'instruction': (12, 2, 2, 3),
        'after': (0, 3, 3, 2)
    },
    {
        'before': (2, 2, 2, 0),
        'instruction': (1, 2, 0, 0),
        'after': (2, 2, 2, 0)
    },
    {
        'before': (0, 2, 0, 3),
        'instruction': (11, 3, 3, 2),
        'after': (0, 2, 9, 3)
    },
    {
        'before': (0, 1, 3, 2),
        'instruction': (6, 3, 1, 1),
        'after': (0, 3, 3, 2)
    },
    {
        'before': (1, 0, 2, 0),
        'instruction': (2, 2, 3, 0),
        'after': (3, 0, 2, 0)
    },
    {
        'before': (3, 3, 1, 1),
        'instruction': (8, 2, 3, 1),
        'after': (3, 1, 1, 1)
    },
    {
        'before': (0, 1, 0, 2),
        'instruction': (3, 0, 0, 0),
        'after': (0, 1, 0, 2)
    },
    {
        'before': (1, 1, 3, 2),
        'instruction': (10, 0, 3, 0),
        'after': (3, 1, 3, 2)
    },
    {
        'before': (0, 0, 1, 1),
        'instruction': (3, 0, 0, 2),
        'after': (0, 0, 0, 1)
    },
    {
        'before': (0, 1, 1, 2),
        'instruction': (3, 0, 0, 2),
        'after': (0, 1, 0, 2)
    },
    {
        'before': (0, 1, 1, 1),
        'instruction': (3, 0, 0, 3),
        'after': (0, 1, 1, 0)
    },
    {
        'before': (1, 1, 1, 1),
        'instruction': (5, 1, 3, 1),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (1, 1, 3, 3),
        'instruction': (4, 1, 0, 3),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (3, 3, 1, 1),
        'instruction': (13, 2, 3, 3),
        'after': (3, 3, 1, 3)
    },
    {
        'before': (3, 1, 1, 3),
        'instruction': (9, 2, 3, 0),
        'after': (3, 1, 1, 3)
    },
    {
        'before': (1, 1, 2, 0),
        'instruction': (11, 1, 2, 1),
        'after': (1, 2, 2, 0)
    },
    {
        'before': (2, 3, 2, 2),
        'instruction': (1, 2, 0, 2),
        'after': (2, 3, 2, 2)
    },
    {
        'before': (0, 3, 2, 3),
        'instruction': (1, 2, 0, 1),
        'after': (0, 2, 2, 3)
    },
    {
        'before': (1, 1, 2, 0),
        'instruction': (15, 1, 2, 1),
        'after': (1, 3, 2, 0)
    },
    {
        'before': (0, 3, 1, 3),
        'instruction': (9, 2, 3, 1),
        'after': (0, 3, 1, 3)
    },
    {
        'before': (3, 1, 2, 0),
        'instruction': (1, 2, 2, 3),
        'after': (3, 1, 2, 2)
    },
    {
        'before': (0, 2, 1, 3),
        'instruction': (9, 2, 3, 0),
        'after': (3, 2, 1, 3)
    },
    {
        'before': (0, 1, 0, 1),
        'instruction': (13, 1, 3, 3),
        'after': (0, 1, 0, 3)
    },
    {
        'before': (1, 1, 1, 2),
        'instruction': (4, 1, 0, 0),
        'after': (1, 1, 1, 2)
    },
    {
        'before': (2, 2, 3, 1),
        'instruction': (6, 3, 2, 0),
        'after': (3, 2, 3, 1)
    },
    {
        'before': (3, 3, 1, 2),
        'instruction': (10, 2, 3, 1),
        'after': (3, 3, 1, 2)
    },
    {
        'before': (3, 2, 3, 3),
        'instruction': (11, 3, 3, 1),
        'after': (3, 9, 3, 3)
    },
    {
        'before': (0, 0, 2, 3),
        'instruction': (11, 3, 3, 3),
        'after': (0, 0, 2, 9)
    },
    {
        'before': (0, 1, 0, 0),
        'instruction': (0, 3, 1, 3),
        'after': (0, 1, 0, 1)
    },
    {
        'before': (3, 3, 0, 3),
        'instruction': (11, 0, 3, 0),
        'after': (9, 3, 0, 3)
    },
    {
        'before': (2, 1, 3, 1),
        'instruction': (5, 1, 3, 1),
        'after': (2, 1, 3, 1)
    },
    {
        'before': (1, 1, 2, 3),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 2, 3)
    },
    {
        'before': (2, 3, 3, 3),
        'instruction': (11, 0, 3, 0),
        'after': (6, 3, 3, 3)
    },
    {
        'before': (1, 2, 2, 1),
        'instruction': (13, 0, 3, 2),
        'after': (1, 2, 3, 1)
    },
    {
        'before': (0, 1, 3, 2),
        'instruction': (3, 0, 0, 3),
        'after': (0, 1, 3, 0)
    },
    {
        'before': (3, 2, 3, 2),
        'instruction': (14, 2, 3, 3),
        'after': (3, 2, 3, 2)
    },
    {
        'before': (1, 1, 2, 2),
        'instruction': (6, 3, 1, 2),
        'after': (1, 1, 3, 2)
    },
    {
        'before': (0, 2, 3, 2),
        'instruction': (3, 0, 0, 1),
        'after': (0, 0, 3, 2)
    },
    {
        'before': (3, 2, 2, 3),
        'instruction': (14, 3, 2, 2),
        'after': (3, 2, 2, 3)
    },
    {
        'before': (2, 1, 1, 2),
        'instruction': (15, 0, 1, 1),
        'after': (2, 3, 1, 2)
    },
    {
        'before': (1, 1, 1, 3),
        'instruction': (4, 1, 0, 3),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (1, 3, 2, 3),
        'instruction': (1, 2, 2, 0),
        'after': (2, 3, 2, 3)
    },
    {
        'before': (1, 1, 2, 1),
        'instruction': (4, 1, 0, 0),
        'after': (1, 1, 2, 1)
    },
    {
        'before': (1, 1, 3, 1),
        'instruction': (13, 0, 3, 1),
        'after': (1, 3, 3, 1)
    },
    {
        'before': (1, 0, 2, 1),
        'instruction': (8, 3, 3, 1),
        'after': (1, 1, 2, 1)
    },
    {
        'before': (3, 3, 2, 1),
        'instruction': (6, 3, 2, 1),
        'after': (3, 3, 2, 1)
    },
    {
        'before': (3, 3, 2, 3),
        'instruction': (14, 0, 2, 2),
        'after': (3, 3, 2, 3)
    },
    {
        'before': (1, 1, 1, 1),
        'instruction': (5, 1, 3, 0),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (0, 1, 2, 0),
        'instruction': (2, 2, 3, 0),
        'after': (3, 1, 2, 0)
    },
    {
        'before': (0, 2, 1, 3),
        'instruction': (7, 0, 3, 2),
        'after': (0, 2, 0, 3)
    },
    {
        'before': (2, 1, 0, 0),
        'instruction': (13, 1, 3, 1),
        'after': (2, 3, 0, 0)
    },
    {
        'before': (0, 2, 2, 1),
        'instruction': (15, 0, 2, 1),
        'after': (0, 2, 2, 1)
    },
    {
        'before': (2, 2, 3, 0),
        'instruction': (14, 2, 0, 3),
        'after': (2, 2, 3, 2)
    },
    {
        'before': (0, 1, 3, 1),
        'instruction': (5, 1, 3, 0),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (1, 1, 3, 1),
        'instruction': (5, 1, 3, 0),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (0, 1, 3, 1),
        'instruction': (12, 2, 2, 1),
        'after': (0, 2, 3, 1)
    },
    {
        'before': (1, 3, 2, 1),
        'instruction': (11, 1, 2, 2),
        'after': (1, 3, 6, 1)
    },
    {
        'before': (3, 2, 3, 0),
        'instruction': (2, 1, 3, 3),
        'after': (3, 2, 3, 3)
    },
    {
        'before': (0, 1, 3, 1),
        'instruction': (5, 1, 3, 1),
        'after': (0, 1, 3, 1)
    },
    {
        'before': (1, 2, 2, 2),
        'instruction': (11, 0, 2, 1),
        'after': (1, 2, 2, 2)
    },
    {
        'before': (3, 0, 2, 1),
        'instruction': (6, 3, 2, 1),
        'after': (3, 3, 2, 1)
    },
    {
        'before': (1, 1, 2, 0),
        'instruction': (4, 1, 0, 0),
        'after': (1, 1, 2, 0)
    },
    {
        'before': (0, 2, 1, 0),
        'instruction': (3, 0, 0, 1),
        'after': (0, 0, 1, 0)
    },
    {
        'before': (0, 2, 0, 0),
        'instruction': (2, 1, 3, 3),
        'after': (0, 2, 0, 3)
    },
    {
        'before': (1, 1, 1, 0),
        'instruction': (4, 1, 0, 3),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (1, 0, 2, 2),
        'instruction': (15, 0, 2, 2),
        'after': (1, 0, 3, 2)
    },
    {
        'before': (0, 0, 2, 1),
        'instruction': (3, 0, 0, 1),
        'after': (0, 0, 2, 1)
    },
    {
        'before': (2, 1, 0, 3),
        'instruction': (0, 2, 1, 2),
        'after': (2, 1, 1, 3)
    },
    {
        'before': (1, 0, 2, 0),
        'instruction': (13, 0, 3, 1),
        'after': (1, 3, 2, 0)
    },
    {
        'before': (0, 0, 3, 3),
        'instruction': (12, 2, 2, 1),
        'after': (0, 2, 3, 3)
    },
    {
        'before': (2, 1, 3, 1),
        'instruction': (5, 1, 3, 0),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (0, 1, 0, 3),
        'instruction': (7, 0, 2, 2),
        'after': (0, 1, 0, 3)
    },
    {
        'before': (3, 0, 2, 0),
        'instruction': (1, 2, 2, 2),
        'after': (3, 0, 2, 0)
    },
    {
        'before': (2, 1, 1, 1),
        'instruction': (5, 1, 3, 3),
        'after': (2, 1, 1, 1)
    },
    {
        'before': (3, 1, 0, 2),
        'instruction': (10, 1, 3, 0),
        'after': (3, 1, 0, 2)
    },
    {
        'before': (3, 1, 2, 0),
        'instruction': (0, 3, 1, 2),
        'after': (3, 1, 1, 0)
    },
    {
        'before': (3, 1, 2, 1),
        'instruction': (5, 1, 3, 1),
        'after': (3, 1, 2, 1)
    },
    {
        'before': (2, 2, 3, 1),
        'instruction': (6, 3, 2, 2),
        'after': (2, 2, 3, 1)
    },
    {
        'before': (0, 1, 2, 1),
        'instruction': (5, 1, 3, 1),
        'after': (0, 1, 2, 1)
    },
    {
        'before': (2, 2, 2, 3),
        'instruction': (11, 3, 3, 1),
        'after': (2, 9, 2, 3)
    },
    {
        'before': (2, 1, 1, 2),
        'instruction': (2, 0, 3, 0),
        'after': (3, 1, 1, 2)
    },
    {
        'before': (1, 1, 0, 2),
        'instruction': (10, 1, 3, 0),
        'after': (3, 1, 0, 2)
    },
    {
        'before': (1, 1, 3, 1),
        'instruction': (4, 1, 0, 3),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (0, 2, 2, 1),
        'instruction': (3, 0, 0, 2),
        'after': (0, 2, 0, 1)
    },
    {
        'before': (1, 1, 0, 2),
        'instruction': (6, 3, 1, 0),
        'after': (3, 1, 0, 2)
    },
    {
        'before': (0, 0, 0, 3),
        'instruction': (7, 0, 3, 1),
        'after': (0, 0, 0, 3)
    },
    {
        'before': (2, 1, 2, 2),
        'instruction': (6, 3, 1, 1),
        'after': (2, 3, 2, 2)
    },
    {
        'before': (0, 1, 2, 1),
        'instruction': (5, 1, 3, 2),
        'after': (0, 1, 1, 1)
    },
    {
        'before': (2, 0, 3, 3),
        'instruction': (11, 0, 3, 2),
        'after': (2, 0, 6, 3)
    },
    {
        'before': (0, 3, 0, 0),
        'instruction': (3, 0, 0, 2),
        'after': (0, 3, 0, 0)
    },
    {
        'before': (3, 3, 1, 2),
        'instruction': (10, 2, 3, 2),
        'after': (3, 3, 3, 2)
    },
    {
        'before': (1, 1, 3, 0),
        'instruction': (13, 1, 3, 3),
        'after': (1, 1, 3, 3)
    },
    {
        'before': (2, 1, 0, 1),
        'instruction': (0, 2, 1, 1),
        'after': (2, 1, 0, 1)
    },
    {
        'before': (2, 2, 2, 1),
        'instruction': (6, 3, 2, 1),
        'after': (2, 3, 2, 1)
    },
    {
        'before': (2, 1, 2, 0),
        'instruction': (2, 0, 3, 1),
        'after': (2, 3, 2, 0)
    },
    {
        'before': (1, 2, 3, 3),
        'instruction': (11, 2, 3, 1),
        'after': (1, 9, 3, 3)
    },
    {
        'before': (0, 1, 1, 0),
        'instruction': (7, 0, 3, 2),
        'after': (0, 1, 0, 0)
    },
    {
        'before': (0, 2, 1, 1),
        'instruction': (3, 0, 0, 1),
        'after': (0, 0, 1, 1)
    },
    {
        'before': (1, 1, 2, 3),
        'instruction': (9, 1, 3, 3),
        'after': (1, 1, 2, 3)
    },
    {
        'before': (3, 0, 1, 3),
        'instruction': (1, 3, 0, 3),
        'after': (3, 0, 1, 3)
    },
    {
        'before': (0, 3, 1, 2),
        'instruction': (10, 2, 3, 0),
        'after': (3, 3, 1, 2)
    },
    {
        'before': (2, 2, 1, 3),
        'instruction': (1, 3, 3, 2),
        'after': (2, 2, 3, 3)
    },
    {
        'before': (2, 2, 2, 1),
        'instruction': (6, 3, 2, 3),
        'after': (2, 2, 2, 3)
    },
    {
        'before': (0, 2, 2, 2),
        'instruction': (1, 2, 0, 0),
        'after': (2, 2, 2, 2)
    },
    {
        'before': (0, 1, 3, 2),
        'instruction': (12, 2, 2, 0),
        'after': (2, 1, 3, 2)
    },
    {
        'before': (0, 2, 1, 0),
        'instruction': (3, 0, 0, 3),
        'after': (0, 2, 1, 0)
    },
    {
        'before': (1, 1, 3, 1),
        'instruction': (4, 1, 0, 2),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (2, 2, 2, 1),
        'instruction': (8, 3, 3, 0),
        'after': (1, 2, 2, 1)
    },
    {
        'before': (1, 1, 3, 1),
        'instruction': (12, 2, 2, 3),
        'after': (1, 1, 3, 2)
    },
    {
        'before': (3, 3, 3, 1),
        'instruction': (6, 3, 2, 3),
        'after': (3, 3, 3, 3)
    },
    {
        'before': (2, 0, 3, 2),
        'instruction': (14, 2, 3, 0),
        'after': (2, 0, 3, 2)
    },
    {
        'before': (2, 1, 3, 2),
        'instruction': (12, 2, 2, 2),
        'after': (2, 1, 2, 2)
    },
    {
        'before': (1, 0, 1, 1),
        'instruction': (8, 2, 3, 2),
        'after': (1, 0, 1, 1)
    },
    {
        'before': (0, 2, 0, 2),
        'instruction': (7, 0, 3, 3),
        'after': (0, 2, 0, 0)
    },
    {
        'before': (1, 1, 2, 3),
        'instruction': (9, 1, 3, 0),
        'after': (3, 1, 2, 3)
    },
    {
        'before': (1, 2, 2, 1),
        'instruction': (15, 1, 2, 0),
        'after': (4, 2, 2, 1)
    },
    {
        'before': (1, 1, 3, 3),
        'instruction': (9, 0, 3, 3),
        'after': (1, 1, 3, 3)
    },
    {
        'before': (2, 3, 0, 3),
        'instruction': (15, 2, 3, 0),
        'after': (3, 3, 0, 3)
    },
    {
        'before': (1, 1, 3, 3),
        'instruction': (1, 3, 3, 0),
        'after': (3, 1, 3, 3)
    },
    {
        'before': (0, 2, 3, 2),
        'instruction': (7, 0, 1, 0),
        'after': (0, 2, 3, 2)
    },
    {
        'before': (3, 1, 1, 0),
        'instruction': (0, 3, 1, 0),
        'after': (1, 1, 1, 0)
    },
    {
        'before': (0, 3, 2, 0),
        'instruction': (1, 2, 2, 3),
        'after': (0, 3, 2, 2)
    },
    {
        'before': (0, 0, 1, 1),
        'instruction': (8, 2, 3, 1),
        'after': (0, 1, 1, 1)
    },
    {
        'before': (0, 1, 3, 0),
        'instruction': (12, 2, 2, 3),
        'after': (0, 1, 3, 2)
    },
    {
        'before': (3, 0, 1, 2),
        'instruction': (10, 2, 3, 3),
        'after': (3, 0, 1, 3)
    },
    {
        'before': (1, 1, 0, 0),
        'instruction': (4, 1, 0, 0),
        'after': (1, 1, 0, 0)
    },
    {
        'before': (0, 3, 2, 3),
        'instruction': (7, 0, 3, 0),
        'after': (0, 3, 2, 3)
    },
    {
        'before': (0, 2, 3, 0),
        'instruction': (3, 0, 0, 0),
        'after': (0, 2, 3, 0)
    },
    {
        'before': (0, 2, 0, 3),
        'instruction': (1, 3, 0, 0),
        'after': (3, 2, 0, 3)
    },
    {
        'before': (3, 3, 1, 2),
        'instruction': (10, 2, 3, 3),
        'after': (3, 3, 1, 3)
    },
    {
        'before': (1, 1, 2, 2),
        'instruction': (6, 3, 1, 3),
        'after': (1, 1, 2, 3)
    },
    {
        'before': (0, 1, 1, 2),
        'instruction': (6, 3, 1, 3),
        'after': (0, 1, 1, 3)
    },
    {
        'before': (0, 0, 2, 3),
        'instruction': (15, 0, 2, 0),
        'after': (2, 0, 2, 3)
    },
    {
        'before': (1, 1, 3, 2),
        'instruction': (14, 2, 3, 1),
        'after': (1, 2, 3, 2)
    },
    {
        'before': (0, 2, 0, 1),
        'instruction': (7, 0, 1, 1),
        'after': (0, 0, 0, 1)
    },
    {
        'before': (0, 1, 2, 1),
        'instruction': (6, 3, 2, 2),
        'after': (0, 1, 3, 1)
    },
    {
        'before': (2, 1, 0, 0),
        'instruction': (2, 0, 3, 3),
        'after': (2, 1, 0, 3)
    },
    {
        'before': (3, 1, 3, 1),
        'instruction': (5, 1, 3, 0),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (2, 1, 3, 1),
        'instruction': (6, 3, 2, 2),
        'after': (2, 1, 3, 1)
    },
    {
        'before': (3, 0, 3, 1),
        'instruction': (12, 2, 2, 0),
        'after': (2, 0, 3, 1)
    },
    {
        'before': (0, 2, 2, 3),
        'instruction': (3, 0, 0, 0),
        'after': (0, 2, 2, 3)
    },
    {
        'before': (1, 1, 3, 2),
        'instruction': (6, 3, 1, 3),
        'after': (1, 1, 3, 3)
    },
    {
        'before': (3, 1, 1, 2),
        'instruction': (10, 1, 3, 1),
        'after': (3, 3, 1, 2)
    },
    {
        'before': (1, 1, 2, 3),
        'instruction': (15, 2, 1, 0),
        'after': (3, 1, 2, 3)
    },
    {
        'before': (2, 0, 3, 3),
        'instruction': (14, 2, 0, 2),
        'after': (2, 0, 2, 3)
    },
    {
        'before': (1, 1, 1, 2),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 1, 2)
    },
    {
        'before': (0, 1, 2, 0),
        'instruction': (7, 0, 2, 2),
        'after': (0, 1, 0, 0)
    },
    {
        'before': (0, 3, 0, 3),
        'instruction': (3, 0, 0, 0),
        'after': (0, 3, 0, 3)
    },
    {
        'before': (3, 1, 0, 0),
        'instruction': (0, 2, 1, 0),
        'after': (1, 1, 0, 0)
    },
    {
        'before': (1, 1, 2, 0),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 2, 0)
    },
    {
        'before': (1, 1, 2, 0),
        'instruction': (4, 1, 0, 2),
        'after': (1, 1, 1, 0)
    },
    {
        'before': (1, 1, 0, 2),
        'instruction': (0, 2, 1, 3),
        'after': (1, 1, 0, 1)
    },
    {
        'before': (1, 1, 1, 2),
        'instruction': (6, 3, 1, 3),
        'after': (1, 1, 1, 3)
    },
    {
        'before': (0, 3, 0, 2),
        'instruction': (3, 0, 0, 0),
        'after': (0, 3, 0, 2)
    },
    {
        'before': (0, 0, 3, 2),
        'instruction': (7, 0, 1, 2),
        'after': (0, 0, 0, 2)
    },
    {
        'before': (1, 3, 3, 2),
        'instruction': (12, 2, 2, 3),
        'after': (1, 3, 3, 2)
    },
    {
        'before': (0, 3, 3, 2),
        'instruction': (3, 0, 0, 2),
        'after': (0, 3, 0, 2)
    },
    {
        'before': (0, 1, 0, 3),
        'instruction': (1, 3, 0, 3),
        'after': (0, 1, 0, 3)
    },
    {
        'before': (0, 0, 2, 3),
        'instruction': (3, 0, 0, 2),
        'after': (0, 0, 0, 3)
    },
    {
        'before': (2, 1, 0, 2),
        'instruction': (2, 0, 3, 2),
        'after': (2, 1, 3, 2)
    },
    {
        'before': (1, 2, 1, 3),
        'instruction': (1, 3, 0, 2),
        'after': (1, 2, 3, 3)
    },
    {
        'before': (1, 0, 0, 3),
        'instruction': (15, 2, 3, 1),
        'after': (1, 3, 0, 3)
    },
    {
        'before': (3, 1, 0, 3),
        'instruction': (9, 1, 3, 2),
        'after': (3, 1, 3, 3)
    },
    {
        'before': (0, 0, 0, 0),
        'instruction': (7, 0, 1, 2),
        'after': (0, 0, 0, 0)
    },
    {
        'before': (0, 2, 3, 0),
        'instruction': (14, 2, 1, 1),
        'after': (0, 2, 3, 0)
    },
    {
        'before': (2, 0, 2, 1),
        'instruction': (6, 3, 2, 2),
        'after': (2, 0, 3, 1)
    },
    {
        'before': (2, 1, 1, 1),
        'instruction': (8, 2, 3, 0),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (1, 0, 3, 3),
        'instruction': (12, 2, 2, 1),
        'after': (1, 2, 3, 3)
    },
    {
        'before': (0, 0, 3, 1),
        'instruction': (3, 0, 0, 1),
        'after': (0, 0, 3, 1)
    },
    {
        'before': (1, 1, 3, 1),
        'instruction': (4, 1, 0, 0),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (1, 3, 2, 1),
        'instruction': (14, 1, 2, 3),
        'after': (1, 3, 2, 2)
    },
    {
        'before': (2, 1, 2, 3),
        'instruction': (9, 1, 3, 1),
        'after': (2, 3, 2, 3)
    },
    {
        'before': (2, 1, 0, 0),
        'instruction': (0, 2, 1, 0),
        'after': (1, 1, 0, 0)
    },
    {
        'before': (3, 1, 0, 1),
        'instruction': (5, 1, 3, 2),
        'after': (3, 1, 1, 1)
    },
    {
        'before': (1, 2, 3, 3),
        'instruction': (12, 2, 2, 0),
        'after': (2, 2, 3, 3)
    },
    {
        'before': (1, 3, 2, 1),
        'instruction': (1, 2, 2, 3),
        'after': (1, 3, 2, 2)
    },
    {
        'before': (0, 2, 2, 3),
        'instruction': (1, 3, 0, 2),
        'after': (0, 2, 3, 3)
    },
    {
        'before': (2, 0, 3, 1),
        'instruction': (8, 3, 3, 3),
        'after': (2, 0, 3, 1)
    },
    {
        'before': (1, 3, 1, 2),
        'instruction': (10, 2, 3, 2),
        'after': (1, 3, 3, 2)
    },
    {
        'before': (1, 1, 2, 1),
        'instruction': (5, 1, 3, 1),
        'after': (1, 1, 2, 1)
    },
    {
        'before': (2, 0, 1, 3),
        'instruction': (9, 2, 3, 0),
        'after': (3, 0, 1, 3)
    },
    {
        'before': (0, 3, 1, 0),
        'instruction': (13, 2, 3, 3),
        'after': (0, 3, 1, 3)
    },
    {
        'before': (1, 2, 0, 1),
        'instruction': (8, 3, 3, 1),
        'after': (1, 1, 0, 1)
    },
    {
        'before': (2, 1, 2, 3),
        'instruction': (15, 0, 2, 1),
        'after': (2, 4, 2, 3)
    },
    {
        'before': (3, 3, 2, 3),
        'instruction': (11, 0, 2, 2),
        'after': (3, 3, 6, 3)
    },
    {
        'before': (0, 0, 0, 2),
        'instruction': (7, 0, 1, 0),
        'after': (0, 0, 0, 2)
    },
    {
        'before': (0, 1, 3, 1),
        'instruction': (12, 2, 2, 2),
        'after': (0, 1, 2, 1)
    },
    {
        'before': (3, 2, 2, 3),
        'instruction': (11, 3, 3, 1),
        'after': (3, 9, 2, 3)
    },
    {
        'before': (2, 3, 1, 0),
        'instruction': (2, 0, 3, 3),
        'after': (2, 3, 1, 3)
    },
    {
        'before': (3, 3, 1, 2),
        'instruction': (10, 2, 3, 0),
        'after': (3, 3, 1, 2)
    },
    {
        'before': (1, 0, 1, 0),
        'instruction': (13, 0, 3, 3),
        'after': (1, 0, 1, 3)
    },
    {
        'before': (1, 1, 3, 3),
        'instruction': (9, 0, 3, 2),
        'after': (1, 1, 3, 3)
    },
    {
        'before': (2, 2, 2, 2),
        'instruction': (2, 0, 3, 1),
        'after': (2, 3, 2, 2)
    },
    {
        'before': (0, 1, 1, 3),
        'instruction': (9, 2, 3, 0),
        'after': (3, 1, 1, 3)
    },
    {
        'before': (0, 1, 3, 1),
        'instruction': (6, 3, 2, 0),
        'after': (3, 1, 3, 1)
    },
    {
        'before': (1, 2, 3, 3),
        'instruction': (11, 1, 3, 1),
        'after': (1, 6, 3, 3)
    },
    {
        'before': (1, 2, 1, 3),
        'instruction': (1, 3, 3, 0),
        'after': (3, 2, 1, 3)
    },
    {
        'before': (0, 3, 2, 0),
        'instruction': (2, 2, 3, 2),
        'after': (0, 3, 3, 0)
    },
    {
        'before': (2, 1, 0, 1),
        'instruction': (5, 1, 3, 1),
        'after': (2, 1, 0, 1)
    },
    {
        'before': (2, 0, 3, 0),
        'instruction': (14, 2, 0, 3),
        'after': (2, 0, 3, 2)
    },
    {
        'before': (1, 1, 1, 3),
        'instruction': (9, 0, 3, 2),
        'after': (1, 1, 3, 3)
    },
    {
        'before': (2, 1, 2, 1),
        'instruction': (15, 1, 2, 0),
        'after': (3, 1, 2, 1)
    },
    {
        'before': (2, 1, 3, 1),
        'instruction': (6, 3, 2, 0),
        'after': (3, 1, 3, 1)
    },
    {
        'before': (1, 1, 3, 2),
        'instruction': (4, 1, 0, 2),
        'after': (1, 1, 1, 2)
    },
    {
        'before': (1, 1, 1, 0),
        'instruction': (13, 2, 3, 0),
        'after': (3, 1, 1, 0)
    },
    {
        'before': (0, 2, 3, 0),
        'instruction': (2, 1, 3, 3),
        'after': (0, 2, 3, 3)
    },
    {
        'before': (2, 1, 0, 3),
        'instruction': (15, 0, 1, 1),
        'after': (2, 3, 0, 3)
    },
    {
        'before': (1, 1, 2, 0),
        'instruction': (13, 0, 3, 2),
        'after': (1, 1, 3, 0)
    },
    {
        'before': (2, 2, 2, 2),
        'instruction': (2, 2, 3, 0),
        'after': (3, 2, 2, 2)
    },
    {
        'before': (0, 0, 1, 0),
        'instruction': (7, 0, 2, 1),
        'after': (0, 0, 1, 0)
    },
    {
        'before': (0, 0, 2, 3),
        'instruction': (3, 0, 0, 3),
        'after': (0, 0, 2, 0)
    },
    {
        'before': (3, 1, 1, 3),
        'instruction': (9, 1, 3, 3),
        'after': (3, 1, 1, 3)
    },
    {
        'before': (2, 1, 0, 3),
        'instruction': (0, 2, 1, 1),
        'after': (2, 1, 0, 3)
    },
    {
        'before': (2, 0, 2, 2),
        'instruction': (2, 2, 3, 0),
        'after': (3, 0, 2, 2)
    },
    {
        'before': (1, 2, 2, 3),
        'instruction': (14, 3, 2, 3),
        'after': (1, 2, 2, 2)
    },
    {
        'before': (0, 0, 2, 3),
        'instruction': (3, 0, 0, 0),
        'after': (0, 0, 2, 3)
    },
    {
        'before': (1, 0, 1, 0),
        'instruction': (13, 2, 3, 2),
        'after': (1, 0, 3, 0)
    },
    {
        'before': (3, 3, 1, 1),
        'instruction': (13, 2, 3, 0),
        'after': (3, 3, 1, 1)
    },
    {
        'before': (1, 1, 1, 3),
        'instruction': (11, 3, 3, 3),
        'after': (1, 1, 1, 9)
    },
    {
        'before': (0, 3, 3, 3),
        'instruction': (12, 2, 2, 3),
        'after': (0, 3, 3, 2)
    },
    {
        'before': (0, 2, 1, 3),
        'instruction': (3, 0, 0, 1),
        'after': (0, 0, 1, 3)
    },
    {
        'before': (1, 0, 2, 3),
        'instruction': (9, 0, 3, 1),
        'after': (1, 3, 2, 3)
    },
    {
        'before': (2, 3, 2, 1),
        'instruction': (6, 3, 2, 0),
        'after': (3, 3, 2, 1)
    },
    {
        'before': (1, 3, 1, 3),
        'instruction': (9, 2, 3, 0),
        'after': (3, 3, 1, 3)
    },
    {
        'before': (0, 1, 0, 0),
        'instruction': (3, 0, 0, 1),
        'after': (0, 0, 0, 0)
    },
    {
        'before': (1, 0, 0, 0),
        'instruction': (13, 0, 3, 3),
        'after': (1, 0, 0, 3)
    },
    {
        'before': (1, 3, 3, 2),
        'instruction': (10, 0, 3, 3),
        'after': (1, 3, 3, 3)
    },
    {
        'before': (2, 0, 1, 2),
        'instruction': (10, 2, 3, 0),
        'after': (3, 0, 1, 2)
    },
    {
        'before': (1, 1, 0, 1),
        'instruction': (5, 1, 3, 1),
        'after': (1, 1, 0, 1)
    },
    {
        'before': (2, 2, 0, 0),
        'instruction': (2, 1, 3, 3),
        'after': (2, 2, 0, 3)
    },
    {
        'before': (2, 2, 3, 2),
        'instruction': (14, 2, 3, 3),
        'after': (2, 2, 3, 2)
    },
    {
        'before': (3, 3, 2, 3),
        'instruction': (14, 3, 2, 3),
        'after': (3, 3, 2, 2)
    },
    {
        'before': (0, 1, 2, 2),
        'instruction': (10, 1, 3, 3),
        'after': (0, 1, 2, 3)
    },
    {
        'before': (1, 0, 3, 2),
        'instruction': (12, 2, 2, 2),
        'after': (1, 0, 2, 2)
    },
    {
        'before': (0, 2, 0, 2),
        'instruction': (7, 0, 2, 2),
        'after': (0, 2, 0, 2)
    },
    {
        'before': (0, 0, 2, 0),
        'instruction': (7, 0, 3, 2),
        'after': (0, 0, 0, 0)
    },
    {
        'before': (1, 1, 0, 0),
        'instruction': (0, 2, 1, 1),
        'after': (1, 1, 0, 0)
    },
    {
        'before': (3, 1, 0, 1),
        'instruction': (0, 2, 1, 0),
        'after': (1, 1, 0, 1)
    },
    {
        'before': (1, 1, 3, 1),
        'instruction': (5, 1, 3, 3),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (1, 1, 3, 3),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 3, 3)
    },
    {
        'before': (1, 1, 3, 0),
        'instruction': (0, 3, 1, 0),
        'after': (1, 1, 3, 0)
    },
    {
        'before': (2, 1, 0, 3),
        'instruction': (15, 2, 3, 2),
        'after': (2, 1, 3, 3)
    },
    {
        'before': (1, 0, 2, 2),
        'instruction': (15, 1, 2, 0),
        'after': (2, 0, 2, 2)
    },
    {
        'before': (0, 3, 0, 1),
        'instruction': (8, 3, 3, 2),
        'after': (0, 3, 1, 1)
    },
    {
        'before': (3, 1, 0, 1),
        'instruction': (5, 1, 3, 1),
        'after': (3, 1, 0, 1)
    },
    {
        'before': (0, 2, 3, 2),
        'instruction': (12, 2, 2, 2),
        'after': (0, 2, 2, 2)
    },
    {
        'before': (2, 1, 0, 3),
        'instruction': (11, 0, 3, 1),
        'after': (2, 6, 0, 3)
    },
    {
        'before': (3, 1, 2, 0),
        'instruction': (2, 2, 3, 1),
        'after': (3, 3, 2, 0)
    },
    {
        'before': (1, 2, 2, 1),
        'instruction': (13, 0, 3, 0),
        'after': (3, 2, 2, 1)
    },
    {
        'before': (2, 3, 3, 2),
        'instruction': (14, 2, 0, 0),
        'after': (2, 3, 3, 2)
    },
    {
        'before': (2, 1, 0, 0),
        'instruction': (0, 2, 1, 2),
        'after': (2, 1, 1, 0)
    },
    {
        'before': (0, 0, 0, 1),
        'instruction': (3, 0, 0, 1),
        'after': (0, 0, 0, 1)
    },
    {
        'before': (2, 2, 2, 3),
        'instruction': (11, 0, 3, 1),
        'after': (2, 6, 2, 3)
    },
    {
        'before': (2, 2, 3, 0),
        'instruction': (12, 2, 2, 3),
        'after': (2, 2, 3, 2)
    },
    {
        'before': (2, 3, 3, 1),
        'instruction': (8, 3, 3, 0),
        'after': (1, 3, 3, 1)
    },
    {
        'before': (2, 1, 2, 2),
        'instruction': (2, 2, 3, 3),
        'after': (2, 1, 2, 3)
    },
    {
        'before': (0, 0, 1, 1),
        'instruction': (8, 3, 3, 1),
        'after': (0, 1, 1, 1)
    },
    {
        'before': (1, 1, 3, 1),
        'instruction': (6, 3, 2, 3),
        'after': (1, 1, 3, 3)
    },
    {
        'before': (1, 1, 2, 2),
        'instruction': (6, 3, 1, 1),
        'after': (1, 3, 2, 2)
    },
    {
        'before': (0, 0, 3, 2),
        'instruction': (14, 2, 3, 3),
        'after': (0, 0, 3, 2)
    },
    {
        'before': (3, 1, 2, 2),
        'instruction': (6, 3, 1, 0),
        'after': (3, 1, 2, 2)
    },
    {
        'before': (1, 0, 1, 2),
        'instruction': (10, 0, 3, 0),
        'after': (3, 0, 1, 2)
    },
    {
        'before': (0, 2, 2, 0),
        'instruction': (3, 0, 0, 3),
        'after': (0, 2, 2, 0)
    },
    {
        'before': (2, 1, 0, 0),
        'instruction': (0, 3, 1, 2),
        'after': (2, 1, 1, 0)
    },
    {
        'before': (2, 1, 3, 2),
        'instruction': (12, 2, 2, 1),
        'after': (2, 2, 3, 2)
    },
    {
        'before': (1, 1, 0, 2),
        'instruction': (4, 1, 0, 3),
        'after': (1, 1, 0, 1)
    },
    {
        'before': (3, 1, 1, 1),
        'instruction': (5, 1, 3, 2),
        'after': (3, 1, 1, 1)
    },
    {
        'before': (3, 0, 2, 0),
        'instruction': (15, 2, 2, 1),
        'after': (3, 4, 2, 0)
    },
    {
        'before': (0, 2, 3, 1),
        'instruction': (14, 2, 1, 2),
        'after': (0, 2, 2, 1)
    },
    {
        'before': (3, 2, 2, 3),
        'instruction': (14, 0, 2, 2),
        'after': (3, 2, 2, 3)
    },
    {
        'before': (1, 1, 2, 1),
        'instruction': (4, 1, 0, 2),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (1, 3, 3, 1),
        'instruction': (6, 3, 2, 1),
        'after': (1, 3, 3, 1)
    },
    {
        'before': (0, 0, 0, 0),
        'instruction': (7, 0, 1, 3),
        'after': (0, 0, 0, 0)
    },
    {
        'before': (0, 3, 1, 3),
        'instruction': (3, 0, 0, 1),
        'after': (0, 0, 1, 3)
    },
    {
        'before': (0, 1, 0, 0),
        'instruction': (0, 3, 1, 0),
        'after': (1, 1, 0, 0)
    },
    {
        'before': (0, 0, 3, 1),
        'instruction': (12, 2, 2, 1),
        'after': (0, 2, 3, 1)
    },
    {
        'before': (0, 0, 1, 1),
        'instruction': (8, 3, 3, 3),
        'after': (0, 0, 1, 1)
    },
    {
        'before': (1, 3, 3, 1),
        'instruction': (6, 3, 2, 3),
        'after': (1, 3, 3, 3)
    },
    {
        'before': (1, 1, 1, 3),
        'instruction': (4, 1, 0, 2),
        'after': (1, 1, 1, 3)
    },
    {
        'before': (0, 3, 0, 2),
        'instruction': (3, 0, 0, 1),
        'after': (0, 0, 0, 2)
    },
    {
        'before': (0, 1, 3, 1),
        'instruction': (12, 2, 2, 0),
        'after': (2, 1, 3, 1)
    },
    {
        'before': (2, 1, 2, 1),
        'instruction': (5, 1, 3, 1),
        'after': (2, 1, 2, 1)
    },
    {
        'before': (3, 0, 1, 2),
        'instruction': (10, 2, 3, 1),
        'after': (3, 3, 1, 2)
    },
    {
        'before': (0, 3, 2, 3),
        'instruction': (15, 0, 3, 3),
        'after': (0, 3, 2, 3)
    },
    {
        'before': (1, 1, 2, 2),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 2, 2)
    },
    {
        'before': (2, 1, 0, 2),
        'instruction': (10, 1, 3, 1),
        'after': (2, 3, 0, 2)
    },
    {
        'before': (1, 1, 2, 2),
        'instruction': (4, 1, 0, 2),
        'after': (1, 1, 1, 2)
    },
    {
        'before': (3, 0, 1, 3),
        'instruction': (15, 1, 3, 1),
        'after': (3, 3, 1, 3)
    },
    {
        'before': (1, 3, 0, 1),
        'instruction': (8, 3, 3, 0),
        'after': (1, 3, 0, 1)
    },
    {
        'before': (2, 2, 3, 2),
        'instruction': (14, 2, 0, 2),
        'after': (2, 2, 2, 2)
    },
    {
        'before': (0, 3, 2, 1),
        'instruction': (11, 3, 2, 3),
        'after': (0, 3, 2, 2)
    },
    {
        'before': (3, 2, 3, 2),
        'instruction': (2, 1, 3, 3),
        'after': (3, 2, 3, 3)
    },
    {
        'before': (1, 1, 2, 3),
        'instruction': (1, 2, 2, 0),
        'after': (2, 1, 2, 3)
    },
    {
        'before': (3, 1, 1, 0),
        'instruction': (13, 2, 3, 3),
        'after': (3, 1, 1, 3)
    },
    {
        'before': (0, 3, 0, 2),
        'instruction': (3, 0, 0, 2),
        'after': (0, 3, 0, 2)
    },
    {
        'before': (3, 2, 2, 3),
        'instruction': (11, 0, 3, 0),
        'after': (9, 2, 2, 3)
    },
    {
        'before': (0, 1, 0, 3),
        'instruction': (7, 0, 1, 3),
        'after': (0, 1, 0, 0)
    },
    {
        'before': (0, 1, 0, 2),
        'instruction': (3, 0, 0, 3),
        'after': (0, 1, 0, 0)
    },
    {
        'before': (3, 1, 0, 3),
        'instruction': (1, 3, 1, 3),
        'after': (3, 1, 0, 3)
    },
    {
        'before': (2, 1, 0, 0),
        'instruction': (15, 0, 1, 0),
        'after': (3, 1, 0, 0)
    },
    {
        'before': (2, 1, 3, 0),
        'instruction': (0, 3, 1, 0),
        'after': (1, 1, 3, 0)
    },
    {
        'before': (1, 2, 3, 1),
        'instruction': (13, 0, 3, 0),
        'after': (3, 2, 3, 1)
    },
    {
        'before': (1, 0, 3, 1),
        'instruction': (8, 3, 3, 0),
        'after': (1, 0, 3, 1)
    },
    {
        'before': (1, 0, 3, 1),
        'instruction': (8, 3, 3, 1),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (1, 2, 3, 1),
        'instruction': (12, 2, 2, 2),
        'after': (1, 2, 2, 1)
    },
    {
        'before': (3, 0, 1, 1),
        'instruction': (8, 2, 3, 0),
        'after': (1, 0, 1, 1)
    },
    {
        'before': (0, 1, 2, 2),
        'instruction': (3, 0, 0, 3),
        'after': (0, 1, 2, 0)
    },
    {
        'before': (0, 1, 1, 3),
        'instruction': (3, 0, 0, 2),
        'after': (0, 1, 0, 3)
    },
    {
        'before': (2, 1, 2, 1),
        'instruction': (5, 1, 3, 2),
        'after': (2, 1, 1, 1)
    },
    {
        'before': (1, 0, 3, 3),
        'instruction': (9, 0, 3, 3),
        'after': (1, 0, 3, 3)
    },
    {
        'before': (1, 0, 2, 3),
        'instruction': (15, 2, 2, 3),
        'after': (1, 0, 2, 4)
    },
    {
        'before': (1, 2, 3, 2),
        'instruction': (15, 0, 2, 2),
        'after': (1, 2, 3, 2)
    },
    {
        'before': (3, 1, 2, 3),
        'instruction': (15, 2, 2, 0),
        'after': (4, 1, 2, 3)
    },
    {
        'before': (1, 0, 3, 2),
        'instruction': (10, 0, 3, 1),
        'after': (1, 3, 3, 2)
    },
    {
        'before': (3, 1, 2, 3),
        'instruction': (14, 0, 2, 2),
        'after': (3, 1, 2, 3)
    },
    {
        'before': (3, 0, 2, 2),
        'instruction': (15, 1, 2, 0),
        'after': (2, 0, 2, 2)
    },
    {
        'before': (2, 3, 2, 3),
        'instruction': (11, 2, 3, 2),
        'after': (2, 3, 6, 3)
    },
    {
        'before': (2, 1, 1, 0),
        'instruction': (13, 2, 3, 1),
        'after': (2, 3, 1, 0)
    },
    {
        'before': (2, 0, 1, 2),
        'instruction': (10, 2, 3, 2),
        'after': (2, 0, 3, 2)
    },
    {
        'before': (1, 2, 2, 1),
        'instruction': (8, 3, 3, 2),
        'after': (1, 2, 1, 1)
    },
    {
        'before': (3, 2, 2, 1),
        'instruction': (14, 0, 2, 3),
        'after': (3, 2, 2, 2)
    },
    {
        'before': (3, 1, 2, 2),
        'instruction': (11, 1, 2, 0),
        'after': (2, 1, 2, 2)
    },
    {
        'before': (0, 3, 0, 3),
        'instruction': (7, 0, 1, 1),
        'after': (0, 0, 0, 3)
    },
    {
        'before': (2, 1, 2, 0),
        'instruction': (2, 0, 3, 0),
        'after': (3, 1, 2, 0)
    },
    {
        'before': (1, 1, 1, 2),
        'instruction': (10, 1, 3, 0),
        'after': (3, 1, 1, 2)
    },
    {
        'before': (2, 1, 3, 3),
        'instruction': (9, 1, 3, 2),
        'after': (2, 1, 3, 3)
    },
    {
        'before': (3, 0, 1, 3),
        'instruction': (11, 0, 3, 2),
        'after': (3, 0, 9, 3)
    },
    {
        'before': (0, 1, 0, 1),
        'instruction': (5, 1, 3, 0),
        'after': (1, 1, 0, 1)
    },
    {
        'before': (1, 1, 3, 1),
        'instruction': (5, 1, 3, 1),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (1, 1, 3, 1),
        'instruction': (8, 3, 3, 1),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (1, 1, 1, 2),
        'instruction': (10, 0, 3, 1),
        'after': (1, 3, 1, 2)
    },
    {
        'before': (3, 2, 3, 1),
        'instruction': (14, 2, 1, 1),
        'after': (3, 2, 3, 1)
    },
    {
        'before': (1, 2, 1, 1),
        'instruction': (8, 2, 3, 3),
        'after': (1, 2, 1, 1)
    },
    {
        'before': (3, 3, 2, 1),
        'instruction': (8, 3, 3, 2),
        'after': (3, 3, 1, 1)
    },
    {
        'before': (1, 1, 1, 2),
        'instruction': (4, 1, 0, 2),
        'after': (1, 1, 1, 2)
    },
    {
        'before': (2, 3, 3, 1),
        'instruction': (14, 2, 0, 0),
        'after': (2, 3, 3, 1)
    },
    {
        'before': (2, 0, 1, 3),
        'instruction': (9, 2, 3, 1),
        'after': (2, 3, 1, 3)
    },
    {
        'before': (1, 1, 0, 1),
        'instruction': (5, 1, 3, 2),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (0, 1, 0, 2),
        'instruction': (10, 1, 3, 3),
        'after': (0, 1, 0, 3)
    },
    {
        'before': (3, 1, 0, 1),
        'instruction': (8, 3, 3, 1),
        'after': (3, 1, 0, 1)
    },
    {
        'before': (1, 1, 3, 2),
        'instruction': (4, 1, 0, 0),
        'after': (1, 1, 3, 2)
    },
    {
        'before': (0, 3, 1, 0),
        'instruction': (3, 0, 0, 2),
        'after': (0, 3, 0, 0)
    },
    {
        'before': (3, 1, 1, 0),
        'instruction': (0, 3, 1, 3),
        'after': (3, 1, 1, 1)
    },
    {
        'before': (1, 0, 2, 2),
        'instruction': (10, 0, 3, 0),
        'after': (3, 0, 2, 2)
    },
    {
        'before': (0, 1, 3, 1),
        'instruction': (3, 0, 0, 3),
        'after': (0, 1, 3, 0)
    },
    {
        'before': (2, 3, 2, 0),
        'instruction': (1, 2, 0, 1),
        'after': (2, 2, 2, 0)
    },
    {
        'before': (1, 1, 3, 0),
        'instruction': (0, 3, 1, 1),
        'after': (1, 1, 3, 0)
    },
    {
        'before': (2, 0, 1, 3),
        'instruction': (15, 1, 3, 0),
        'after': (3, 0, 1, 3)
    },
    {
        'before': (2, 0, 3, 1),
        'instruction': (8, 3, 3, 2),
        'after': (2, 0, 1, 1)
    },
    {
        'before': (0, 2, 3, 2),
        'instruction': (7, 0, 2, 3),
        'after': (0, 2, 3, 0)
    },
    {
        'before': (1, 3, 3, 3),
        'instruction': (9, 0, 3, 1),
        'after': (1, 3, 3, 3)
    },
    {
        'before': (3, 1, 2, 3),
        'instruction': (1, 3, 3, 1),
        'after': (3, 3, 2, 3)
    },
    {
        'before': (0, 0, 3, 0),
        'instruction': (3, 0, 0, 3),
        'after': (0, 0, 3, 0)
    },
    {
        'before': (2, 3, 2, 3),
        'instruction': (11, 1, 2, 3),
        'after': (2, 3, 2, 6)
    },
    {
        'before': (2, 1, 0, 1),
        'instruction': (8, 3, 3, 1),
        'after': (2, 1, 0, 1)
    },
    {
        'before': (2, 1, 1, 0),
        'instruction': (0, 3, 1, 2),
        'after': (2, 1, 1, 0)
    },
    {
        'before': (0, 0, 3, 2),
        'instruction': (12, 2, 2, 2),
        'after': (0, 0, 2, 2)
    },
    {
        'before': (3, 2, 3, 3),
        'instruction': (11, 1, 3, 0),
        'after': (6, 2, 3, 3)
    },
    {
        'before': (3, 1, 0, 0),
        'instruction': (0, 2, 1, 3),
        'after': (3, 1, 0, 1)
    },
    {
        'before': (1, 3, 2, 3),
        'instruction': (9, 0, 3, 0),
        'after': (3, 3, 2, 3)
    },
    {
        'before': (0, 0, 0, 0),
        'instruction': (3, 0, 0, 3),
        'after': (0, 0, 0, 0)
    },
    {
        'before': (0, 1, 1, 2),
        'instruction': (3, 0, 0, 1),
        'after': (0, 0, 1, 2)
    },
    {
        'before': (1, 2, 2, 2),
        'instruction': (10, 0, 3, 0),
        'after': (3, 2, 2, 2)
    },
    {
        'before': (2, 1, 2, 0),
        'instruction': (0, 3, 1, 2),
        'after': (2, 1, 1, 0)
    },
    {
        'before': (2, 3, 0, 3),
        'instruction': (11, 1, 3, 0),
        'after': (9, 3, 0, 3)
    },
    {
        'before': (1, 2, 3, 1),
        'instruction': (13, 0, 3, 1),
        'after': (1, 3, 3, 1)
    },
    {
        'before': (0, 2, 0, 3),
        'instruction': (1, 3, 3, 0),
        'after': (3, 2, 0, 3)
    },
    {
        'before': (1, 1, 0, 3),
        'instruction': (1, 3, 1, 2),
        'after': (1, 1, 3, 3)
    },
    {
        'before': (3, 1, 3, 0),
        'instruction': (13, 1, 3, 3),
        'after': (3, 1, 3, 3)
    },
    {
        'before': (3, 2, 2, 2),
        'instruction': (2, 2, 3, 0),
        'after': (3, 2, 2, 2)
    },
    {
        'before': (0, 0, 3, 1),
        'instruction': (12, 2, 2, 2),
        'after': (0, 0, 2, 1)
    },
    {
        'before': (0, 1, 3, 1),
        'instruction': (5, 1, 3, 2),
        'after': (0, 1, 1, 1)
    },
    {
        'before': (0, 1, 1, 1),
        'instruction': (7, 0, 1, 1),
        'after': (0, 0, 1, 1)
    },
    {
        'before': (3, 1, 3, 0),
        'instruction': (0, 3, 1, 0),
        'after': (1, 1, 3, 0)
    },
    {
        'before': (0, 2, 2, 3),
        'instruction': (11, 1, 3, 0),
        'after': (6, 2, 2, 3)
    },
    {
        'before': (0, 3, 0, 3),
        'instruction': (11, 1, 3, 0),
        'after': (9, 3, 0, 3)
    },
    {
        'before': (0, 1, 3, 1),
        'instruction': (7, 0, 1, 2),
        'after': (0, 1, 0, 1)
    },
    {
        'before': (2, 1, 2, 3),
        'instruction': (15, 2, 2, 1),
        'after': (2, 4, 2, 3)
    },
    {
        'before': (2, 1, 2, 3),
        'instruction': (9, 1, 3, 3),
        'after': (2, 1, 2, 3)
    },
    {
        'before': (0, 0, 3, 0),
        'instruction': (12, 2, 2, 1),
        'after': (0, 2, 3, 0)
    },
    {
        'before': (1, 2, 3, 3),
        'instruction': (14, 2, 1, 3),
        'after': (1, 2, 3, 2)
    },
    {
        'before': (0, 1, 2, 0),
        'instruction': (0, 3, 1, 1),
        'after': (0, 1, 2, 0)
    },
    {
        'before': (2, 3, 1, 2),
        'instruction': (10, 2, 3, 0),
        'after': (3, 3, 1, 2)
    },
    {
        'before': (3, 1, 3, 1),
        'instruction': (5, 1, 3, 3),
        'after': (3, 1, 3, 1)
    },
    {
        'before': (0, 1, 3, 3),
        'instruction': (1, 3, 1, 1),
        'after': (0, 3, 3, 3)
    },
    {
        'before': (0, 2, 1, 3),
        'instruction': (7, 0, 2, 2),
        'after': (0, 2, 0, 3)
    },
    {
        'before': (1, 2, 3, 3),
        'instruction': (11, 1, 3, 0),
        'after': (6, 2, 3, 3)
    },
    {
        'before': (2, 1, 1, 0),
        'instruction': (0, 3, 1, 1),
        'after': (2, 1, 1, 0)
    },
    {
        'before': (2, 1, 2, 2),
        'instruction': (2, 2, 3, 0),
        'after': (3, 1, 2, 2)
    },
    {
        'before': (1, 2, 3, 3),
        'instruction': (9, 0, 3, 2),
        'after': (1, 2, 3, 3)
    },
    {
        'before': (1, 2, 2, 0),
        'instruction': (2, 2, 3, 1),
        'after': (1, 3, 2, 0)
    },
    {
        'before': (3, 2, 2, 0),
        'instruction': (15, 2, 2, 3),
        'after': (3, 2, 2, 4)
    },
    {
        'before': (3, 1, 3, 1),
        'instruction': (6, 3, 2, 2),
        'after': (3, 1, 3, 1)
    },
    {
        'before': (0, 3, 2, 2),
        'instruction': (15, 3, 2, 0),
        'after': (4, 3, 2, 2)
    },
    {
        'before': (1, 1, 3, 2),
        'instruction': (12, 2, 2, 0),
        'after': (2, 1, 3, 2)
    },
    {
        'before': (3, 3, 1, 1),
        'instruction': (8, 2, 3, 0),
        'after': (1, 3, 1, 1)
    },
    {
        'before': (0, 3, 0, 2),
        'instruction': (3, 0, 0, 3),
        'after': (0, 3, 0, 0)
    },
    {
        'before': (0, 1, 2, 1),
        'instruction': (15, 1, 2, 1),
        'after': (0, 3, 2, 1)
    },
    {
        'before': (3, 3, 2, 1),
        'instruction': (8, 3, 3, 0),
        'after': (1, 3, 2, 1)
    },
    {
        'before': (0, 0, 2, 1),
        'instruction': (8, 3, 3, 2),
        'after': (0, 0, 1, 1)
    },
    {
        'before': (1, 0, 3, 1),
        'instruction': (13, 0, 3, 2),
        'after': (1, 0, 3, 1)
    },
    {
        'before': (3, 3, 3, 3),
        'instruction': (12, 2, 2, 1),
        'after': (3, 2, 3, 3)
    },
    {
        'before': (0, 1, 1, 0),
        'instruction': (0, 3, 1, 3),
        'after': (0, 1, 1, 1)
    },
    {
        'before': (2, 1, 0, 1),
        'instruction': (5, 1, 3, 2),
        'after': (2, 1, 1, 1)
    },
    {
        'before': (1, 0, 0, 1),
        'instruction': (8, 3, 3, 0),
        'after': (1, 0, 0, 1)
    },
    {
        'before': (0, 3, 0, 2),
        'instruction': (7, 0, 2, 3),
        'after': (0, 3, 0, 0)
    },
    {
        'before': (0, 3, 3, 3),
        'instruction': (3, 0, 0, 0),
        'after': (0, 3, 3, 3)
    },
    {
        'before': (3, 2, 3, 1),
        'instruction': (6, 3, 2, 2),
        'after': (3, 2, 3, 1)
    },
    {
        'before': (1, 1, 2, 0),
        'instruction': (0, 3, 1, 1),
        'after': (1, 1, 2, 0)
    },
    {
        'before': (1, 0, 1, 1),
        'instruction': (8, 3, 3, 1),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (3, 1, 3, 2),
        'instruction': (10, 1, 3, 2),
        'after': (3, 1, 3, 2)
    },
    {
        'before': (2, 1, 0, 0),
        'instruction': (0, 2, 1, 3),
        'after': (2, 1, 0, 1)
    },
    {
        'before': (0, 0, 0, 2),
        'instruction': (7, 0, 3, 1),
        'after': (0, 0, 0, 2)
    },
    {
        'before': (1, 1, 2, 2),
        'instruction': (15, 1, 2, 1),
        'after': (1, 3, 2, 2)
    },
    {
        'before': (1, 0, 2, 3),
        'instruction': (14, 3, 2, 1),
        'after': (1, 2, 2, 3)
    },
    {
        'before': (1, 1, 3, 3),
        'instruction': (4, 1, 0, 2),
        'after': (1, 1, 1, 3)
    },
    {
        'before': (0, 1, 0, 2),
        'instruction': (0, 2, 1, 2),
        'after': (0, 1, 1, 2)
    },
    {
        'before': (1, 3, 3, 1),
        'instruction': (8, 3, 3, 2),
        'after': (1, 3, 1, 1)
    },
    {
        'before': (2, 1, 3, 3),
        'instruction': (9, 1, 3, 1),
        'after': (2, 3, 3, 3)
    },
    {
        'before': (0, 3, 1, 2),
        'instruction': (3, 0, 0, 3),
        'after': (0, 3, 1, 0)
    },
    {
        'before': (0, 1, 3, 3),
        'instruction': (3, 0, 0, 0),
        'after': (0, 1, 3, 3)
    },
    {
        'before': (2, 1, 1, 1),
        'instruction': (5, 1, 3, 0),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (3, 3, 3, 2),
        'instruction': (14, 2, 3, 2),
        'after': (3, 3, 2, 2)
    },
    {
        'before': (3, 3, 3, 3),
        'instruction': (12, 2, 2, 2),
        'after': (3, 3, 2, 3)
    },
    {
        'before': (0, 2, 2, 2),
        'instruction': (1, 2, 2, 2),
        'after': (0, 2, 2, 2)
    },
    {
        'before': (0, 2, 1, 0),
        'instruction': (2, 1, 3, 0),
        'after': (3, 2, 1, 0)
    },
    {
        'before': (0, 0, 3, 1),
        'instruction': (6, 3, 2, 0),
        'after': (3, 0, 3, 1)
    },
    {
        'before': (1, 1, 2, 2),
        'instruction': (1, 2, 2, 3),
        'after': (1, 1, 2, 2)
    },
    {
        'before': (3, 1, 0, 0),
        'instruction': (0, 2, 1, 1),
        'after': (3, 1, 0, 0)
    },
    {
        'before': (1, 1, 0, 3),
        'instruction': (9, 0, 3, 0),
        'after': (3, 1, 0, 3)
    },
    {
        'before': (3, 2, 2, 2),
        'instruction': (2, 1, 3, 3),
        'after': (3, 2, 2, 3)
    },
    {
        'before': (2, 3, 2, 2),
        'instruction': (2, 2, 3, 1),
        'after': (2, 3, 2, 2)
    },
    {
        'before': (1, 1, 1, 1),
        'instruction': (4, 1, 0, 3),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (1, 2, 1, 3),
        'instruction': (9, 0, 3, 3),
        'after': (1, 2, 1, 3)
    },
    {
        'before': (1, 2, 0, 1),
        'instruction': (13, 0, 3, 3),
        'after': (1, 2, 0, 3)
    },
    {
        'before': (0, 2, 2, 3),
        'instruction': (3, 0, 0, 3),
        'after': (0, 2, 2, 0)
    },
    {
        'before': (0, 2, 3, 2),
        'instruction': (14, 2, 1, 2),
        'after': (0, 2, 2, 2)
    },
    {
        'before': (1, 1, 3, 0),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 3, 0)
    },
    {
        'before': (1, 1, 0, 2),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 0, 2)
    },
    {
        'before': (1, 1, 0, 3),
        'instruction': (9, 1, 3, 1),
        'after': (1, 3, 0, 3)
    },
    {
        'before': (0, 3, 0, 3),
        'instruction': (3, 0, 0, 3),
        'after': (0, 3, 0, 0)
    },
    {
        'before': (1, 0, 3, 0),
        'instruction': (13, 0, 3, 1),
        'after': (1, 3, 3, 0)
    },
    {
        'before': (2, 0, 2, 0),
        'instruction': (15, 1, 2, 3),
        'after': (2, 0, 2, 2)
    },
    {
        'before': (1, 1, 3, 2),
        'instruction': (6, 3, 1, 2),
        'after': (1, 1, 3, 2)
    },
    {
        'before': (1, 0, 2, 3),
        'instruction': (9, 0, 3, 2),
        'after': (1, 0, 3, 3)
    },
    {
        'before': (0, 2, 3, 0),
        'instruction': (14, 2, 1, 0),
        'after': (2, 2, 3, 0)
    },
    {
        'before': (0, 1, 2, 3),
        'instruction': (15, 2, 1, 1),
        'after': (0, 3, 2, 3)
    },
    {
        'before': (0, 3, 3, 1),
        'instruction': (12, 2, 2, 3),
        'after': (0, 3, 3, 2)
    },
    {
        'before': (0, 1, 0, 0),
        'instruction': (7, 0, 2, 1),
        'after': (0, 0, 0, 0)
    },
    {
        'before': (0, 2, 1, 1),
        'instruction': (7, 0, 2, 2),
        'after': (0, 2, 0, 1)
    },
    {
        'before': (1, 3, 1, 0),
        'instruction': (13, 0, 3, 1),
        'after': (1, 3, 1, 0)
    },
    {
        'before': (1, 1, 0, 3),
        'instruction': (9, 0, 3, 1),
        'after': (1, 3, 0, 3)
    },
    {
        'before': (2, 1, 1, 3),
        'instruction': (1, 3, 1, 0),
        'after': (3, 1, 1, 3)
    },
    {
        'before': (0, 1, 1, 3),
        'instruction': (7, 0, 1, 1),
        'after': (0, 0, 1, 3)
    },
    {
        'before': (0, 1, 0, 1),
        'instruction': (5, 1, 3, 1),
        'after': (0, 1, 0, 1)
    },
    {
        'before': (0, 3, 2, 0),
        'instruction': (3, 0, 0, 0),
        'after': (0, 3, 2, 0)
    },
    {
        'before': (3, 1, 3, 2),
        'instruction': (10, 1, 3, 0),
        'after': (3, 1, 3, 2)
    },
    {
        'before': (3, 1, 2, 2),
        'instruction': (6, 3, 1, 2),
        'after': (3, 1, 3, 2)
    },
    {
        'before': (1, 1, 2, 1),
        'instruction': (5, 1, 3, 0),
        'after': (1, 1, 2, 1)
    },
    {
        'before': (0, 1, 0, 0),
        'instruction': (3, 0, 0, 0),
        'after': (0, 1, 0, 0)
    },
    {
        'before': (2, 3, 0, 3),
        'instruction': (11, 0, 3, 2),
        'after': (2, 3, 6, 3)
    },
    {
        'before': (0, 1, 2, 0),
        'instruction': (7, 0, 2, 1),
        'after': (0, 0, 2, 0)
    },
    {
        'before': (3, 1, 2, 1),
        'instruction': (5, 1, 3, 3),
        'after': (3, 1, 2, 1)
    },
    {
        'before': (1, 1, 0, 3),
        'instruction': (0, 2, 1, 2),
        'after': (1, 1, 1, 3)
    },
    {
        'before': (3, 1, 1, 1),
        'instruction': (8, 3, 3, 0),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (2, 1, 3, 1),
        'instruction': (8, 3, 3, 1),
        'after': (2, 1, 3, 1)
    },
    {
        'before': (1, 0, 3, 2),
        'instruction': (10, 0, 3, 2),
        'after': (1, 0, 3, 2)
    },
    {
        'before': (1, 1, 1, 2),
        'instruction': (4, 1, 0, 3),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (3, 3, 3, 2),
        'instruction': (12, 2, 2, 3),
        'after': (3, 3, 3, 2)
    },
    {
        'before': (2, 2, 3, 1),
        'instruction': (6, 3, 2, 1),
        'after': (2, 3, 3, 1)
    },
    {
        'before': (2, 3, 2, 1),
        'instruction': (11, 1, 2, 1),
        'after': (2, 6, 2, 1)
    },
    {
        'before': (1, 1, 3, 0),
        'instruction': (0, 3, 1, 3),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (1, 3, 1, 1),
        'instruction': (8, 3, 3, 1),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (2, 3, 1, 3),
        'instruction': (9, 2, 3, 2),
        'after': (2, 3, 3, 3)
    },
    {
        'before': (3, 0, 2, 1),
        'instruction': (6, 3, 2, 0),
        'after': (3, 0, 2, 1)
    },
    {
        'before': (0, 1, 3, 0),
        'instruction': (3, 0, 0, 3),
        'after': (0, 1, 3, 0)
    },
    {
        'before': (1, 0, 2, 1),
        'instruction': (6, 3, 2, 2),
        'after': (1, 0, 3, 1)
    },
    {
        'before': (0, 1, 0, 1),
        'instruction': (7, 0, 2, 2),
        'after': (0, 1, 0, 1)
    },
    {
        'before': (0, 1, 3, 1),
        'instruction': (13, 1, 3, 1),
        'after': (0, 3, 3, 1)
    },
    {
        'before': (0, 1, 0, 1),
        'instruction': (5, 1, 3, 3),
        'after': (0, 1, 0, 1)
    },
    {
        'before': (1, 1, 1, 3),
        'instruction': (9, 1, 3, 2),
        'after': (1, 1, 3, 3)
    },
    {
        'before': (0, 0, 0, 0),
        'instruction': (3, 0, 0, 2),
        'after': (0, 0, 0, 0)
    },
    {
        'before': (0, 2, 0, 1),
        'instruction': (3, 0, 0, 0),
        'after': (0, 2, 0, 1)
    },
    {
        'before': (3, 1, 0, 3),
        'instruction': (0, 2, 1, 0),
        'after': (1, 1, 0, 3)
    },
    {
        'before': (2, 0, 2, 0),
        'instruction': (2, 0, 3, 1),
        'after': (2, 3, 2, 0)
    },
    {
        'before': (2, 1, 1, 3),
        'instruction': (9, 2, 3, 3),
        'after': (2, 1, 1, 3)
    },
    {
        'before': (0, 1, 0, 3),
        'instruction': (15, 0, 3, 3),
        'after': (0, 1, 0, 3)
    },
    {
        'before': (2, 0, 2, 1),
        'instruction': (15, 1, 2, 3),
        'after': (2, 0, 2, 2)
    },
    {
        'before': (2, 1, 1, 3),
        'instruction': (9, 1, 3, 3),
        'after': (2, 1, 1, 3)
    },
    {
        'before': (1, 2, 1, 0),
        'instruction': (13, 2, 3, 3),
        'after': (1, 2, 1, 3)
    },
    {
        'before': (0, 1, 0, 3),
        'instruction': (9, 1, 3, 1),
        'after': (0, 3, 0, 3)
    },
    {
        'before': (0, 3, 2, 1),
        'instruction': (3, 0, 0, 2),
        'after': (0, 3, 0, 1)
    },
    {
        'before': (1, 2, 3, 3),
        'instruction': (11, 1, 3, 3),
        'after': (1, 2, 3, 6)
    },
    {
        'before': (1, 1, 0, 3),
        'instruction': (4, 1, 0, 3),
        'after': (1, 1, 0, 1)
    },
    {
        'before': (1, 0, 0, 3),
        'instruction': (9, 0, 3, 3),
        'after': (1, 0, 0, 3)
    },
    {
        'before': (1, 3, 1, 1),
        'instruction': (13, 0, 3, 2),
        'after': (1, 3, 3, 1)
    },
    {
        'before': (1, 1, 0, 1),
        'instruction': (0, 2, 1, 1),
        'after': (1, 1, 0, 1)
    },
    {
        'before': (1, 1, 0, 2),
        'instruction': (4, 1, 0, 2),
        'after': (1, 1, 1, 2)
    },
    {
        'before': (0, 1, 3, 2),
        'instruction': (15, 1, 2, 1),
        'after': (0, 3, 3, 2)
    },
    {
        'before': (1, 1, 3, 2),
        'instruction': (12, 2, 2, 2),
        'after': (1, 1, 2, 2)
    },
    {
        'before': (3, 1, 3, 2),
        'instruction': (6, 3, 1, 1),
        'after': (3, 3, 3, 2)
    },
    {
        'before': (0, 1, 0, 3),
        'instruction': (9, 1, 3, 3),
        'after': (0, 1, 0, 3)
    },
    {
        'before': (1, 0, 1, 2),
        'instruction': (10, 2, 3, 1),
        'after': (1, 3, 1, 2)
    },
    {
        'before': (2, 1, 2, 2),
        'instruction': (10, 1, 3, 1),
        'after': (2, 3, 2, 2)
    },
    {
        'before': (3, 1, 2, 1),
        'instruction': (5, 1, 3, 2),
        'after': (3, 1, 1, 1)
    },
    {
        'before': (3, 1, 0, 2),
        'instruction': (0, 2, 1, 0),
        'after': (1, 1, 0, 2)
    },
    {
        'before': (2, 1, 3, 1),
        'instruction': (12, 2, 2, 3),
        'after': (2, 1, 3, 2)
    },
    {
        'before': (1, 0, 1, 1),
        'instruction': (13, 2, 3, 2),
        'after': (1, 0, 3, 1)
    },
    {
        'before': (2, 1, 1, 3),
        'instruction': (9, 2, 3, 0),
        'after': (3, 1, 1, 3)
    },
    {
        'before': (1, 1, 2, 0),
        'instruction': (0, 3, 1, 3),
        'after': (1, 1, 2, 1)
    },
    {
        'before': (0, 2, 2, 0),
        'instruction': (2, 2, 3, 3),
        'after': (0, 2, 2, 3)
    },
    {
        'before': (0, 2, 2, 0),
        'instruction': (7, 0, 1, 2),
        'after': (0, 2, 0, 0)
    },
    {
        'before': (1, 2, 3, 3),
        'instruction': (11, 3, 3, 0),
        'after': (9, 2, 3, 3)
    },
    {
        'before': (0, 2, 3, 1),
        'instruction': (8, 3, 3, 0),
        'after': (1, 2, 3, 1)
    },
    {
        'before': (3, 2, 2, 0),
        'instruction': (2, 1, 3, 2),
        'after': (3, 2, 3, 0)
    },
    {
        'before': (3, 1, 3, 1),
        'instruction': (13, 1, 3, 0),
        'after': (3, 1, 3, 1)
    },
    {
        'before': (1, 2, 1, 1),
        'instruction': (13, 2, 3, 2),
        'after': (1, 2, 3, 1)
    },
    {
        'before': (3, 1, 0, 1),
        'instruction': (5, 1, 3, 0),
        'after': (1, 1, 0, 1)
    },
    {
        'before': (1, 0, 1, 3),
        'instruction': (9, 2, 3, 2),
        'after': (1, 0, 3, 3)
    },
    {
        'before': (3, 1, 1, 2),
        'instruction': (10, 2, 3, 1),
        'after': (3, 3, 1, 2)
    },
    {
        'before': (3, 1, 3, 1),
        'instruction': (5, 1, 3, 1),
        'after': (3, 1, 3, 1)
    },
    {
        'before': (2, 1, 1, 0),
        'instruction': (13, 1, 3, 3),
        'after': (2, 1, 1, 3)
    },
    {
        'before': (1, 1, 0, 2),
        'instruction': (0, 2, 1, 1),
        'after': (1, 1, 0, 2)
    },
    {
        'before': (1, 2, 3, 2),
        'instruction': (10, 0, 3, 1),
        'after': (1, 3, 3, 2)
    },
    {
        'before': (1, 0, 1, 3),
        'instruction': (1, 3, 0, 0),
        'after': (3, 0, 1, 3)
    },
    {
        'before': (0, 2, 0, 3),
        'instruction': (3, 0, 0, 0),
        'after': (0, 2, 0, 3)
    },
    {
        'before': (2, 1, 3, 2),
        'instruction': (10, 1, 3, 0),
        'after': (3, 1, 3, 2)
    },
    {
        'before': (1, 1, 2, 3),
        'instruction': (1, 3, 0, 0),
        'after': (3, 1, 2, 3)
    },
    {
        'before': (0, 0, 1, 1),
        'instruction': (13, 2, 3, 0),
        'after': (3, 0, 1, 1)
    },
    {
        'before': (2, 2, 1, 2),
        'instruction': (2, 1, 3, 1),
        'after': (2, 3, 1, 2)
    },
    {
        'before': (0, 3, 3, 2),
        'instruction': (12, 2, 2, 3),
        'after': (0, 3, 3, 2)
    },
    {
        'before': (0, 0, 2, 3),
        'instruction': (14, 3, 2, 2),
        'after': (0, 0, 2, 3)
    },
    {
        'before': (2, 0, 1, 0),
        'instruction': (2, 0, 3, 0),
        'after': (3, 0, 1, 0)
    },
    {
        'before': (1, 1, 1, 2),
        'instruction': (10, 0, 3, 3),
        'after': (1, 1, 1, 3)
    },
    {
        'before': (2, 3, 2, 1),
        'instruction': (1, 2, 2, 1),
        'after': (2, 2, 2, 1)
    },
    {
        'before': (0, 3, 0, 3),
        'instruction': (1, 3, 1, 3),
        'after': (0, 3, 0, 3)
    },
    {
        'before': (1, 2, 3, 3),
        'instruction': (14, 2, 1, 0),
        'after': (2, 2, 3, 3)
    },
    {
        'before': (3, 1, 0, 1),
        'instruction': (0, 2, 1, 3),
        'after': (3, 1, 0, 1)
    },
    {
        'before': (1, 0, 1, 2),
        'instruction': (10, 0, 3, 1),
        'after': (1, 3, 1, 2)
    },
    {
        'before': (3, 3, 2, 3),
        'instruction': (1, 3, 0, 2),
        'after': (3, 3, 3, 3)
    },
    {
        'before': (3, 0, 3, 3),
        'instruction': (11, 3, 3, 3),
        'after': (3, 0, 3, 9)
    },
    {
        'before': (2, 0, 2, 3),
        'instruction': (14, 3, 2, 0),
        'after': (2, 0, 2, 3)
    },
    {
        'before': (3, 3, 2, 3),
        'instruction': (11, 3, 3, 2),
        'after': (3, 3, 9, 3)
    },
    {
        'before': (2, 0, 3, 2),
        'instruction': (12, 2, 2, 2),
        'after': (2, 0, 2, 2)
    },
    {
        'before': (0, 1, 1, 3),
        'instruction': (9, 2, 3, 2),
        'after': (0, 1, 3, 3)
    },
    {
        'before': (1, 2, 1, 1),
        'instruction': (8, 2, 3, 2),
        'after': (1, 2, 1, 1)
    },
    {
        'before': (1, 3, 3, 0),
        'instruction': (12, 2, 2, 0),
        'after': (2, 3, 3, 0)
    },
    {
        'before': (2, 2, 3, 1),
        'instruction': (14, 2, 1, 0),
        'after': (2, 2, 3, 1)
    },
    {
        'before': (1, 3, 2, 0),
        'instruction': (2, 2, 3, 3),
        'after': (1, 3, 2, 3)
    },
    {
        'before': (1, 2, 0, 1),
        'instruction': (13, 0, 3, 1),
        'after': (1, 3, 0, 1)
    },
    {
        'before': (1, 1, 3, 3),
        'instruction': (4, 1, 0, 0),
        'after': (1, 1, 3, 3)
    },
    {
        'before': (1, 1, 3, 2),
        'instruction': (15, 0, 2, 2),
        'after': (1, 1, 3, 2)
    },
    {
        'before': (2, 1, 2, 1),
        'instruction': (5, 1, 3, 3),
        'after': (2, 1, 2, 1)
    },
    {
        'before': (3, 0, 3, 3),
        'instruction': (15, 1, 3, 1),
        'after': (3, 3, 3, 3)
    },
    {
        'before': (3, 0, 3, 3),
        'instruction': (11, 0, 3, 1),
        'after': (3, 9, 3, 3)
    },
    {
        'before': (3, 3, 2, 3),
        'instruction': (14, 0, 2, 0),
        'after': (2, 3, 2, 3)
    },
    {
        'before': (1, 1, 3, 1),
        'instruction': (6, 3, 2, 0),
        'after': (3, 1, 3, 1)
    },
    {
        'before': (2, 0, 2, 2),
        'instruction': (2, 2, 3, 3),
        'after': (2, 0, 2, 3)
    },
    {
        'before': (0, 2, 0, 3),
        'instruction': (15, 2, 3, 3),
        'after': (0, 2, 0, 3)
    },
    {
        'before': (1, 3, 2, 0),
        'instruction': (11, 1, 2, 3),
        'after': (1, 3, 2, 6)
    },
    {
        'before': (1, 1, 0, 0),
        'instruction': (0, 2, 1, 2),
        'after': (1, 1, 1, 0)
    },
    {
        'before': (1, 2, 0, 1),
        'instruction': (8, 3, 3, 2),
        'after': (1, 2, 1, 1)
    },
    {
        'before': (0, 3, 2, 1),
        'instruction': (1, 2, 2, 1),
        'after': (0, 2, 2, 1)
    },
    {
        'before': (2, 0, 0, 3),
        'instruction': (1, 3, 3, 0),
        'after': (3, 0, 0, 3)
    },
    {
        'before': (3, 2, 3, 1),
        'instruction': (12, 2, 2, 0),
        'after': (2, 2, 3, 1)
    },
    {
        'before': (0, 1, 0, 2),
        'instruction': (6, 3, 1, 3),
        'after': (0, 1, 0, 3)
    },
    {
        'before': (3, 2, 2, 0),
        'instruction': (14, 0, 2, 3),
        'after': (3, 2, 2, 2)
    },
    {
        'before': (2, 1, 3, 3),
        'instruction': (11, 2, 3, 3),
        'after': (2, 1, 3, 9)
    },
    {
        'before': (2, 2, 1, 3),
        'instruction': (9, 2, 3, 2),
        'after': (2, 2, 3, 3)
    },
    {
        'before': (3, 0, 0, 1),
        'instruction': (8, 3, 3, 2),
        'after': (3, 0, 1, 1)
    },
    {
        'before': (1, 2, 1, 0),
        'instruction': (2, 1, 3, 3),
        'after': (1, 2, 1, 3)
    },
    {
        'before': (1, 3, 3, 3),
        'instruction': (12, 2, 2, 3),
        'after': (1, 3, 3, 2)
    },
    {
        'before': (0, 1, 1, 1),
        'instruction': (5, 1, 3, 2),
        'after': (0, 1, 1, 1)
    },
    {
        'before': (1, 0, 0, 1),
        'instruction': (8, 3, 3, 3),
        'after': (1, 0, 0, 1)
    },
    {
        'before': (1, 1, 2, 1),
        'instruction': (5, 1, 3, 2),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (2, 2, 2, 3),
        'instruction': (15, 2, 2, 0),
        'after': (4, 2, 2, 3)
    },
    {
        'before': (2, 2, 2, 1),
        'instruction': (8, 3, 3, 2),
        'after': (2, 2, 1, 1)
    },
    {
        'before': (3, 0, 2, 3),
        'instruction': (11, 0, 3, 0),
        'after': (9, 0, 2, 3)
    },
    {
        'before': (3, 0, 3, 1),
        'instruction': (6, 3, 2, 1),
        'after': (3, 3, 3, 1)
    },
    {
        'before': (3, 0, 3, 3),
        'instruction': (1, 3, 1, 1),
        'after': (3, 3, 3, 3)
    },
    {
        'before': (0, 1, 0, 1),
        'instruction': (0, 2, 1, 1),
        'after': (0, 1, 0, 1)
    },
    {
        'before': (2, 1, 0, 1),
        'instruction': (5, 1, 3, 3),
        'after': (2, 1, 0, 1)
    },
    {
        'before': (1, 0, 1, 3),
        'instruction': (1, 3, 0, 2),
        'after': (1, 0, 3, 3)
    },
    {
        'before': (2, 0, 2, 1),
        'instruction': (15, 1, 2, 2),
        'after': (2, 0, 2, 1)
    },
    {
        'before': (0, 0, 2, 2),
        'instruction': (7, 0, 1, 0),
        'after': (0, 0, 2, 2)
    },
    {
        'before': (2, 1, 1, 2),
        'instruction': (10, 1, 3, 2),
        'after': (2, 1, 3, 2)
    },
    {
        'before': (2, 3, 2, 3),
        'instruction': (11, 3, 3, 2),
        'after': (2, 3, 9, 3)
    },
    {
        'before': (0, 3, 3, 2),
        'instruction': (7, 0, 3, 0),
        'after': (0, 3, 3, 2)
    },
    {
        'before': (3, 1, 3, 0),
        'instruction': (0, 3, 1, 2),
        'after': (3, 1, 1, 0)
    },
    {
        'before': (1, 0, 1, 3),
        'instruction': (9, 0, 3, 0),
        'after': (3, 0, 1, 3)
    },
    {
        'before': (2, 1, 2, 2),
        'instruction': (1, 2, 0, 1),
        'after': (2, 2, 2, 2)
    },
    {
        'before': (3, 1, 0, 3),
        'instruction': (0, 2, 1, 1),
        'after': (3, 1, 0, 3)
    },
    {
        'before': (2, 1, 3, 2),
        'instruction': (6, 3, 1, 2),
        'after': (2, 1, 3, 2)
    },
    {
        'before': (0, 0, 1, 3),
        'instruction': (9, 2, 3, 1),
        'after': (0, 3, 1, 3)
    },
    {
        'before': (2, 2, 2, 2),
        'instruction': (2, 1, 3, 0),
        'after': (3, 2, 2, 2)
    },
    {
        'before': (3, 1, 1, 1),
        'instruction': (5, 1, 3, 3),
        'after': (3, 1, 1, 1)
    },
    {
        'before': (1, 1, 2, 1),
        'instruction': (11, 0, 2, 3),
        'after': (1, 1, 2, 2)
    },
    {
        'before': (1, 0, 2, 3),
        'instruction': (15, 0, 2, 2),
        'after': (1, 0, 3, 3)
    },
    {
        'before': (1, 3, 3, 1),
        'instruction': (13, 0, 3, 3),
        'after': (1, 3, 3, 3)
    },
    {
        'before': (2, 1, 3, 2),
        'instruction': (6, 3, 1, 0),
        'after': (3, 1, 3, 2)
    },
    {
        'before': (0, 1, 1, 2),
        'instruction': (6, 3, 1, 2),
        'after': (0, 1, 3, 2)
    },
    {
        'before': (3, 1, 2, 2),
        'instruction': (11, 0, 2, 2),
        'after': (3, 1, 6, 2)
    },
    {
        'before': (2, 3, 2, 0),
        'instruction': (2, 2, 3, 1),
        'after': (2, 3, 2, 0)
    },
    {
        'before': (3, 1, 1, 0),
        'instruction': (13, 1, 3, 3),
        'after': (3, 1, 1, 3)
    },
    {
        'before': (2, 0, 2, 3),
        'instruction': (11, 3, 3, 1),
        'after': (2, 9, 2, 3)
    },
    {
        'before': (1, 3, 3, 1),
        'instruction': (12, 2, 2, 1),
        'after': (1, 2, 3, 1)
    },
    {
        'before': (0, 0, 0, 1),
        'instruction': (3, 0, 0, 3),
        'after': (0, 0, 0, 0)
    },
    {
        'before': (1, 1, 0, 1),
        'instruction': (5, 1, 3, 0),
        'after': (1, 1, 0, 1)
    },
    {
        'before': (1, 1, 0, 3),
        'instruction': (4, 1, 0, 0),
        'after': (1, 1, 0, 3)
    },
    {
        'before': (2, 3, 2, 0),
        'instruction': (15, 0, 2, 2),
        'after': (2, 3, 4, 0)
    },
    {
        'before': (2, 1, 0, 1),
        'instruction': (5, 1, 3, 0),
        'after': (1, 1, 0, 1)
    },
    {
        'before': (1, 2, 3, 3),
        'instruction': (1, 3, 0, 0),
        'after': (3, 2, 3, 3)
    },
    {
        'before': (3, 1, 1, 1),
        'instruction': (5, 1, 3, 0),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (1, 2, 1, 3),
        'instruction': (11, 1, 3, 2),
        'after': (1, 2, 6, 3)
    },
    {
        'before': (1, 1, 0, 2),
        'instruction': (10, 0, 3, 2),
        'after': (1, 1, 3, 2)
    },
    {
        'before': (2, 2, 0, 3),
        'instruction': (11, 1, 3, 3),
        'after': (2, 2, 0, 6)
    },
    {
        'before': (2, 2, 0, 2),
        'instruction': (2, 0, 3, 2),
        'after': (2, 2, 3, 2)
    },
    {
        'before': (1, 1, 2, 1),
        'instruction': (8, 3, 3, 2),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (1, 0, 1, 3),
        'instruction': (9, 2, 3, 1),
        'after': (1, 3, 1, 3)
    },
    {
        'before': (2, 0, 2, 3),
        'instruction': (11, 0, 3, 2),
        'after': (2, 0, 6, 3)
    },
    {
        'before': (1, 1, 2, 0),
        'instruction': (13, 1, 3, 1),
        'after': (1, 3, 2, 0)
    },
    {
        'before': (1, 1, 3, 0),
        'instruction': (4, 1, 0, 2),
        'after': (1, 1, 1, 0)
    },
    {
        'before': (3, 2, 3, 1),
        'instruction': (12, 2, 2, 1),
        'after': (3, 2, 3, 1)
    },
    {
        'before': (0, 2, 3, 3),
        'instruction': (7, 0, 2, 1),
        'after': (0, 0, 3, 3)
    },
    {
        'before': (3, 1, 2, 1),
        'instruction': (15, 2, 1, 3),
        'after': (3, 1, 2, 3)
    },
    {
        'before': (1, 3, 1, 1),
        'instruction': (8, 3, 3, 3),
        'after': (1, 3, 1, 1)
    },
    {
        'before': (1, 1, 0, 1),
        'instruction': (4, 1, 0, 3),
        'after': (1, 1, 0, 1)
    },
    {
        'before': (0, 1, 0, 0),
        'instruction': (15, 0, 1, 0),
        'after': (1, 1, 0, 0)
    },
    {
        'before': (3, 0, 2, 2),
        'instruction': (1, 2, 2, 0),
        'after': (2, 0, 2, 2)
    },
    {
        'before': (0, 0, 2, 0),
        'instruction': (3, 0, 0, 0),
        'after': (0, 0, 2, 0)
    },
    {
        'before': (3, 0, 2, 1),
        'instruction': (6, 3, 2, 2),
        'after': (3, 0, 3, 1)
    },
    {
        'before': (1, 3, 2, 3),
        'instruction': (1, 3, 3, 3),
        'after': (1, 3, 2, 3)
    },
    {
        'before': (1, 1, 2, 1),
        'instruction': (4, 1, 0, 3),
        'after': (1, 1, 2, 1)
    },
    {
        'before': (0, 2, 3, 3),
        'instruction': (11, 2, 3, 2),
        'after': (0, 2, 9, 3)
    },
    {
        'before': (0, 2, 3, 2),
        'instruction': (3, 0, 0, 2),
        'after': (0, 2, 0, 2)
    },
    {
        'before': (1, 0, 2, 1),
        'instruction': (11, 0, 2, 3),
        'after': (1, 0, 2, 2)
    },
    {
        'before': (3, 2, 1, 0),
        'instruction': (13, 2, 3, 2),
        'after': (3, 2, 3, 0)
    },
    {
        'before': (3, 2, 1, 3),
        'instruction': (11, 0, 3, 3),
        'after': (3, 2, 1, 9)
    },
    {
        'before': (3, 0, 2, 3),
        'instruction': (11, 3, 2, 2),
        'after': (3, 0, 6, 3)
    },
    {
        'before': (0, 1, 3, 3),
        'instruction': (9, 1, 3, 0),
        'after': (3, 1, 3, 3)
    },
    {
        'before': (1, 0, 3, 3),
        'instruction': (9, 0, 3, 2),
        'after': (1, 0, 3, 3)
    },
    {
        'before': (2, 1, 2, 0),
        'instruction': (0, 3, 1, 3),
        'after': (2, 1, 2, 1)
    },
    {
        'before': (0, 0, 3, 1),
        'instruction': (8, 3, 3, 3),
        'after': (0, 0, 3, 1)
    },
    {
        'before': (1, 1, 2, 1),
        'instruction': (8, 3, 3, 3),
        'after': (1, 1, 2, 1)
    },
    {
        'before': (1, 2, 2, 3),
        'instruction': (11, 0, 2, 3),
        'after': (1, 2, 2, 2)
    },
    {
        'before': (3, 3, 3, 3),
        'instruction': (1, 3, 1, 1),
        'after': (3, 3, 3, 3)
    },
    {
        'before': (0, 1, 2, 3),
        'instruction': (9, 1, 3, 0),
        'after': (3, 1, 2, 3)
    },
    {
        'before': (1, 1, 0, 3),
        'instruction': (1, 3, 3, 0),
        'after': (3, 1, 0, 3)
    },
    {
        'before': (2, 2, 3, 1),
        'instruction': (6, 3, 2, 3),
        'after': (2, 2, 3, 3)
    },
    {
        'before': (1, 3, 3, 1),
        'instruction': (8, 3, 3, 0),
        'after': (1, 3, 3, 1)
    },
    {
        'before': (0, 2, 3, 1),
        'instruction': (7, 0, 3, 0),
        'after': (0, 2, 3, 1)
    },
    {
        'before': (0, 1, 2, 1),
        'instruction': (5, 1, 3, 3),
        'after': (0, 1, 2, 1)
    },
    {
        'before': (3, 1, 1, 2),
        'instruction': (6, 3, 1, 0),
        'after': (3, 1, 1, 2)
    },
    {
        'before': (1, 1, 2, 1),
        'instruction': (5, 1, 3, 3),
        'after': (1, 1, 2, 1)
    },
    {
        'before': (0, 2, 0, 3),
        'instruction': (7, 0, 1, 3),
        'after': (0, 2, 0, 0)
    },
    {
        'before': (3, 1, 1, 0),
        'instruction': (0, 3, 1, 2),
        'after': (3, 1, 1, 0)
    },
    {
        'before': (3, 1, 0, 1),
        'instruction': (5, 1, 3, 3),
        'after': (3, 1, 0, 1)
    },
    {
        'before': (1, 1, 1, 1),
        'instruction': (8, 2, 3, 3),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (0, 3, 2, 1),
        'instruction': (6, 3, 2, 2),
        'after': (0, 3, 3, 1)
    },
    {
        'before': (0, 2, 1, 3),
        'instruction': (3, 0, 0, 3),
        'after': (0, 2, 1, 0)
    },
    {
        'before': (3, 1, 3, 1),
        'instruction': (6, 3, 2, 1),
        'after': (3, 3, 3, 1)
    },
    {
        'before': (3, 2, 2, 3),
        'instruction': (1, 3, 0, 3),
        'after': (3, 2, 2, 3)
    },
    {
        'before': (3, 2, 1, 1),
        'instruction': (8, 3, 3, 2),
        'after': (3, 2, 1, 1)
    },
    {
        'before': (3, 1, 1, 3),
        'instruction': (1, 3, 1, 2),
        'after': (3, 1, 3, 3)
    },
    {
        'before': (2, 3, 3, 1),
        'instruction': (12, 2, 2, 1),
        'after': (2, 2, 3, 1)
    },
    {
        'before': (3, 1, 3, 0),
        'instruction': (0, 3, 1, 1),
        'after': (3, 1, 3, 0)
    },
    {
        'before': (2, 1, 2, 2),
        'instruction': (10, 1, 3, 0),
        'after': (3, 1, 2, 2)
    },
    {
        'before': (1, 1, 3, 2),
        'instruction': (4, 1, 0, 3),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (0, 1, 0, 0),
        'instruction': (7, 0, 1, 3),
        'after': (0, 1, 0, 0)
    },
    {
        'before': (0, 1, 1, 0),
        'instruction': (0, 3, 1, 1),
        'after': (0, 1, 1, 0)
    },
    {
        'before': (0, 1, 0, 1),
        'instruction': (5, 1, 3, 2),
        'after': (0, 1, 1, 1)
    },
    {
        'before': (2, 1, 1, 1),
        'instruction': (5, 1, 3, 1),
        'after': (2, 1, 1, 1)
    },
    {
        'before': (3, 0, 2, 3),
        'instruction': (11, 0, 3, 3),
        'after': (3, 0, 2, 9)
    },
    {
        'before': (3, 1, 0, 2),
        'instruction': (10, 1, 3, 2),
        'after': (3, 1, 3, 2)
    },
    {
        'before': (1, 2, 2, 3),
        'instruction': (9, 0, 3, 2),
        'after': (1, 2, 3, 3)
    },
    {
        'before': (0, 3, 2, 1),
        'instruction': (14, 1, 2, 3),
        'after': (0, 3, 2, 2)
    },
    {
        'before': (1, 3, 0, 3),
        'instruction': (11, 3, 3, 2),
        'after': (1, 3, 9, 3)
    },
    {
        'before': (0, 0, 2, 1),
        'instruction': (6, 3, 2, 2),
        'after': (0, 0, 3, 1)
    },
    {
        'before': (1, 1, 2, 1),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 2, 1)
    },
    {
        'before': (1, 3, 2, 3),
        'instruction': (11, 1, 2, 0),
        'after': (6, 3, 2, 3)
    },
    {
        'before': (2, 2, 1, 0),
        'instruction': (2, 0, 3, 3),
        'after': (2, 2, 1, 3)
    },
    {
        'before': (0, 1, 1, 0),
        'instruction': (0, 3, 1, 0),
        'after': (1, 1, 1, 0)
    },
    {
        'before': (0, 1, 2, 2),
        'instruction': (6, 3, 1, 0),
        'after': (3, 1, 2, 2)
    },
    {
        'before': (1, 3, 3, 2),
        'instruction': (15, 0, 2, 0),
        'after': (3, 3, 3, 2)
    },
    {
        'before': (3, 2, 3, 2),
        'instruction': (14, 2, 1, 2),
        'after': (3, 2, 2, 2)
    },
    {
        'before': (1, 1, 0, 0),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 0, 0)
    },
    {
        'before': (0, 1, 3, 0),
        'instruction': (0, 3, 1, 0),
        'after': (1, 1, 3, 0)
    },
    {
        'before': (3, 0, 3, 2),
        'instruction': (12, 2, 2, 2),
        'after': (3, 0, 2, 2)
    },
    {
        'before': (0, 0, 2, 1),
        'instruction': (15, 2, 2, 0),
        'after': (4, 0, 2, 1)
    },
    {
        'before': (3, 3, 0, 1),
        'instruction': (8, 3, 3, 0),
        'after': (1, 3, 0, 1)
    },
    {
        'before': (2, 2, 1, 3),
        'instruction': (9, 2, 3, 3),
        'after': (2, 2, 1, 3)
    },
    {
        'before': (0, 3, 1, 0),
        'instruction': (7, 0, 1, 2),
        'after': (0, 3, 0, 0)
    },
    {
        'before': (1, 3, 2, 2),
        'instruction': (14, 1, 2, 2),
        'after': (1, 3, 2, 2)
    },
    {
        'before': (3, 3, 2, 0),
        'instruction': (1, 2, 2, 0),
        'after': (2, 3, 2, 0)
    },
    {
        'before': (1, 1, 3, 2),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 3, 2)
    },
    {
        'before': (1, 0, 2, 2),
        'instruction': (1, 2, 2, 0),
        'after': (2, 0, 2, 2)
    },
    {
        'before': (1, 2, 0, 0),
        'instruction': (2, 1, 3, 3),
        'after': (1, 2, 0, 3)
    },
    {
        'before': (2, 2, 2, 2),
        'instruction': (1, 2, 0, 0),
        'after': (2, 2, 2, 2)
    },
    {
        'before': (0, 3, 2, 2),
        'instruction': (1, 2, 2, 2),
        'after': (0, 3, 2, 2)
    },
    {
        'before': (0, 2, 3, 1),
        'instruction': (8, 3, 3, 2),
        'after': (0, 2, 1, 1)
    },
    {
        'before': (2, 0, 3, 2),
        'instruction': (14, 2, 0, 1),
        'after': (2, 2, 3, 2)
    },
    {
        'before': (1, 1, 1, 3),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 1, 3)
    },
    {
        'before': (1, 1, 3, 2),
        'instruction': (6, 3, 1, 1),
        'after': (1, 3, 3, 2)
    },
    {
        'before': (0, 0, 3, 3),
        'instruction': (1, 3, 1, 1),
        'after': (0, 3, 3, 3)
    },
    {
        'before': (3, 1, 3, 2),
        'instruction': (6, 3, 1, 0),
        'after': (3, 1, 3, 2)
    },
    {
        'before': (2, 3, 3, 2),
        'instruction': (14, 2, 0, 3),
        'after': (2, 3, 3, 2)
    },
    {
        'before': (2, 0, 1, 2),
        'instruction': (10, 2, 3, 3),
        'after': (2, 0, 1, 3)
    },
    {
        'before': (2, 1, 2, 3),
        'instruction': (1, 3, 3, 0),
        'after': (3, 1, 2, 3)
    },
    {
        'before': (0, 1, 1, 2),
        'instruction': (10, 2, 3, 0),
        'after': (3, 1, 1, 2)
    },
    {
        'before': (3, 3, 2, 2),
        'instruction': (2, 2, 3, 1),
        'after': (3, 3, 2, 2)
    },
    {
        'before': (1, 1, 0, 2),
        'instruction': (4, 1, 0, 0),
        'after': (1, 1, 0, 2)
    },
    {
        'before': (3, 2, 2, 1),
        'instruction': (14, 0, 2, 0),
        'after': (2, 2, 2, 1)
    },
    {
        'before': (0, 2, 3, 1),
        'instruction': (7, 0, 1, 2),
        'after': (0, 2, 0, 1)
    },
    {
        'before': (1, 1, 2, 3),
        'instruction': (11, 3, 2, 2),
        'after': (1, 1, 6, 3)
    },
    {
        'before': (1, 2, 2, 3),
        'instruction': (9, 0, 3, 3),
        'after': (1, 2, 2, 3)
    },
    {
        'before': (2, 1, 3, 3),
        'instruction': (9, 1, 3, 3),
        'after': (2, 1, 3, 3)
    },
    {
        'before': (0, 1, 3, 1),
        'instruction': (5, 1, 3, 3),
        'after': (0, 1, 3, 1)
    },
    {
        'before': (0, 0, 2, 3),
        'instruction': (7, 0, 1, 1),
        'after': (0, 0, 2, 3)
    },
    {
        'before': (0, 0, 2, 1),
        'instruction': (7, 0, 2, 0),
        'after': (0, 0, 2, 1)
    },
    {
        'before': (0, 1, 0, 3),
        'instruction': (1, 3, 1, 1),
        'after': (0, 3, 0, 3)
    },
    {
        'before': (3, 2, 3, 3),
        'instruction': (14, 2, 1, 3),
        'after': (3, 2, 3, 2)
    },
    {
        'before': (1, 1, 0, 3),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 0, 3)
    },
    {
        'before': (0, 1, 1, 1),
        'instruction': (5, 1, 3, 3),
        'after': (0, 1, 1, 1)
    },
    {
        'before': (3, 1, 3, 1),
        'instruction': (8, 3, 3, 2),
        'after': (3, 1, 1, 1)
    },
    {
        'before': (1, 1, 1, 0),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 1, 0)
    },
    {
        'before': (1, 2, 2, 3),
        'instruction': (15, 0, 2, 0),
        'after': (3, 2, 2, 3)
    },
    {
        'before': (3, 0, 2, 3),
        'instruction': (1, 3, 1, 3),
        'after': (3, 0, 2, 3)
    },
    {
        'before': (0, 2, 0, 3),
        'instruction': (3, 0, 0, 2),
        'after': (0, 2, 0, 3)
    },
    {
        'before': (2, 3, 0, 3),
        'instruction': (15, 2, 3, 2),
        'after': (2, 3, 3, 3)
    },
    {
        'before': (1, 1, 1, 1),
        'instruction': (5, 1, 3, 2),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (1, 1, 1, 1),
        'instruction': (13, 2, 3, 1),
        'after': (1, 3, 1, 1)
    },
    {
        'before': (2, 2, 2, 1),
        'instruction': (15, 2, 2, 3),
        'after': (2, 2, 2, 4)
    },
    {
        'before': (0, 1, 3, 0),
        'instruction': (12, 2, 2, 1),
        'after': (0, 2, 3, 0)
    },
    {
        'before': (1, 2, 1, 2),
        'instruction': (10, 0, 3, 0),
        'after': (3, 2, 1, 2)
    },
    {
        'before': (1, 0, 3, 1),
        'instruction': (12, 2, 2, 0),
        'after': (2, 0, 3, 1)
    },
    {
        'before': (3, 2, 0, 3),
        'instruction': (15, 2, 3, 1),
        'after': (3, 3, 0, 3)
    },
    {
        'before': (0, 2, 2, 1),
        'instruction': (8, 3, 3, 1),
        'after': (0, 1, 2, 1)
    },
    {
        'before': (2, 2, 1, 3),
        'instruction': (9, 2, 3, 1),
        'after': (2, 3, 1, 3)
    },
    {
        'before': (0, 0, 2, 2),
        'instruction': (15, 2, 2, 1),
        'after': (0, 4, 2, 2)
    },
    {
        'before': (3, 1, 1, 1),
        'instruction': (5, 1, 3, 1),
        'after': (3, 1, 1, 1)
    },
    {
        'before': (1, 1, 3, 1),
        'instruction': (5, 1, 3, 2),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (0, 1, 1, 3),
        'instruction': (15, 0, 1, 3),
        'after': (0, 1, 1, 1)
    },
    {
        'before': (2, 1, 2, 0),
        'instruction': (1, 2, 0, 1),
        'after': (2, 2, 2, 0)
    },
    {
        'before': (0, 1, 1, 0),
        'instruction': (3, 0, 0, 1),
        'after': (0, 0, 1, 0)
    },
    {
        'before': (1, 1, 1, 3),
        'instruction': (9, 2, 3, 1),
        'after': (1, 3, 1, 3)
    },
    {
        'before': (3, 2, 1, 3),
        'instruction': (1, 3, 3, 2),
        'after': (3, 2, 3, 3)
    },
    {
        'before': (0, 1, 2, 3),
        'instruction': (7, 0, 1, 1),
        'after': (0, 0, 2, 3)
    },
    {
        'before': (1, 2, 0, 3),
        'instruction': (9, 0, 3, 3),
        'after': (1, 2, 0, 3)
    },
    {
        'before': (1, 1, 1, 1),
        'instruction': (8, 2, 3, 2),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (0, 0, 1, 1),
        'instruction': (13, 2, 3, 2),
        'after': (0, 0, 3, 1)
    },
    {
        'before': (2, 2, 3, 3),
        'instruction': (14, 2, 1, 0),
        'after': (2, 2, 3, 3)
    },
    {
        'before': (3, 2, 0, 3),
        'instruction': (11, 0, 3, 1),
        'after': (3, 9, 0, 3)
    },
    {
        'before': (0, 1, 1, 2),
        'instruction': (10, 2, 3, 2),
        'after': (0, 1, 3, 2)
    },
    {
        'before': (0, 3, 0, 3),
        'instruction': (3, 0, 0, 2),
        'after': (0, 3, 0, 3)
    },
    {
        'before': (1, 3, 3, 0),
        'instruction': (13, 0, 3, 1),
        'after': (1, 3, 3, 0)
    },
    {
        'before': (1, 3, 1, 1),
        'instruction': (13, 2, 3, 1),
        'after': (1, 3, 1, 1)
    },
    {
        'before': (1, 1, 0, 3),
        'instruction': (0, 2, 1, 1),
        'after': (1, 1, 0, 3)
    },
    {
        'before': (2, 1, 3, 1),
        'instruction': (5, 1, 3, 2),
        'after': (2, 1, 1, 1)
    },
    {
        'before': (0, 1, 0, 3),
        'instruction': (1, 3, 1, 0),
        'after': (3, 1, 0, 3)
    },
    {
        'before': (3, 2, 3, 2),
        'instruction': (2, 1, 3, 2),
        'after': (3, 2, 3, 2)
    },
    {
        'before': (0, 1, 3, 3),
        'instruction': (11, 3, 3, 3),
        'after': (0, 1, 3, 9)
    },
    {
        'before': (1, 1, 0, 2),
        'instruction': (6, 3, 1, 1),
        'after': (1, 3, 0, 2)
    },
    {
        'before': (1, 1, 3, 1),
        'instruction': (4, 1, 0, 1),
        'after': (1, 1, 3, 1)
    },
    {
        'before': (2, 1, 0, 2),
        'instruction': (6, 3, 1, 0),
        'after': (3, 1, 0, 2)
    },
    {
        'before': (0, 0, 2, 3),
        'instruction': (1, 3, 0, 2),
        'after': (0, 0, 3, 3)
    },
    {
        'before': (1, 2, 2, 0),
        'instruction': (2, 2, 3, 3),
        'after': (1, 2, 2, 3)
    },
    {
        'before': (1, 1, 1, 1),
        'instruction': (5, 1, 3, 3),
        'after': (1, 1, 1, 1)
    },
    {
        'before': (3, 2, 2, 0),
        'instruction': (14, 0, 2, 2),
        'after': (3, 2, 2, 0)
    },
    {
        'before': (1, 2, 1, 2),
        'instruction': (10, 2, 3, 3),
        'after': (1, 2, 1, 3)
    },
    {
        'before': (0, 1, 1, 1),
        'instruction': (5, 1, 3, 1),
        'after': (0, 1, 1, 1)
    },
    {
        'before': (3, 2, 2, 0),
        'instruction': (15, 3, 2, 3),
        'after': (3, 2, 2, 2)
    },
    {
        'before': (3, 0, 2, 0),
        'instruction': (11, 0, 2, 2),
        'after': (3, 0, 6, 0)
    },
    {
        'before': (1, 0, 0, 1),
        'instruction': (13, 0, 3, 1),
        'after': (1, 3, 0, 1)
    },
    {
        'before': (0, 1, 3, 3),
        'instruction': (9, 1, 3, 3),
        'after': (0, 1, 3, 3)
    },
    {
        'before': (0, 0, 2, 3),
        'instruction': (11, 2, 3, 0),
        'after': (6, 0, 2, 3)
    },
    {
        'before': (3, 3, 3, 3),
        'instruction': (1, 3, 0, 1),
        'after': (3, 3, 3, 3)
    },
    {
        'before': (2, 3, 1, 0),
        'instruction': (13, 2, 3, 3),
        'after': (2, 3, 1, 3)
    }
]

# List of istructions
test_program = [
    (6, 1, 3, 1),
    (6, 2, 3, 2),
    (6, 1, 2, 0),
    (1, 0, 2, 1),
    (13, 1, 3, 1),
    (10, 1, 3, 3),
    (6, 1, 2, 2),
    (6, 1, 1, 1),
    (10, 1, 0, 0),
    (13, 0, 1, 0),
    (10, 0, 3, 3),
    (1, 3, 2, 1),
    (6, 3, 2, 2),
    (6, 3, 0, 0),
    (6, 3, 1, 3),
    (12, 0, 2, 3),
    (13, 3, 3, 3),
    (10, 1, 3, 1),
    (1, 1, 1, 0),
    (6, 0, 3, 1),
    (13, 0, 0, 2),
    (15, 2, 0, 2),
    (6, 0, 3, 3),
    (6, 3, 2, 2),
    (13, 2, 1, 2),
    (13, 2, 3, 2),
    (10, 0, 2, 0),
    (1, 0, 2, 3),
    (13, 0, 0, 0),
    (15, 0, 2, 0),
    (6, 3, 1, 1),
    (6, 3, 3, 2),
    (7, 0, 2, 2),
    (13, 2, 2, 2),
    (10, 3, 2, 3),
    (1, 3, 2, 0),
    (6, 2, 2, 1),
    (6, 2, 0, 2),
    (6, 0, 0, 3),
    (0, 3, 2, 1),
    (13, 1, 3, 1),
    (13, 1, 1, 1),
    (10, 0, 1, 0),
    (1, 0, 3, 3),
    (13, 3, 0, 2),
    (15, 2, 3, 2),
    (13, 0, 0, 0),
    (15, 0, 3, 0),
    (6, 0, 0, 1),
    (12, 0, 2, 1),
    (13, 1, 3, 1),
    (10, 1, 3, 3),
    (1, 3, 2, 1),
    (6, 2, 1, 2),
    (6, 0, 3, 3),
    (6, 1, 0, 0),
    (1, 0, 2, 0),
    (13, 0, 1, 0),
    (13, 0, 1, 0),
    (10, 0, 1, 1),
    (6, 3, 2, 0),
    (13, 1, 0, 3),
    (15, 3, 1, 3),
    (9, 2, 0, 3),
    (13, 3, 1, 3),
    (13, 3, 2, 3),
    (10, 1, 3, 1),
    (1, 1, 0, 2),
    (13, 1, 0, 0),
    (15, 0, 1, 0),
    (6, 3, 3, 1),
    (6, 2, 3, 3),
    (15, 0, 1, 0),
    (13, 0, 3, 0),
    (10, 0, 2, 2),
    (1, 2, 1, 1),
    (6, 0, 0, 0),
    (6, 3, 2, 2),
    (6, 2, 0, 2),
    (13, 2, 1, 2),
    (13, 2, 3, 2),
    (10, 2, 1, 1),
    (6, 1, 2, 2),
    (6, 2, 0, 0),
    (8, 0, 3, 0),
    (13, 0, 2, 0),
    (10, 0, 1, 1),
    (6, 3, 3, 2),
    (6, 2, 2, 0),
    (8, 0, 3, 3),
    (13, 3, 2, 3),
    (10, 1, 3, 1),
    (1, 1, 3, 0),
    (6, 3, 3, 1),
    (6, 1, 3, 3),
    (13, 3, 2, 1),
    (13, 1, 3, 1),
    (10, 0, 1, 0),
    (1, 0, 2, 1),
    (13, 1, 0, 2),
    (15, 2, 2, 2),
    (6, 1, 1, 0),
    (6, 3, 2, 3),
    (1, 0, 2, 0),
    (13, 0, 3, 0),
    (10, 1, 0, 1),
    (1, 1, 2, 3),
    (6, 3, 2, 1),
    (6, 2, 1, 0),
    (6, 3, 0, 2),
    (7, 0, 2, 0),
    (13, 0, 3, 0),
    (10, 0, 3, 3),
    (1, 3, 0, 2),
    (6, 2, 2, 0),
    (13, 0, 0, 3),
    (15, 3, 2, 3),
    (13, 1, 0, 1),
    (15, 1, 1, 1),
    (8, 0, 3, 1),
    (13, 1, 1, 1),
    (10, 2, 1, 2),
    (1, 2, 0, 1),
    (13, 2, 0, 3),
    (15, 3, 0, 3),
    (13, 3, 0, 0),
    (15, 0, 1, 0),
    (6, 3, 0, 2),
    (5, 3, 2, 2),
    (13, 2, 1, 2),
    (13, 2, 3, 2),
    (10, 1, 2, 1),
    (6, 3, 2, 3),
    (13, 1, 0, 0),
    (15, 0, 2, 0),
    (6, 3, 0, 2),
    (14, 3, 0, 2),
    (13, 2, 2, 2),
    (13, 2, 3, 2),
    (10, 1, 2, 1),
    (1, 1, 2, 2),
    (6, 2, 0, 1),
    (6, 2, 3, 3),
    (6, 3, 0, 3),
    (13, 3, 2, 3),
    (10, 3, 2, 2),
    (1, 2, 2, 3),
    (6, 2, 0, 2),
    (13, 3, 0, 1),
    (15, 1, 3, 1),
    (14, 1, 0, 0),
    (13, 0, 2, 0),
    (10, 0, 3, 3),
    (1, 3, 1, 1),
    (6, 0, 3, 3),
    (6, 3, 2, 0),
    (6, 0, 0, 2),
    (7, 2, 0, 3),
    (13, 3, 1, 3),
    (10, 1, 3, 1),
    (6, 2, 1, 3),
    (12, 0, 2, 0),
    (13, 0, 1, 0),
    (10, 1, 0, 1),
    (1, 1, 2, 3),
    (6, 2, 1, 2),
    (6, 1, 3, 0),
    (13, 0, 0, 1),
    (15, 1, 0, 1),
    (1, 0, 2, 2),
    (13, 2, 3, 2),
    (13, 2, 2, 2),
    (10, 3, 2, 3),
    (6, 3, 1, 2),
    (15, 0, 1, 2),
    (13, 2, 2, 2),
    (13, 2, 1, 2),
    (10, 3, 2, 3),
    (1, 3, 1, 0),
    (6, 1, 0, 1),
    (13, 3, 0, 3),
    (15, 3, 1, 3),
    (13, 3, 0, 2),
    (15, 2, 0, 2),
    (13, 1, 2, 1),
    (13, 1, 2, 1),
    (10, 0, 1, 0),
    (1, 0, 2, 1),
    (13, 2, 0, 2),
    (15, 2, 3, 2),
    (6, 2, 0, 3),
    (6, 2, 3, 0),
    (8, 0, 3, 0),
    (13, 0, 3, 0),
    (13, 0, 1, 0),
    (10, 1, 0, 1),
    (13, 0, 0, 2),
    (15, 2, 2, 2),
    (6, 1, 3, 0),
    (1, 0, 2, 3),
    (13, 3, 2, 3),
    (13, 3, 2, 3),
    (10, 3, 1, 1),
    (6, 0, 1, 0),
    (6, 0, 3, 3),
    (0, 3, 2, 0),
    (13, 0, 2, 0),
    (13, 0, 1, 0),
    (10, 0, 1, 1),
    (6, 2, 1, 0),
    (6, 2, 2, 3),
    (8, 0, 3, 0),
    (13, 0, 1, 0),
    (13, 0, 2, 0),
    (10, 0, 1, 1),
    (1, 1, 3, 3),
    (6, 3, 3, 2),
    (13, 1, 0, 0),
    (15, 0, 1, 0),
    (6, 2, 1, 1),
    (9, 1, 2, 0),
    (13, 0, 1, 0),
    (10, 0, 3, 3),
    (1, 3, 1, 2),
    (6, 2, 1, 0),
    (13, 1, 0, 1),
    (15, 1, 0, 1),
    (6, 3, 1, 3),
    (14, 3, 0, 3),
    (13, 3, 2, 3),
    (10, 3, 2, 2),
    (1, 2, 1, 0),
    (13, 0, 0, 3),
    (15, 3, 2, 3),
    (6, 1, 3, 1),
    (6, 3, 0, 2),
    (11, 1, 3, 1),
    (13, 1, 1, 1),
    (10, 0, 1, 0),
    (6, 1, 3, 2),
    (6, 0, 0, 3),
    (6, 3, 2, 1),
    (12, 1, 2, 1),
    (13, 1, 2, 1),
    (10, 1, 0, 0),
    (6, 3, 1, 1),
    (6, 1, 2, 3),
    (6, 2, 2, 2),
    (15, 3, 1, 3),
    (13, 3, 3, 3),
    (13, 3, 3, 3),
    (10, 3, 0, 0),
    (1, 0, 0, 1),
    (6, 0, 3, 0),
    (6, 2, 1, 3),
    (2, 2, 3, 2),
    (13, 2, 3, 2),
    (13, 2, 2, 2),
    (10, 1, 2, 1),
    (1, 1, 2, 0),
    (6, 2, 3, 2),
    (6, 0, 1, 3),
    (6, 3, 3, 1),
    (0, 3, 2, 2),
    (13, 2, 2, 2),
    (13, 2, 3, 2),
    (10, 0, 2, 0),
    (1, 0, 2, 1),
    (6, 3, 0, 0),
    (6, 2, 2, 3),
    (6, 0, 3, 2),
    (7, 2, 0, 0),
    (13, 0, 3, 0),
    (13, 0, 2, 0),
    (10, 0, 1, 1),
    (13, 1, 0, 0),
    (15, 0, 1, 0),
    (6, 3, 0, 2),
    (11, 0, 3, 2),
    (13, 2, 1, 2),
    (13, 2, 1, 2),
    (10, 2, 1, 1),
    (1, 1, 2, 2),
    (6, 0, 1, 1),
    (6, 3, 1, 3),
    (15, 0, 1, 3),
    (13, 3, 3, 3),
    (13, 3, 3, 3),
    (10, 3, 2, 2),
    (1, 2, 0, 3),
    (6, 2, 0, 1),
    (13, 1, 0, 0),
    (15, 0, 3, 0),
    (13, 0, 0, 2),
    (15, 2, 2, 2),
    (4, 2, 0, 0),
    (13, 0, 2, 0),
    (13, 0, 2, 0),
    (10, 0, 3, 3),
    (1, 3, 1, 1),
    (6, 1, 2, 3),
    (13, 3, 0, 0),
    (15, 0, 1, 0),
    (1, 0, 2, 2),
    (13, 2, 2, 2),
    (10, 2, 1, 1),
    (6, 3, 2, 2),
    (6, 3, 2, 0),
    (6, 3, 0, 3),
    (12, 3, 2, 0),
    (13, 0, 1, 0),
    (13, 0, 2, 0),
    (10, 1, 0, 1),
    (1, 1, 1, 0),
    (6, 0, 1, 2),
    (6, 2, 2, 3),
    (6, 0, 1, 1),
    (5, 2, 3, 2),
    (13, 2, 3, 2),
    (10, 0, 2, 0),
    (1, 0, 2, 2),
    (13, 0, 0, 1),
    (15, 1, 1, 1),
    (6, 1, 2, 0),
    (11, 0, 3, 3),
    (13, 3, 3, 3),
    (13, 3, 3, 3),
    (10, 2, 3, 2),
    (1, 2, 0, 0),
    (6, 3, 3, 1),
    (6, 3, 3, 2),
    (6, 2, 1, 3),
    (14, 1, 3, 2),
    (13, 2, 1, 2),
    (10, 0, 2, 0),
    (1, 0, 0, 3),
    (6, 1, 2, 1),
    (6, 3, 1, 2),
    (13, 1, 0, 0),
    (15, 0, 0, 0),
    (13, 1, 2, 2),
    (13, 2, 3, 2),
    (10, 3, 2, 3),
    (1, 3, 0, 1),
    (6, 1, 2, 3),
    (6, 2, 2, 0),
    (6, 0, 2, 2),
    (3, 0, 3, 0),
    (13, 0, 2, 0),
    (13, 0, 3, 0),
    (10, 0, 1, 1),
    (1, 1, 3, 3),
    (6, 2, 2, 0),
    (13, 3, 0, 1),
    (15, 1, 1, 1),
    (11, 1, 0, 2),
    (13, 2, 3, 2),
    (10, 2, 3, 3),
    (1, 3, 0, 2),
    (6, 0, 2, 0),
    (13, 2, 0, 3),
    (15, 3, 3, 3),
    (13, 2, 0, 1),
    (15, 1, 2, 1),
    (14, 3, 1, 3),
    (13, 3, 3, 3),
    (13, 3, 2, 3),
    (10, 2, 3, 2),
    (1, 2, 0, 0),
    (6, 0, 3, 3),
    (6, 3, 1, 1),
    (6, 2, 0, 2),
    (2, 2, 3, 2),
    (13, 2, 2, 2),
    (10, 2, 0, 0),
    (1, 0, 2, 1),
    (6, 3, 2, 0),
    (13, 0, 0, 2),
    (15, 2, 2, 2),
    (0, 3, 2, 0),
    (13, 0, 1, 0),
    (10, 0, 1, 1),
    (1, 1, 0, 3),
    (6, 0, 2, 1),
    (6, 0, 0, 2),
    (6, 1, 3, 0),
    (10, 0, 0, 1),
    (13, 1, 2, 1),
    (10, 1, 3, 3),
    (6, 0, 1, 1),
    (13, 0, 0, 0),
    (15, 0, 3, 0),
    (7, 2, 0, 0),
    (13, 0, 2, 0),
    (10, 0, 3, 3),
    (1, 3, 2, 1),
    (6, 2, 2, 0),
    (6, 0, 0, 3),
    (6, 3, 1, 2),
    (7, 0, 2, 3),
    (13, 3, 2, 3),
    (13, 3, 1, 3),
    (10, 3, 1, 1),
    (6, 2, 0, 3),
    (13, 1, 0, 2),
    (15, 2, 2, 2),
    (6, 1, 3, 0),
    (1, 0, 2, 0),
    (13, 0, 1, 0),
    (13, 0, 1, 0),
    (10, 0, 1, 1),
    (1, 1, 0, 2),
    (13, 1, 0, 0),
    (15, 0, 2, 0),
    (6, 3, 2, 3),
    (6, 3, 0, 1),
    (14, 3, 0, 1),
    (13, 1, 3, 1),
    (10, 1, 2, 2),
    (1, 2, 0, 1),
    (6, 2, 1, 3),
    (6, 1, 1, 2),
    (8, 0, 3, 2),
    (13, 2, 1, 2),
    (10, 2, 1, 1),
    (6, 2, 1, 2),
    (6, 3, 3, 0),
    (6, 3, 3, 3),
    (4, 2, 0, 2),
    (13, 2, 1, 2),
    (10, 1, 2, 1),
    (1, 1, 1, 2),
    (6, 1, 0, 3),
    (6, 2, 3, 1),
    (9, 1, 0, 1),
    (13, 1, 2, 1),
    (10, 2, 1, 2),
    (6, 1, 3, 1),
    (6, 2, 3, 3),
    (6, 2, 1, 0),
    (2, 0, 3, 3),
    (13, 3, 3, 3),
    (10, 2, 3, 2),
    (1, 2, 1, 1),
    (6, 3, 2, 0),
    (6, 2, 0, 2),
    (13, 3, 0, 3),
    (15, 3, 3, 3),
    (9, 2, 0, 0),
    (13, 0, 2, 0),
    (10, 0, 1, 1),
    (1, 1, 2, 2),
    (6, 2, 2, 0),
    (6, 0, 1, 3),
    (6, 3, 2, 1),
    (14, 1, 0, 0),
    (13, 0, 1, 0),
    (10, 2, 0, 2),
    (13, 2, 0, 0),
    (15, 0, 1, 0),
    (13, 0, 0, 1),
    (15, 1, 2, 1),
    (2, 1, 3, 0),
    (13, 0, 3, 0),
    (10, 2, 0, 2),
    (6, 3, 2, 1),
    (6, 2, 2, 0),
    (6, 2, 3, 3),
    (14, 1, 0, 0),
    (13, 0, 3, 0),
    (13, 0, 3, 0),
    (10, 0, 2, 2),
    (1, 2, 1, 0),
    (13, 2, 0, 2),
    (15, 2, 2, 2),
    (6, 0, 2, 3),
    (0, 3, 2, 1),
    (13, 1, 3, 1),
    (10, 0, 1, 0),
    (1, 0, 3, 3),
    (6, 0, 1, 1),
    (6, 1, 1, 0),
    (1, 0, 2, 0),
    (13, 0, 3, 0),
    (10, 0, 3, 3),
    (1, 3, 3, 0),
    (6, 1, 0, 3),
    (6, 1, 0, 1),
    (6, 3, 2, 2),
    (13, 1, 2, 1),
    (13, 1, 1, 1),
    (10, 1, 0, 0),
    (1, 0, 0, 1),
    (6, 0, 2, 0),
    (6, 1, 1, 2),
    (6, 2, 3, 3),
    (6, 2, 0, 0),
    (13, 0, 1, 0),
    (13, 0, 2, 0),
    (10, 1, 0, 1),
    (1, 1, 1, 0),
    (6, 1, 2, 1),
    (6, 3, 0, 2),
    (13, 2, 0, 3),
    (15, 3, 0, 3),
    (13, 1, 2, 1),
    (13, 1, 3, 1),
    (13, 1, 1, 1),
    (10, 0, 1, 0),
    (1, 0, 3, 1),
    (6, 3, 3, 0),
    (12, 0, 2, 0),
    (13, 0, 3, 0),
    (13, 0, 2, 0),
    (10, 0, 1, 1),
    (1, 1, 0, 3),
    (6, 3, 1, 1),
    (6, 2, 0, 0),
    (7, 0, 2, 1),
    (13, 1, 2, 1),
    (10, 1, 3, 3),
    (6, 1, 0, 2),
    (13, 2, 0, 0),
    (15, 0, 1, 0),
    (6, 0, 1, 1),
    (15, 0, 1, 0),
    (13, 0, 2, 0),
    (13, 0, 3, 0),
    (10, 0, 3, 3),
    (1, 3, 3, 1),
    (6, 0, 2, 2),
    (6, 1, 1, 0),
    (6, 0, 0, 3),
    (10, 0, 0, 2),
    (13, 2, 3, 2),
    (10, 1, 2, 1),
    (1, 1, 2, 3),
    (6, 3, 0, 2),
    (6, 0, 1, 1),
    (15, 0, 1, 0),
    (13, 0, 3, 0),
    (10, 0, 3, 3),
    (1, 3, 3, 1),
    (13, 3, 0, 0),
    (15, 0, 2, 0),
    (13, 0, 0, 3),
    (15, 3, 1, 3),
    (6, 2, 1, 2),
    (3, 0, 3, 2),
    (13, 2, 2, 2),
    (13, 2, 2, 2),
    (10, 1, 2, 1),
    (6, 1, 1, 0),
    (13, 0, 0, 3),
    (15, 3, 0, 3),
    (6, 3, 2, 2),
    (5, 3, 2, 3),
    (13, 3, 1, 3),
    (13, 3, 2, 3),
    (10, 1, 3, 1),
    (6, 1, 0, 2),
    (6, 2, 1, 0),
    (6, 1, 1, 3),
    (3, 0, 3, 3),
    (13, 3, 1, 3),
    (10, 1, 3, 1),
    (6, 0, 2, 3),
    (6, 2, 2, 2),
    (6, 1, 2, 0),
    (0, 3, 2, 0),
    (13, 0, 2, 0),
    (10, 1, 0, 1),
    (1, 1, 3, 0),
    (6, 2, 1, 1),
    (0, 3, 2, 3),
    (13, 3, 2, 3),
    (10, 0, 3, 0),
    (1, 0, 2, 1),
    (6, 2, 3, 0),
    (6, 0, 0, 3),
    (0, 3, 2, 2),
    (13, 2, 3, 2),
    (10, 2, 1, 1),
    (1, 1, 0, 2),
    (6, 1, 3, 1),
    (6, 3, 1, 0),
    (13, 0, 1, 0),
    (10, 0, 2, 2),
    (1, 2, 3, 1),
    (6, 3, 1, 2),
    (6, 2, 3, 3),
    (6, 2, 0, 0),
    (9, 0, 2, 0),
    (13, 0, 1, 0),
    (10, 0, 1, 1),
    (1, 1, 1, 3),
    (6, 3, 2, 0),
    (13, 1, 0, 2),
    (15, 2, 0, 2),
    (13, 0, 0, 1),
    (15, 1, 1, 1),
    (7, 2, 0, 2),
    (13, 2, 1, 2),
    (13, 2, 1, 2),
    (10, 2, 3, 3),
    (6, 3, 1, 1),
    (13, 0, 0, 0),
    (15, 0, 2, 0),
    (6, 0, 1, 2),
    (12, 1, 2, 2),
    (13, 2, 2, 2),
    (10, 3, 2, 3),
    (1, 3, 2, 1),
    (6, 1, 2, 2),
    (6, 1, 3, 0),
    (6, 2, 0, 3),
    (10, 0, 0, 2),
    (13, 2, 1, 2),
    (13, 2, 1, 2),
    (10, 2, 1, 1),
    (6, 1, 1, 3),
    (13, 1, 0, 0),
    (15, 0, 2, 0),
    (13, 1, 0, 2),
    (15, 2, 2, 2),
    (11, 3, 0, 0),
    (13, 0, 3, 0),
    (13, 0, 2, 0),
    (10, 1, 0, 1),
    (13, 3, 0, 2),
    (15, 2, 0, 2),
    (6, 3, 2, 0),
    (6, 3, 3, 3),
    (12, 0, 2, 2),
    (13, 2, 2, 2),
    (13, 2, 1, 2),
    (10, 2, 1, 1),
    (1, 1, 3, 2),
    (6, 2, 3, 3),
    (6, 2, 2, 1),
    (2, 1, 3, 3),
    (13, 3, 2, 3),
    (10, 2, 3, 2),
    (1, 2, 2, 3),
    (6, 1, 3, 1),
    (6, 2, 1, 2),
    (6, 1, 1, 0),
    (1, 0, 2, 2),
    (13, 2, 1, 2),
    (10, 3, 2, 3),
    (6, 3, 0, 0),
    (6, 3, 3, 1),
    (6, 3, 0, 2),
    (12, 1, 2, 1),
    (13, 1, 2, 1),
    (10, 3, 1, 3),
    (6, 0, 1, 0),
    (6, 2, 2, 1),
    (9, 1, 2, 1),
    (13, 1, 3, 1),
    (10, 1, 3, 3),
    (1, 3, 0, 1),
    (6, 0, 2, 3),
    (13, 2, 0, 2),
    (15, 2, 0, 2),
    (6, 3, 0, 0),
    (12, 0, 2, 3),
    (13, 3, 2, 3),
    (13, 3, 2, 3),
    (10, 3, 1, 1),
    (1, 1, 1, 3),
    (6, 3, 3, 1),
    (7, 2, 0, 1),
    (13, 1, 1, 1),
    (13, 1, 3, 1),
    (10, 1, 3, 3),
    (1, 3, 2, 0),
    (6, 0, 2, 3),
    (6, 1, 0, 1),
    (13, 1, 2, 2),
    (13, 2, 2, 2),
    (10, 2, 0, 0),
    (6, 1, 3, 3),
    (6, 3, 2, 1),
    (6, 3, 3, 2),
    (13, 3, 2, 3),
    (13, 3, 3, 3),
    (10, 0, 3, 0),
    (1, 0, 0, 1),
    (13, 3, 0, 3),
    (15, 3, 0, 3),
    (13, 0, 0, 2),
    (15, 2, 2, 2),
    (6, 2, 2, 0),
    (0, 3, 2, 3),
    (13, 3, 2, 3),
    (10, 3, 1, 1),
    (1, 1, 1, 0),
    (6, 1, 1, 3),
    (13, 3, 0, 2),
    (15, 2, 3, 2),
    (6, 3, 2, 1),
    (13, 3, 2, 2),
    (13, 2, 3, 2),
    (10, 2, 0, 0),
    (1, 0, 1, 1),
    (6, 3, 2, 3),
    (6, 1, 3, 2),
    (6, 0, 0, 0),
    (12, 3, 2, 3),
    (13, 3, 1, 3),
    (10, 1, 3, 1),
    (1, 1, 1, 3),
    (13, 0, 0, 1),
    (15, 1, 1, 1),
    (6, 2, 1, 2),
    (6, 1, 3, 0),
    (1, 0, 2, 0),
    (13, 0, 2, 0),
    (10, 0, 3, 3),
    (1, 3, 3, 0),
    (6, 0, 3, 3),
    (6, 3, 1, 1),
    (4, 2, 1, 1),
    (13, 1, 1, 1),
    (10, 1, 0, 0),
    (1, 0, 0, 3),
    (6, 2, 1, 1),
    (6, 3, 2, 0),
    (13, 2, 0, 2),
    (15, 2, 0, 2),
    (7, 2, 0, 0),
    (13, 0, 3, 0),
    (13, 0, 1, 0),
    (10, 0, 3, 3),
    (1, 3, 2, 1),
    (6, 0, 1, 0),
    (6, 0, 3, 3),
    (6, 2, 1, 2),
    (0, 3, 2, 3),
    (13, 3, 2, 3),
    (10, 1, 3, 1),
    (6, 1, 2, 3),
    (6, 3, 1, 0),
    (4, 2, 0, 0),
    (13, 0, 1, 0),
    (13, 0, 1, 0),
    (10, 0, 1, 1),
    (1, 1, 0, 3),
    (6, 2, 0, 0),
    (6, 3, 1, 2),
    (13, 1, 0, 1),
    (15, 1, 0, 1),
    (9, 0, 2, 0),
    (13, 0, 2, 0),
    (10, 3, 0, 3),
    (1, 3, 0, 2),
    (13, 3, 0, 0),
    (15, 0, 2, 0),
    (6, 1, 1, 3),
    (15, 3, 1, 0),
    (13, 0, 1, 0),
    (10, 2, 0, 2),
    (1, 2, 3, 0),
    (6, 2, 1, 3),
    (6, 0, 0, 2),
    (6, 1, 1, 1),
    (11, 1, 3, 2),
    (13, 2, 2, 2),
    (10, 0, 2, 0),
    (1, 0, 3, 2),
    (6, 0, 2, 0),
    (6, 0, 0, 3),
    (6, 3, 1, 0),
    (13, 0, 2, 0),
    (10, 0, 2, 2),
    (1, 2, 3, 3),
    (6, 3, 0, 2),
    (13, 0, 0, 0),
    (15, 0, 2, 0),
    (7, 0, 2, 0),
    (13, 0, 1, 0),
    (13, 0, 3, 0),
    (10, 3, 0, 3),
    (1, 3, 3, 2),
    (6, 1, 0, 0),
    (6, 2, 2, 3),
    (11, 1, 3, 3),
    (13, 3, 3, 3),
    (10, 3, 2, 2),
    (1, 2, 3, 1),
    (6, 1, 1, 3),
    (13, 0, 0, 0),
    (15, 0, 2, 0),
    (6, 2, 3, 2),
    (3, 0, 3, 0),
    (13, 0, 3, 0),
    (10, 0, 1, 1),
    (13, 2, 0, 3),
    (15, 3, 2, 3),
    (6, 3, 3, 0),
    (6, 0, 1, 2),
    (5, 2, 3, 0),
    (13, 0, 2, 0),
    (10, 1, 0, 1),
    (1, 1, 1, 3),
    (6, 3, 1, 2),
    (6, 3, 0, 1),
    (6, 2, 1, 0),
    (4, 0, 1, 2),
    (13, 2, 1, 2),
    (10, 3, 2, 3),
    (1, 3, 2, 0),
    (6, 0, 3, 2),
    (6, 0, 1, 1),
    (6, 2, 2, 3),
    (5, 2, 3, 1),
    (13, 1, 3, 1),
    (10, 1, 0, 0),
    (1, 0, 3, 1),
    (13, 1, 0, 2),
    (15, 2, 1, 2),
    (6, 2, 0, 0),
    (13, 3, 0, 3),
    (15, 3, 3, 3),
    (14, 3, 0, 3),
    (13, 3, 3, 3),
    (13, 3, 3, 3),
    (10, 1, 3, 1),
    (1, 1, 0, 2),
    (6, 1, 0, 3),
    (6, 1, 2, 1),
    (3, 0, 3, 1),
    (13, 1, 3, 1),
    (10, 1, 2, 2),
    (1, 2, 0, 1),
    (6, 3, 1, 2),
    (6, 0, 0, 3),
    (5, 3, 2, 2),
    (13, 2, 1, 2),
    (10, 1, 2, 1),
    (1, 1, 2, 0),
    (13, 1, 0, 1),
    (15, 1, 2, 1),
    (6, 2, 3, 2),
    (0, 3, 2, 2),
    (13, 2, 3, 2),
    (10, 0, 2, 0),
    (1, 0, 1, 1),
    (13, 3, 0, 0),
    (15, 0, 1, 0),
    (6, 2, 2, 2),
    (6, 1, 3, 3),
    (1, 0, 2, 0),
    (13, 0, 1, 0),
    (10, 1, 0, 1),
    (1, 1, 0, 3),
    (6, 2, 2, 1),
    (13, 1, 0, 0),
    (15, 0, 3, 0),
    (6, 1, 1, 2),
    (6, 2, 0, 1),
    (13, 1, 1, 1),
    (10, 3, 1, 3),
    (1, 3, 3, 0),
    (6, 3, 1, 2),
    (6, 1, 0, 1),
    (6, 2, 3, 3),
    (13, 1, 2, 3),
    (13, 3, 2, 3),
    (13, 3, 3, 3),
    (10, 3, 0, 0),
    (1, 0, 3, 1),
    (6, 1, 0, 0),
    (6, 3, 3, 3),
    (6, 1, 1, 2),
    (12, 3, 2, 0),
    (13, 0, 1, 0),
    (13, 0, 2, 0),
    (10, 0, 1, 1),
    (1, 1, 2, 2),
    (6, 3, 0, 0),
    (13, 0, 0, 1),
    (15, 1, 2, 1),
    (6, 1, 1, 3),
    (9, 1, 0, 3),
    (13, 3, 1, 3),
    (10, 2, 3, 2),
    (1, 2, 2, 0),
    (6, 0, 2, 2),
    (6, 0, 0, 1),
    (6, 1, 1, 3),
    (10, 3, 3, 1),
    (13, 1, 2, 1),
    (10, 0, 1, 0),
    (1, 0, 0, 1),
    (6, 1, 1, 0),
    (6, 2, 0, 2),
    (6, 3, 1, 3),
    (1, 0, 2, 3),
    (13, 3, 2, 3),
    (10, 3, 1, 1),
    (1, 1, 2, 0),
    (13, 3, 0, 1),
    (15, 1, 3, 1),
    (6, 1, 0, 3),
    (13, 1, 0, 2),
    (15, 2, 3, 2),
    (15, 3, 1, 2),
    (13, 2, 3, 2),
    (10, 2, 0, 0),
    (1, 0, 2, 2),
    (6, 1, 3, 0),
    (10, 0, 0, 1),
    (13, 1, 2, 1),
    (10, 2, 1, 2),
    (1, 2, 2, 1),
    (13, 0, 0, 2),
    (15, 2, 3, 2),
    (6, 3, 3, 0),
    (13, 3, 2, 0),
    (13, 0, 3, 0),
    (10, 1, 0, 1),
    (1, 1, 0, 0),
    (6, 0, 3, 3),
    (13, 1, 0, 1),
    (15, 1, 0, 1),
    (5, 3, 2, 1),
    (13, 1, 2, 1),
    (10, 0, 1, 0),
    (1, 0, 0, 2),
    (13, 1, 0, 1),
    (15, 1, 2, 1),
    (13, 1, 0, 3),
    (15, 3, 3, 3),
    (6, 2, 1, 0),
    (14, 3, 1, 0),
    (13, 0, 3, 0),
    (10, 0, 2, 2),
    (1, 2, 0, 0)
]
