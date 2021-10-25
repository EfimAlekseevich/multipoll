# Bytes order
# 2 bytes
b01 = 0, 1
b10 = 1, 0

# 4 bytes
b0123 = 0, 1, 2, 3
b1032 = 1, 0, 3, 2

# Default values
LOCALHOST = 'localhost'
MODBUS_TCP_PORT = 502
TRANSACTION_ID = int('1010101010101010', 2)

# Status
status = {
    'channel': [
        'Not checked',
        'No connection',
        'Lags',
        'Good',
    ],
    'tag': [
        'Not checked',
        'No connection',
        'Not available',
        'Not readable',
        'Not writable',
        'Good',
    ],
    'device': [
        'Not checked',
        'No connection',
        'Lags',
        'Good',

    ]
}
