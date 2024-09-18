class location :
    def __init__(self) :
        self.street = 0
        self.apartment= 0

work = location()
work.street = "1 Park Place"
work.apartment = "Room 724"

print (f'The work place can be found at {work.street} in {work.apartment}. ')