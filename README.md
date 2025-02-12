# Railway-Reservation-System-Django

## Description
This railway project is a web application that allows users to manage train schedules, book tickets, and handle user authentication. It provides functionalities for both users and administrators to interact with the railway system efficiently.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd railway
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Access the application at `http://127.0.0.1:8000/`.
- Users can register, log in, and book tickets.
- Administrators can manage trains, schedules, and view bookings.

## Features
- User registration and authentication
- Ticket booking system
- Train schedule management
- Admin dashboard for managing trains and stations

## Models
- **Station**: Represents a train station with fields for name and location.
- **Train**: Represents a train with fields for name, source, destination, and number of seats.
- **Schedule**: Represents the schedule of a train with arrival and departure times.
- **Admin**: Represents an administrator with fields for username, email, and password.
- **Ticket**: Represents a booked ticket with fields for train, passenger name, and seat number.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.

