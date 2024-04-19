import random
import string
from datetime import datetime

def generate_event_ticket_code(event_name, event_date, length=8):
    # Remove spaces and convert event name to uppercase
    event_name = event_name.replace(" ", "").upper()
    # Extract year and month from event date
    year = str(event_date.year)[-2:]
    month = str(event_date.month).zfill(2)
    # Generate unique identifier
    unique_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    # Combine all components to form ticket code
    ticket_code = f"{event_name[:3]}{year}{month}{unique_id}"
    return ticket_code

# Example usage
event_name = "Python Conference"
event_date = datetime(2024, 5, 15)  # Example date
ticket_code = generate_event_ticket_code(event_name, event_date)
print("Generated ticket code:", ticket_code)
