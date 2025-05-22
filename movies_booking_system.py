# -*- coding: utf-8 -*-
"""
Movie Ticket Booking System - Password First, Role Second
"""

# --- Class Definitions ---

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.role = None

    def validate_username_password(self):
        try:
            with open('users.txt', 'r') as file:
                users = file.readlines()
                for user in users:
                    u, p, r = user.strip().split(',')
                    if self.username == u:
                        if self.password == p:
                            self.role = r  # Temporarily store correct role
                            return True
                        else:
                            print("❌ Incorrect password.")
                            return False
        except FileNotFoundError:
            print("❌ users.txt file not found.")
        print("❌ Username not found.")
        return False

    def validate_role(self, input_role):
        if self.role == input_role:
            return True
        else:
            print("❌ Incorrect role.")
            return False


# --- Helper to Count Booked Seats ---

def get_booked_seats(movie_title):
    booked = 0
    try:
        with open('bookings.txt', 'r') as file:
            for line in file:
                _, title, seats = line.strip().split(',')
                if title.lower() == movie_title.lower():
                    booked += int(seats)
    except FileNotFoundError:
        pass
    return booked


# --- Movie Functions ---

def view_movies():
    print("\n--- Available Movies ---")
    try:
        with open('movies.txt', 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No movies found.")
            else:
                for line in lines:
                    title, genre, time, seats = line.strip().split(',')
                    seats = int(seats)
                    booked = get_booked_seats(title)
                    total = seats + booked
                    print(f"{title} | {genre} | {time} | Total Seats: {total} | Booked: {booked} | Available: {seats}")
    except FileNotFoundError:
        print("❌ movies.txt not found.")


def add_movie():
    print("\n--- Add a New Movie ---")
    title = input("Movie title: ")
    genre = input("Genre: ")
    showtime = input("Showtime: ")
    seats = input("Number of seats: ")

    try:
        seats = int(seats)
        with open('movies.txt', 'a') as file:
            file.write(f"{title},{genre},{showtime},{seats}\n")
        print("✅ Movie added.")
    except ValueError:
        print("❌ Seats must be a number.")


# --- Booking Functions ---

def book_ticket(username):
    while True:
        view_movies()
        movie_title = input("\nEnter movie title to book (or type 'exit' to go back): ")
        if movie_title.lower() == 'exit':
            break
        try:
            seats_to_book = int(input("Enter number of seats: "))
        except ValueError:
            print("❌ Enter a valid number.")
            continue

        updated_movies = []
        booked = False

        try:
            with open('movies.txt', 'r') as file:
                lines = file.readlines()

            for line in lines:
                title, genre, time, seats = line.strip().split(',')
                if title.lower() == movie_title.lower():
                    if seats_to_book <= int(seats):
                        new_seats = int(seats) - seats_to_book
                        updated_movies.append(f"{title},{genre},{time},{new_seats}\n")
                        with open('bookings.txt', 'a') as bfile:
                            bfile.write(f"{username},{title},{seats_to_book}\n")
                        booked = True
                    else:
                        print("❌ Not enough seats.")
                        break
                else:
                    updated_movies.append(line)

            if booked:
                with open('movies.txt', 'w') as file:
                    file.writelines(updated_movies)
                print("✅ Booking successful.")
                break
            else:
                print("❌ Movie not found. Try again.")
        except FileNotFoundError:
            print("❌ movies.txt not found.")
            break


def cancel_booking(username):
    while True:
        print("\n--- Cancel Booking ---")
        try:
            with open('bookings.txt', 'r') as file:
                bookings = file.readlines()
        except FileNotFoundError:
            print("❌ bookings.txt not found.")
            return

        user_bookings = [b for b in bookings if b.startswith(username + ',')]
        if not user_bookings:
            print("No bookings found.")
            return

        print("Your Bookings:")
        for i, booking in enumerate(user_bookings, 1):
            print(f"{i}. {booking.strip()}")

        choice = input("Enter booking number to cancel (or 'exit' to go back): ")
        if choice.lower() == 'exit':
            break

        try:
            choice = int(choice)
            if choice < 1 or choice > len(user_bookings):
                print("❌ Invalid choice. Try again.")
                continue
        except ValueError:
            print("❌ Enter a valid number.")
            continue

        booking_to_cancel = user_bookings[choice - 1]
        _, movie_title, seats_booked = booking_to_cancel.strip().split(',')
        seats_booked = int(seats_booked)

        updated_movies = []
        try:
            with open('movies.txt', 'r') as file:
                movies = file.readlines()

            for line in movies:
                title, genre, time, seats = line.strip().split(',')
                if title.lower() == movie_title.lower():
                    new_seats = int(seats) + seats_booked
                    updated_movies.append(f"{title},{genre},{time},{new_seats}\n")
                else:
                    updated_movies.append(line)

            with open('movies.txt', 'w') as file:
                file.writelines(updated_movies)
        except FileNotFoundError:
            print("❌ movies.txt not found.")
            return

        bookings.remove(booking_to_cancel)
        with open('bookings.txt', 'w') as file:
            file.writelines(bookings)

        print("✅ Booking cancelled and seat restored.")
        break


def show_my_bookings(username):
    print("\n--- My Booked Tickets ---")
    try:
        with open('bookings.txt', 'r') as file:
            lines = file.readlines()
            user_bookings = [line.strip() for line in lines if line.startswith(username + ',')]

            if not user_bookings:
                print("You have no bookings.")
            else:
                for booking in user_bookings:
                    _, movie, seats = booking.split(',')
                    print(f"Movie: {movie} | Seats Booked: {seats}")
    except FileNotFoundError:
        print("❌ bookings.txt not found.")


# --- Menus ---

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            add_movie()
        elif choice == '2':
            view_movies()
        elif choice == '3':
            print("Logging out...\n")
            break
        else:
            print("Invalid option. Try again.")


def customer_menu(username):
    while True:
        print(f"\n--- Customer Menu ({username}) ---")
        print("1. View All Movies")
        print("2. Book Ticket")
        print("3. Cancel Booking")
        print("4. Show My Bookings")
        print("5. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            view_movies()
        elif choice == '2':
            book_ticket(username)
        elif choice == '3':
            cancel_booking(username)
        elif choice == '4':
            show_my_bookings(username)
        elif choice == '5':
            print("Logging out...\n")
            break
        else:
            print("Invalid option. Try again.")


# --- Login + Main Menu ---

def login_user():
    print("\n=== Login ===")
    username = input("Username: ")
    password = input("Password: ")
    user = User(username, password)

    if user.validate_username_password():
        while True:
            role = input("Role (admin/customer): ").lower()
            if role not in ['admin', 'customer']:
                print("❌ Invalid role. Please enter 'admin' or 'customer'.")
            else:
                if user.validate_role(role):
                    print(f"\n✅ Welcome {username}!")
                    if role == 'admin':
                        admin_menu()
                    else:
                        customer_menu(username)
                break
    else:
        print("❌ Login failed. Try again.\n")


def show_main_menu():
    while True:
        print("\n=== Movie Ticket Booking System ===")
        print("1. Login")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ")

        if choice == '1':
            login_user()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# --- Run Program ---
if __name__ == "__main__":
    show_main_menu()
