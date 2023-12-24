# Car Rental System

Welcome to the Car Rental System project! This Django-based web application allows users to rent cars, manage bookings, and leave reviews.

## Table of Contents

- [Authors](#authors)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [API Documentation](#api-documentation)

## Authors

- **Abdi Berhe**
  - GitHub: [abdi-bb](https://github.com/abdi-bb)
  - LinkedIn: [Abdi Berhe on LinkedIn](https://www.linkedin.com/in/abdi-berhe)

- **Addis Simegn**
  - GitHub: [Addika1630](https://github.com/Addika1630/)
  - LinkedIn: [Addis Simegn on LinkedIn](https://www.linkedin.com/in/your-linkedin-profile/)

- **Daniel Tsega**
  - GitHub: [DannySanchez6658](https://github.com/DannySanchez6658/)
  - LinkedIn: [Daniel Tsega on LinkedIn](https://www.linkedin.com/in/your-linkedin-profile/)

- **Abrhaley**
  - GitHub: [Abrsh7](https://github.com/Abrsh7/)
  - LinkedIn: [Abrhaley on LinkedIn](https://www.linkedin.com/in/your-linkedin-profile/)

Feel free to reach out to the authors for any questions or contributions related to the project.

Happy renting! 🚗

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Other dependencies (specified in requirements.txt)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abdi-bb/car-rental-system.git
   cd car-rental-system
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv carvenv
   source carvenv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at `http://localhost:8000/`.

## Usage

Describe how to use your application. Include information about user authentication, renting a car, managing bookings, leaving reviews, etc.

## Features

List key features of your car rental system.

- User authentication
- Car renting and booking management
- Review system
- ...

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bugfix: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Description of your changes'`
4. Push to your branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or issues, please contact the project maintainers:

- Abdi Berhe: [abdiberhe@gmail.com](mailto:abdiberhe@gmail.com)
- Addis Simegn: [addis@email.com](mailto:addis@email.com)
- Daniel Tsega: [daniel@email.com](mailto:daniel@email.com)
- Abrhaley: [abrhaley@email.com](mailto:abrhaley@email.com)

## API Documentation

Welcome to the API documentation for the Car Rental System. This API provides endpoints for managing users, customer profiles, cars, reviews, and bookings.


**Base URL:** `http://127.0.0.1:8000/api/`

## Authentication

To interact with the API, you'll need to authenticate using JSON Web Tokens (JWT). Follow the steps below to get started.

### 1. User Management

#### Get/Create User
- **Endpoint:** `auth/users/`
- **Method:** `GET` (retrieve user list) / `POST` (create user)
- **Fields for Create:**
  - `id`: (auto-generated)
  - `username`: (string)
  - `password`: (string)
  - `email`: (string)
  - `first_name`: (string)
  - `last_name`: (string)

#### Retrieve User
- **Endpoint:** `auth/users/{user_id}/`
- **Method:** `GET`
- **Fields:**
  - `id`
  - `username`
  - `email`
  - `first_name`
  - `last_name`

### 2. Obtain JWT Token

To access protected endpoints, obtain a JWT token.

- **Endpoint:** `auth/jwt/create/`
- **Method:** `POST`
- **Request Body:**
  - `username`: (string)
  - `password`: (string)
- **Usage:** Add the obtained token to the `Authorization` header in your requests.

### 3. Customer Profile

#### Create Customer Profile
- **Endpoint:** `rental/customers/`
- **Method:** `POST`
- **Authorization Header:** `Bearer {your_token}`
- **Request Body:**
  - `user_id`: (integer) - ID of the user for whom the profile is created.

#### View/Update Current User Profile
- **Endpoint:** `rental/customers/me/`
- **Method:** `GET` (retrieve) / `PUT` (update)
- **Authorization Header:** `Bearer {your_token}`

### 4. Cars

#### View Cars List
- **Endpoint:** `rental/cars/`
- **Method:** `GET`
- **Authorization Header:** `Bearer {your_token}`
- **Note:** Admin users have all permissions.

### 5. Car Reviews

#### View/Create Car Reviews
- **Endpoint:** `rental/cars/{car_id}/reviews/`
- **Method:** `GET` (retrieve reviews) / `POST` (create review)
- **Authorization Header:** `Bearer {your_token}`
- **Note:** Use nested-loop to view and create reviews for a specific car.

### 6. Bookings

#### View Your Own Bookings
- **Endpoint:** `rental/bookings/`
- **Method:** `GET`
- **Authorization Header:** `Bearer {your_token}`
- **Note:** Authenticated users have all permissions.

## Libraries Used

This API is built on top of Django and includes the following key libraries:

- Django REST framework
- Djoser
- Other necessary dependencies specified in `requirements.txt`

Feel free to reach out if you have any questions or need further clarification.

Happy developing! 🚀