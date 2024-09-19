<h1 style="font-size: 36px;">Portfolio Project:</h1>

This project is a personal portfolio web application built with Flask and Docker. It showcases your skills, projects, and allows visitors to contact you. The application integrates with PostgreSQL as the database for storing contact form submissions and is deployed with a continuous integration/continuous deployment (CI/CD) pipeline using GitHub Actions.

Features:
- Portfolio showcase: Display your personal information, skills, and projects.
- Contact form: Allow users to contact you via a form, which submits data to a backend API.
- Dockerized: The application is containerized using Docker for easy setup and deployment.
- PostgreSQL integration: Contact form submissions are stored in a PostgreSQL database.
- CI/CD pipeline: Automated testing and deployment using GitHub Actions.

Tech Stack:
- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript (for portfolio and contact form)
- Database: PostgreSQL
- Containerization: Docker, Docker Compose
- CI/CD: GitHub Actions for automated testing and deployment
- Testing: Curl tests for API endpoints

Prerequisites:
To run this project locally, you will need the following tools:
- Docker: Install Docker.
- Docker Compose: Make sure Docker Compose is also installed.
- Git: For cloning the repository.

Installation:
1) Clone this repository.
  git clone https://github.com/your-username/portfolio_project.git

2) Set up the environment variables: Create a .env file in the root directory with the following variables (update them according to your environment):

POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_database_name

Running Locally:
1) Build and run the Docker containers:
docker-compose up --build
2) Visit the application at http://localhost:5000. The application should now be running, and you can explore the portfolio and test the contact form functionality.

CI/CD Pipeline
This project uses GitHub Actions to automate the following CI/CD tasks:

Build and Test: 
On every push to the main branch, the Docker images are built and tested.

Automated Deployment: 
After testing, the application can be deployed automatically to your server.

CI/CD Pipeline Flow:
- Trigger: The pipeline is triggered on a push to the main branch.
- Docker Build: The Docker images for the app and PostgreSQL are built.
- API Testing: A test POST request is sent to the running Flask app to verify the API functionality.
- Automated Deployment: After successful tests, the deployment can be configured to push the image to a Docker registry or deploy to a live server.

Contributing:
Contributions are welcome! If you'd like to improve this project:
1) Fork the repository.
2) Create a new branch: git checkout -b feature/your-feature-name.
3) Make your changes and commit them: git commit -m 'new feature'.
4) Push to your branch: git push origin feature/your-feature-name.
5) Open a pull request.
