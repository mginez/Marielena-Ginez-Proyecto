from Client import Ticket
prueba = Ticket(
    'Marielena',
    123456,
    17,
    48,
    'VIP',
    00,
    50
)

clients_db = []
clients_VIP_db = []
tickets = [prueba]
unused_qrcodes = []
used_qrcodes = []
matches_attendance = [] ###no se