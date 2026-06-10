# 📘 Assignment: Database-backed APIs with SQLAlchemy

## 🎯 Objective

Build a FastAPI REST API backed by a SQLite database using SQLAlchemy so students can persist and manage data through CRUD operations.

## 📝 Tasks

### 🛠️ Configure the database and data models

#### Description
Set up SQLAlchemy with a SQLite database and define a model that represents a data record.

#### Requirements
Completed program should:

- Create a SQLAlchemy `Base` model for a resource such as `Product`
- Configure a SQLite database engine and session factory
- Create database tables automatically when the app starts
- Define Pydantic request and response schemas for validation

### 🛠️ Build REST endpoints for CRUD operations

#### Description
Implement API endpoints to create, read, update, and delete database records.

#### Requirements
Completed program should:

- Add `POST`, `GET`, `PUT`, and `DELETE` endpoints for the resource
- Validate request bodies with Pydantic models
- Use SQLAlchemy sessions to read and write database records
- Return appropriate HTTP responses for missing or invalid records

### 🛠️ Persist and test data behavior

#### Description
Ensure data changes persist in the database and verify the API behavior using example requests.

#### Requirements
Completed program should:

- Save new resources to the database on create
- Update and delete records with database persistence
- Return stored data in response JSON
- Include example request and response formats in comments or documentation
