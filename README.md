<h1 align="center">🏨 Hotel Management (Python)</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue">
  <img src="https://img.shields.io/badge/Status-Work_in_Progress-orange">
  <img src="https://img.shields.io/badge/Improvements-Planned-yellow">
  <img src="https://img.shields.io/badge/Project-Learning-brightgreen">
  <img src="https://img.shields.io/badge/project-academic-informational">
  <img src="https://img.shields.io/badge/Architecture-Modular-blueviolet">
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg">
  </a>
</p>

This project is a simple **hotel management system**, developed in **Python**, with a strong focus on **Object-Oriented Programming (OOP)** and solving real-world problems.

The goal is to simulate the basic operation of a hotel, allowing the management of rooms and reservations, and user interaction through a terminal-based menu.

---

## 🎯 Features

* Create and manage rooms
* Display all rooms
* Display available rooms
* Make reservations
* List existing reservations
* Simple text-based interface (terminal)
* Modular and scalable structure
* Prepared for unit testing

---

## 🧱 Project Structure

```text
hotel/
│
├── model/                  # Model layer (Object-Oriented Programming)
│   ├── __init__.py
│   ├── hotel.py            # Hotel class (main management class)
│   ├── quarto.py           # Room class
│   ├── reserva.py          # Reservation class
│   └── estado_quarto.py    # Enum defining room states
│
├── interface/              # Interface layer (menus and user interaction)
│   ├── __init__.py
│   ├── menu.py             # Main menu logic
│   ├── reservas.py         # Reservation-related menus
│   └── quartos.py          # Room-related menus
│
├── utils/                  # Utility/helper functions
│   ├── __init__.py
│   ├── limpar_tela.py      # Clear terminal screen
│   └── aguardar.py         # Pause/wait for user input
│
├── tests/                  # Unit tests
│   ├── __init__.py
│   └── test_hotel.py       # Tests for the Hotel class
│
├── main.py                 # Program entry point
├── obj.py                  # Initial object creation (hotel, rooms, reservations)
├── README.md
```

---

## 🧠 Concepts Used

* Object-Oriented Programming (OOP)
* Separation of responsibilities
* Code modularization
* Enumerations (`Enum`)
* Unit testing (`unittest`)
* Good project organization practices

---

## ▶️ How to Run the Program

1. Make sure you have **Python 3.10+** installed
2. Open a terminal in the project folder
3. Run the following command:

```bash
python main.py
```

---

## 🧪 Unit Tests

The project includes unit tests to validate the behavior of the main classes.

To run all tests:

```bash
python -m unittest
```

Or a specific test file:

```bash
python -m unittest tests/test_hotel.py
```

---

## 🚀 Possible Future Improvements

* Add a `Client` class
* Real date validation (using `datetime`)
* Reservation cancellation
* Data persistence (files or database)
* Graphical or web interface
* Reports (occupancy, reservation history)

---

## 👤 Author

Project developed as part of the professional course  
**Management and Programming of Information Systems (GPSI)**

**School:** Escola Profissional Bento Jesus Caraça (EPBJC)  
**Subject:** PSI  
**Author:** Andérson Brito  

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
