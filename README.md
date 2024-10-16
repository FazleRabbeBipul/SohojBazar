# SohojBazar

SohojBazar is an online marketplace application designed to facilitate conversations between buyers and sellers, with a dashboard for product management, item deletion, and live chat functionality. The project is built using Django and includes an admin dashboard for managing items and user interactions.

## Demo

Watch the demo video of **SohojBazar** to see it in action:

[![Watch the video](https://img.youtube.com/vi/Lqe1lmNUMo0/0.jpg)](https://www.youtube.com/watch?v=Lqe1lmNUMo0)

> _Click the image to watch the video!_

Alternatively, you can download the demo video directly [here](https://youtu.be/Lqe1lmNUMo0).

## Features

- **Live Conversation**: Real-time chat between buyers and sellers.
- **Product Management**: Admins can add, edit, and delete products.
- **Inbox Page**: Seamless messaging interface for buyers and sellers.
- **Dashboard**: Comprehensive dashboard to view and manage product listings.
- **Admin Panel**: Manage products, users, and view conversations.

## Project Structure

```bash
SohojBazar/
├── conversation/            # Chat and conversation related code
├── core/                    # Core application files
├── dashboard/               # Admin dashboard functionality
├── item/                    # Item management logic
├── media/item_images/       # Images for products
├── db.sqlite3               # SQLite database
├── manage.py                # Django management file
├── requirments.txt          # Project dependencies
└── Instruction.txt          # Setup instructions
```
## Setup Instructions

### Prerequisites

Ensure you have the following installed on your machine:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Django**: Install using `pip install django`

### Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/FazleRabbeBipul/SohojBazar.git
    cd SohojBazar
    ```

2. Install dependencies from **requirments.txt**:
    ```bash
    pip install -r requirments.txt
    ```

3. Run the Django migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

4. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

5. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

6. Access the application by navigating to `http://127.0.0.1:8000/` in your browser.

## Usage

- **Log in** to the admin panel using the superuser account to manage products and users.
- **Buyers and sellers** can communicate through the live chat feature.
- **Admins** can manage the product inventory and delete items via the dashboard.
