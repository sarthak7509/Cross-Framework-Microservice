# Movie Recommendation Microservice Project

This project demonstrates the integration of two isolated services developed using Django and Java Spring Boot. The Django service handles the logical functions of a basic movie recommendation system, while the Spring Boot service acts as an end-user microservice that interacts with the user and communicates with the Django service to provide recommendations. The services are connected internally using Eureka Discovery Client.

## Project Structure

- **Discovery**: Contains the Eureka Discovery Client for service registration and discovery.
- **Recommendation Service**: A Django-based microservice that provides movie recommendations.
- **User Service**: A Spring Boot-based microservice that interacts with the end user.

## API Endpoints

### Recommendation Service (Django)

1. **Get List of Movies**
   - **Endpoint**: `GET /movies`
   - **URL**: `http://localhost:8060/movies`
   - **Description**: Returns a list of available movies.

2. **Get Movie Recommendations**
   - **Endpoint**: `POST /movies`
   - **URL**: `http://localhost:8060/movies`
   - **Request Body**:
     ```json
     {
       "title": "movie name"
     }
     ```
   - **Response**: 
     ```json
     [
       "Top 5 recommendations for the given movie"
     ]
     ```

## Running the Project

To run the project, follow these steps:

### 1. Run Eureka Discovery Client

```sh
cd Discovery/Discovery/
mvnw.cmd spring-boot:run
```

### 2. Run Python Microservice (Recommendation Service)

```sh
pip install -r requirements.txt
cd RecommendationService
python manage.py runserver 0.0.0.0:8000
```

### 3. Run End User Service (Spring Boot)

```sh
cd UserService/UserService
mvnw.cmd spring-boot:run
```

## Prerequisites

- **Java 11** or later
- **Python 3.8** or later
- **Maven**
- **pip**

## Installation

Ensure you have the required dependencies installed. Follow the instructions to run the Discovery, Recommendation Service, and User Service in their respective directories.

## Conclusion

This project illustrates the implementation of a microservice architecture using Django and Spring Boot, connected through Eureka Discovery Client. The Django service handles movie recommendations, while the Spring Boot service manages user interactions and communicates with the Django service to fetch recommendations. This setup provides a scalable and modular approach to building microservices.