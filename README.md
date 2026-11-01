# Student Result Prediction - Practical 7

## Objective

Automate Docker image creation, container startup, health verification,
and prediction API testing using GitHub Actions.

## Application

The application predicts whether a student will PASS or FAIL based on:

- Attendance
- Internal marks
- Assignment marks
- Previous score

## CI/CD Pipeline

The GitHub Actions workflow performs:

1. Checkout repository
2. Set up Python
3. Install dependencies
4. Train the ML model
5. Check the ML quality gate
6. Run automated tests
7. Build Docker image
8. Start Docker container
9. Verify the `/health` endpoint
10. Test the `/predict` endpoint
11. Display container logs
12. Stop and remove the container

## Docker

The application runs on:

- Host port: 5000
- Container port: 5000

## Practical 7 Outcome

The Dockerized ML application is automatically built and tested
inside a GitHub Actions runner.
