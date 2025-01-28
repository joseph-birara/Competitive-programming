class MyCalendarTwo:

    def __init__(self):
        self.bookings = []  # To store single bookings
        self.overlaps = []  # To store double bookings (overlaps between single bookings)

    def book(self, start: int, end: int) -> bool:
        # First, check if the new booking would cause a triple booking by comparing with double bookings
        for overlap_start, overlap_end in self.overlaps:
            if start < overlap_end and end > overlap_start:  # Check overlap with a double-booked interval
                return False  # A triple booking would occur, so return False
        
        # Now, update the double bookings list if this new event overlaps with any existing bookings
        for booking_start, booking_end in self.bookings:
            if start < booking_end and end > booking_start:  # Check overlap with single bookings
                # Add the overlap to the double bookings list
                overlap_start = max(start, booking_start)
                overlap_end = min(end, booking_end)
                self.overlaps.append((overlap_start, overlap_end))
        
        # Finally, add the new booking to the single bookings list
        self.bookings.append((start, end))
        return True
