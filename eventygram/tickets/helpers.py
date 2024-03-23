from eventygram.tickets.models import Ticket
import uuid


def generate_unique_number():
    while True:
        generated_number = uuid.uuid4().hex[:10].upper()
        if not Ticket.objects.filter(number=generated_number).exists():
            return generated_number
