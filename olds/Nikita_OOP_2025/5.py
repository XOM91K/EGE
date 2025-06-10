class Seat:
    def __init__(self):
        self.is_occupied = False


class Hall:
    def __init__(self, hall_number, rows, seats_per_row):
        self.hall_number = hall_number
        self.seats = [[Seat() for _ in range(seats_per_row)]
                      for _ in range(rows)]
        self.sessions = []

    def add_session(self, movie_name, duration, start_time):
        self.sessions.append(Session(movie_name, duration, start_time, self))

    def print_layout(self):
        for row in self.seats:
            row_layout = ''.join(['O' if not seat.is_occupied else 'X'
                                  for seat in row])
            print(row_layout)

    def has_free_seats(self):
        return any(seat.is_occupied is False for
                   row in self.seats for seat in row)


class Session:
    def __init__(self, movie_name, duration, start_time, hall):
        self.movie_name = movie_name
        self.duration = duration
        self.start_time = start_time
        self.hall = hall


class Cinema:
    def __init__(self):
        self.halls = {}

    def add_hall(self, hall_number, rows, seats_per_row):
        self.halls[hall_number] = Hall(hall_number, rows, seats_per_row)

    def find_next_session(self, movie_name):
        for hall in self.halls.values():
            for session in hall.sessions:
                if session.movie_name == movie_name and hall.has_free_seats():
                    return session
        return None

    def sell_ticket(self, session, row, seat_number):
        if session.hall.seats[row][seat_number].is_occupied:
            stn = seat_number + 1
            rw = row + 1
            print(f"Билет недоступен: место {stn} в ряду {rw} занято.")
            return False
        session.hall.seats[row][seat_number].is_occupied = True
        smn = session.movie_name
        sn1 = seat_number + 1
        rw = row + 1
        print(f"Билет куплен на '{smn}', ряд {rw}, место {sn1}.")
        return True


if __name__ == "__main__":
    cinema = Cinema()
    num_halls = int(input("Введите количество залов: "))
    for i in range(num_halls):
        hall_number = i + 1
        hn = hall_number
        rows = int(input(f"Введите количество рядов для зала {hn}: "))
        seats_per_row = int(input(f"Введите количество мест в ряду для зала {hn}: "))
        cinema.add_hall(hall_number, rows, seats_per_row)
    for hall_number in cinema.halls:
        hall = cinema.halls[hall_number]
        hn = hall_number
        num_sessions = int(input(f"Введите количество сеансов для зала {hn}: "))
        for j in range(num_sessions):
            hn = hall_number
            jj = j + 1
            movie_name = input(f"Введите название фильма для сеанса {jj} в зале {hn}: ")
            duration = int(input(f"Введите длительность фильма в мин: "))
            start_time = input(f"Введите время начала сеанса (например, 00:00): ")
            hall.add_session(movie_name, duration, start_time)
    movie_to_find = input("Введите желаемый фильм: ")
    session = cinema.find_next_session(movie_to_find)
    if session:
        sh_hn = session.hall.hall_number
        stt = session.start_time
        print(f"Ближайший сеанс в зале {sh_hn} в {stt}.")
        session.hall.print_layout()
        row = int(input("Введите номер ряда (с 1): ")) - 1
        seat_number = int(input("Введите номер места (с 1): ")) - 1
        cinema.sell_ticket(session, row, seat_number)
        session.hall.print_layout()
    else:
        print("Доступных мест не найдено")