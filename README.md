# OnlineElectronicStore
Django~=4.2.11
# Introduction
This is a Django-based online electronic store project. It allows users to browse electronic products, add them to their cart, and make purchases.

#Requirements
- Python 3.11
- Django~=4.2.11
- python -m pip install pillow | Pillow package (for image processing)


# Installation
1. Clone the repository:
    ```
    git clone https://github.com/rajuhchaudhary/online-electronic-store.git
    ```
2. Navigate to the project directory:
    ```
    cd online-electronic-store
    ```
3. Install Python 3.11 if not already installed.
4. Install required packages using pip:
    ```
    pip install -r requirements.txt
    ```
5. Apply database migrations:
    ```
    python manage.py migrate
    ```
6. Create a superuser to access the Django admin panel:
    ```
    python manage.py createsuperuser
    ```
7. Start the development server:
    ```
    python manage.py runserver
    ```
8. Access the application at http://localhost:8000/ in your web browser.
