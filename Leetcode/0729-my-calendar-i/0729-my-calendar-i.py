class MyCalendar:

    def __init__(self):
        # List to store the booked events as (start, end) pairs
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        # Check if the new booking overlaps with any existing bookings
        for booked_start, booked_end in self.bookings:
            # If the current event overlaps with the new event, return False
            if not (end <= booked_start or start >= booked_end):
                return False
        
        # If no overlap, add the event to bookings and return True
        self.bookings.append((start, end))
        return True
