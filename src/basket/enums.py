from enum import Enum
class BasketStatus(Enum):
    OPEN = 'Open'
    CLOSED = 'Closed'
    CANCELLED = 'Cancelled'

class OrderStatus(Enum):
    Open = 'Open'
    Paid = 'Paid'
    Sent = 'Sent'
    Received = 'Received'
    Cancelled = 'Cancelled'
    Returned = 'Returned'