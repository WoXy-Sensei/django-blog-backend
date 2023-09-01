# Django Blog API


Welcome to the Django Blog API, a blog infrastructure developed using Django REST framework. Below, you'll find an overview of the project's features and instructions on how to get started.

## Features

1. **Adding Comments with Recaptcha**: Ensure a spam-free commenting experience by using Recaptcha when posting comments.

2. **User Registration**: Users can register for the platform. During registration, users are required to provide their age information.

3. **User Age Verification**: User ages are validated to fall within specified age limits, which can be configured in the project settings.

4. **User Authentication**: Registered users can log in to the platform using either session-based authentication or Auth Token provided by Django REST framework.

5. **Profile Management**: Users can view, edit, and update their profile information.

6. **Comment Replies**: Encourage interaction and discussions by allowing replies to comments.

7. **Category and Tag Management**: Organize blog posts by categorizing them and adding tags.

8. **View Posts by Category**: Filter and view posts within specific categories.

9. **View User-Specific Posts**: Implement an authorization system to enable users to view their own posts.

## Installation

To run the project in your local environment, follow these steps:

1. Clone this repository: ```git clone https://github.com/WoXy-Sensei/django-blog-backend```

2. Navigate to the project folder: ```cd blog```


3. Create and activate a virtual environment:

- Linux or macOS:
  ```
  python -m venv venv
  source venv/bin/activate
  ```

- Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```

4. Install required dependencies: ```pip install -r requirements.txt```

5. Create the database: ```python manage.py migrate```

6. Create a superuser account: ```python manage.py createsuperuser```

7. Start the project: ```python manage.py runserver```

8. Access the admin panel by visiting `http://localhost:8000/admin/` in your browser and logging in with the superuser account.

## Contribution

This project is currently in development and open to contributions. If you would like to contribute, add new features, or fix issues, please visit the [GitHub repository](https://github.com/WoXy-Sensei/django-blog-backend) and open an issue or submit a pull request.

## Future Development and API Documentation

Please note that this project is actively evolving. We plan to enhance it further and provide comprehensive API documentation in the near future.

## License

This project is licensed under the [MIT License](LICENSE).
