# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Learn to build RESTful APIs with FastAPI by creating endpoints, handling request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description
Initialize a FastAPI application and configure the basic route structure.

#### Requirements
Completed program should:

- Create an instance of `FastAPI`
- Define a root endpoint (`/`) that returns a welcome message
- Run the app using `uvicorn` or a similar ASGI server

### 🛠️ Build CRUD-style Endpoints

#### Description
Add routes for creating and retrieving items with path and query parameters.

#### Requirements
Completed program should:

- Define a `GET /items/{item_id}` endpoint that returns item details
- Define a `POST /items` endpoint that accepts JSON request data
- Use Pydantic models for request validation and response formatting

### 🛠️ Validate Requests and Test the API

#### Description
Implement request validation, error handling, and verify the API behavior.

#### Requirements
Completed program should:

- Use `BaseModel` to validate incoming request bodies
- Return a `422` error for invalid input automatically
- Include example request and response JSON in comments or documentation
- Verify the endpoints in the browser or via cURL/Postman
