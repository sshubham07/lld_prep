def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return datetime.now()

if __name__ == "__main__":
    print("=====================================================")
    print("MOVIE TICKET BOOKING SYSTEM - SCENARIO DEMONSTRATION")
    print("=====================================================")

    # Setup
    city = City("Seattle", "WA", 98101, [])
    cinema = Cinema(1, [], city)
    city.cinemas.append(cinema)

    hall = Hall(101, [])
    cinema.halls.append(hall)

    inception = Movie("Inception", "Sci-Fi", parse_date("2010-07-16"), "English", 148, [])
    interstellar = Movie("Interstellar", "Sci-Fi", parse_date("2014-11-07"), "English", 169, [])

    seats_show1 = [Platinum(), Gold(), Silver()]
    for i, seat in enumerate(seats_show1):
        seat.seat_no = f"A{i+1}"
        seat.status = SeatStatus.AVAILABLE
        seat.set_rate()

    show1 = ShowTime(1001, datetime.now(), datetime.now(), 150, seats_show1)
    hall.shows.append(show1)
    inception.shows.append(show1)

    catalog = Catalog()
    catalog.movie_titles["Inception"] = [inception]
    catalog.movie_titles["Interstellar"] = [interstellar]

    admin = Admin()
    admin.name = "Bob (Admin)"
    admin.email = "bob.admin@cinema.com"

    customer = Customer()
    customer.name = "Alice (Customer)"
    customer.email = "alice@example.com"

    agent = TicketAgent()
    agent.name = "Eve (Ticket Agent)"
    agent.email = "eve.agent@cinema.com"

    # Scenario 1
    print("\n----- SCENARIO 1: Customer Searches For A Movie -----")
    print(f"{customer.name} is searching for the movie 'Inception':")
    found = catalog.search_movie_title("Inception")
    for m in found:
        print(f"  - Found: {m.title} ({m.genre}, Released: {m.release_date.strftime('%Y-%m-%d')})")

    # Scenario 2
    print("\n----- SCENARIO 2: Customer Books A Ticket -----")
    chosen_seat = show1.seats[0]
    if chosen_seat.is_available():
        chosen_seat.status = SeatStatus.BOOKED

        ticket = MovieTicket(2001, chosen_seat, inception, show1)
        tickets = [ticket]

        payment = CreditCard()
        payment.amount = 15.0
        payment.name_on_card = customer.name
        payment.card_number = "1234-5678-9012-3456"
        payment.billing_address = "123 1st Ave, Seattle, WA"
        payment.code = 123
        payment.status = PaymentStatus.PENDING
        payment.timestamp = datetime.now()
        payment.make_payment()
        payment.status = PaymentStatus.CONFIRMED

        booking = Booking(3001, 15, 1, datetime.now(), BookingStatus.CONFIRMED,
                          payment, tickets, [chosen_seat])
        customer.bookings.append(booking)

        notification = EmailNotification()
        notification.content = f"Booking confirmed for {inception.title}!\nSeat: {chosen_seat.seat_no} ({type(chosen_seat).__name__})\nShow ID: {show1.show_id}"
        notification.send_notification(customer)

        print(f"{customer.name} successfully booked a ticket for: {inception.title}")
        print(f"  - Seat: {chosen_seat.seat_no} ({type(chosen_seat).__name__}), Show ID: {show1.show_id}")
        print(f"  - Payment: ${payment.amount:.2f} by Credit Card ending {payment.card_number[-4:]}")
    else:
        print("Seat is not available!")

    # Scenario 3
    print("\n----- SCENARIO 3: Admin Adds A New Show -----")
    new_show = ShowTime(1002, datetime.now(), datetime.now(), 148, [])
    if admin.add_show(new_show):
        hall.shows.append(new_show)
        inception.shows.append(new_show)
        print(f"{admin.name} added a new show for: {inception.title} (Show ID: {new_show.show_id})")

    # Scenario 4
    print("\n----- SCENARIO 4: Ticket Agent Creates A Walk-In Booking -----")
    show_interstellar = ShowTime(1003, datetime.now(), datetime.now(), 169, [])
    hall.shows.append(show_interstellar)
    interstellar.shows.append(show_interstellar)

    seats_show2 = [Gold(), Silver()]
    for i, seat in enumerate(seats_show2):
        seat.seat_no = f"B{i+1}"
        seat.status = SeatStatus.AVAILABLE
        seat.set_rate()
    show_interstellar.seats = seats_show2

    walk_in_seat = show_interstellar.seats[1]
    if walk_in_seat.is_available():
        walk_in_seat.status = SeatStatus.BOOKED

        ticket = MovieTicket(2002, walk_in_seat, interstellar, show_interstellar)
        tickets = [ticket]

        cash_payment = Cash()
        cash_payment.amount = 10.0
        cash_payment.status = PaymentStatus.PENDING
        cash_payment.timestamp = datetime.now()
        cash_payment.make_payment()
        cash_payment.status = PaymentStatus.CONFIRMED

        agent_booking = Booking(3002, 10, 1, datetime.now(), BookingStatus.CONFIRMED,
                                cash_payment, tickets, [walk_in_seat])
        if agent.create_booking(agent_booking):
            print(f"{agent.name} booked ticket for: {interstellar.title} (walk-in)")
            print(f"  - Seat: {walk_in_seat.seat_no} ({type(walk_in_seat).__name__}), Show ID: {show_interstellar.show_id}")
            print(f"  - Payment: ${cash_payment.amount:.2f} by Cash")

    # Scenario 5
    print("\n----- SCENARIO 5: Admin Deletes A Movie -----")
    if admin.delete_movie(interstellar):
        if "Interstellar" in catalog.movie_titles:
            del catalog.movie_titles["Interstellar"]
        print(f"{admin.name} deleted movie: {interstellar.title}")

    print("\n=====================================================")
    print("       END OF MOVIE TICKET BOOKING DEMO RUN")
    print("=====================================================")
