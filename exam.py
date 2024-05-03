class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


if __name__ == "__main__":
    hall1 = Hall("Hall 1", 100)
    hall2 = Hall("Hall 2", 150)

    cinema = Star_Cinema()
    cinema.entry_hall(hall1)
    cinema.entry_hall(hall2)

    print(cinema.hall_list)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []  
        self.rows = rows
        self.cols = cols  
        self.hall_no = hall_no
class Star_Cinema:
    hall_list = []

    def __init__(self):
        pass

    @classmethod
    def add_hall(cls, hall):
        cls.hall_list.append(hall)


hall1 = Hall(rows=10, cols=10, hall_no=1)
Star_Cinema.add_hall(hall1)



class Hall:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.show_list = []
        self.seats = {}

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)
        
        
        allocated_seats = [['O' for _ in range(self.cols)] for _ in range(self.rows)]
        
        self.seats[show_id] = allocated_seats

    def display_seats(self, show_id):
        if show_id in self.seats:
            seats = self.seats[show_id]
            for row in seats:
                print(' '.join(row))
        else:
            print("Show ID not found")


hall = Hall(rows=5, cols=10)
hall.entry_show('1', 'Avengers: Endgame', '12:00 PM')


hall.display_seats('1')


class Hall:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.seats = [[0] * cols for _ in range(rows)]  # 0 represents available seats

    def book_seats(self, show_id, seat_list):
        if show_id == self.get_show_id():
            for row, col in seat_list:
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    if self.seats[row][col] == 0:
                        self.seats[row][col] = 1  # Book the seat
                        print(f"Seat ({row}, {col}) booked successfully.")
                    else:
                        print(f"Seat ({row}, {col}) is already booked.")
                else:
                    print(f"Seat ({row}, {col}) is invalid.")
        else:
            print("Invalid show ID.")

    def get_show_id(self):
                return "12345"



hall = Hall(5, 5)
seat_list = [(0, 0), (1, 1), (2, 2)]
hall.book_seats("12345", seat_list)


class Show:
    def __init__(self, name, time):
        self.name = name
        self.time = time

class Hall:
    def __init__(self, name):
        self.name = name
        self.shows = []

    def add_show(self, show):
        self.shows.append(show)

    def view_show_list(self):
        if not self.shows:
            print("No shows running currently.")
        else:
            print(f"Shows running in {self.name}:")
            for show in self.shows:
                print(f"{show.name} - Time: {show.time}")

hall = Hall("Main Hall")

show1 = Show("Magic Show", "6:00 PM")
show2 = Show("Comedy Show", "8:00 PM")
show3 = Show("Concert", "10:00 PM")

hall.add_show(show1)
hall.add_show(show2)
hall.add_show(show3)

hall.view_show_list()


class Hall:
    def __init__(self, hall_id, capacity):
        self.hall_id = hall_id
        self.capacity = capacity
        self.shows = {}

    def add_show(self, show_id, seats):
        self.shows[show_id] = seats

    def view_available_seats(self, show_id):
        if show_id not in self.shows:
            print("Show ID not found.")
            return

        print(f"Available seats for show {show_id}:")
        seats = self.shows[show_id]
        for row, seat_row in enumerate(seats, start=1):
            for seat, is_available in enumerate(seat_row, start=1):
                if is_available:
                    print(f"Row {row}, Seat {seat}")


hall = Hall("Hall A", capacity=50)


hall.add_show("Show1", [[True, True, False, True],
                        [True, False, False, True],
                        [True, True, True, False]])


hall.view_available_seats("Show1")



