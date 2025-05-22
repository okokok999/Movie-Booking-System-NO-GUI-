
# 🎬 Movie Ticket Booking System  

## 📄 Description

This project is a **console-based movie ticket booking system** written in Python. It simulates a real-world booking system where **Admins** can manage movie listings, and **Customers** can book or cancel tickets. The program is implemented using **Object-Oriented Programming (OOP)** principles and stores data persistently using text files (`users.txt`, `movies.txt`, `bookings.txt`).

---

## 🧠 Features

### 👤 Admin Functions
- Login via `users.txt`
- Add a new movie (`movies.txt`)
- View all listed movies with total, available, and booked seats

### 👥 Customer Functions
- Login via `users.txt`
- View available movies
- Book tickets (with seat availability check)
- Cancel booked tickets
- Show personal booking history

---

## 🏗️ Technologies Used

- **Python 3.10+**
- Object-Oriented Programming (OOP)
- File handling (`open()`, `readlines()`, `write()`, `append()`)
- Exception handling (`try/except`)
- Menu-based console interface

---

## 🗂️ File Structure

```
project/
│
├── movies_booking_system.py       # Main Python script
├── users.txt                      # Predefined user credentials (admin & customers)
├── movies.txt                     # Movie listings (created/updated dynamically)
├── bookings.txt                   # User bookings (created/updated dynamically)
├── README.md                      # This file
└── screenshots/                   # Screenshots for report and demonstration
```

---

## 📝 How to Run

1. Make sure Python 3 is installed on your system.
2. Place all files (`.py`, `.txt`) in the same folder.
3. Open terminal or IDE (like Spyder, VS Code).
4. Run:

   ```bash
   python movies_booking_system.py
   ```

5. Follow the on-screen menu prompts to log in and interact.

---

## 👨‍👩‍👧‍👦 User Credentials (Example in `users.txt`)

```
admin,admin123,admin
alice,pass123,customer
bob,pass456,customer
```

---

## 🧪 Testing & Demonstration

- Tested for both Admin and Customer roles.
- Includes error handling for:
  - Invalid login credentials
  - Overbooking attempts
  - Wrong menu options
  - File not found

Screenshots included in the `screenshots/` folder.

---

## 📋 Project Members (Optional)

| Role              | Responsibility                          |
|-------------------|------------------------------------------|
| Developer         | Code, login system, file handling        |
| Tester            | Flowchart, screenshots, test cases       |
| Reporter/Reviewer | Report writing, documentation            |

---

## 📚 References

Full reference list is provided in the project report under **Section 8** in APA 7 format.
