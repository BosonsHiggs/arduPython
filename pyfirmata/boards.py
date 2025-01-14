BOARDS = {
    'arduino_uno': {
        'digital': tuple(x for x in range(14)),
        'analog': tuple(x for x in range(6)),
        'pwm': (3, 5, 6, 9, 10, 11),
        'use_ports': True,
        'disabled': (0, 1)  # Rx, Tx, Crystal
    },
    'arduino_mega': {
        'digital': tuple(x for x in range(54)),
        'analog': tuple(x for x in range(16)),
        'pwm': tuple(x for x in range(2, 14)),
        'use_ports': True,
        'disabled': (0, 1)  # Rx, Tx, Crystal
    },
    'arduino_due': {
        'digital': tuple(x for x in range(54)),
        'analog': tuple(x for x in range(12)),
        'pwm': tuple(x for x in range(2, 14)),
        'use_ports': True,
        'disabled': (0, 1)  # Rx, Tx, Crystal
    },
    'arduino_nano': {
        'digital': tuple(x for x in range(14)),
        'analog': tuple(x for x in range(8)),
        'pwm': (3, 5, 6, 9, 10, 11),
        'use_ports': True,
        'disabled': (0, 1)  # Rx, Tx, Crystal
    },
    'arduino_leonardo': {
        'digital': tuple(x for x in range(20)),
        'analog': tuple(x for x in range(12)),
        'pwm': (3, 5, 6, 9, 10, 11, 13),
        'use_ports': True,
        'disabled': (0, 1)  # Rx, Tx, Crystal
    },
    'arduino_pro_micro': {
        'digital': (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 15, 16),
        'analog': (0, 1, 2, 3, 6, 7, 8, 9),
        'pwm': (3, 5, 6, 9, 10),
        'use_ports': True,
        'disabled': (0, 1)  # Rx, Tx, Crystal
    },
    'arduino_pro_mini': {
        'digital': tuple(x for x in range(14)),
        'analog': tuple(x for x in range(5)),
        'pwm': (3, 5, 6, 9, 10, 11),
        'use_ports': True,
        'disabled': (0, 1)  # Rx, Tx, Crystal
    },
    'arduino_lilypad': {
        'digital': tuple(x for x in range(14)),
        'analog': tuple(x for x in range(5)),
        'pwm': (5, 6, 9, 10, 11),
        'use_ports': True,
        'disabled': (0, 1)  # Rx, Tx, Crystal
    }
}
