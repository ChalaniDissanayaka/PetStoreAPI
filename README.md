## T2A2 - PET STORE API - Chalani Dissanayaka

### Flask PET STORE API Developed as a part of Coder Academy T2A2 Assignment

GitHub Repository
https://github.com/ChalaniDissanayaka/PetStoreAPI

Trello Board URL 
https://trello.com/b/V7dw2MOe/pet-shop-flask-api


### PET STORE API using Flask, PostgreSQL Database and JWT.
### Set up instructions for python environment, PostgreSQL Database and run the PET STORE API 

1. clone the PET STORE API from GitHub repo 
https://github.com/ChalaniDissanayaka/PetStoreAPI

2. change the directory to /src/PetStoreAPI

3. activate python virtual environment

```
source .venv/bin/activate
```
### installation instructions
How to install requirements

```
pip install -r requirements.txt
```
How to add list of all the installed packages with their corresponding versions in the Python environment to requirements.txt
```
pip freeze > requirements.txt
```
How to run PET STORE API

```
flask run
```

OPENAPI SWAGGER UI PATH
```
http://127.0.0.1:5000/swagger-ui
```

### Make sure to set up PostgreSQL and .env file before run the PET STORE API
How to set up PostgreSQL

login to postgres
```
psql postgres
```
create a database
```
CREATE DATABASE petstore_db;
```
set the password
```
CREATE USER petstore_dev WITH PASSWORD '123456';
```
Grant the permission to user to use the database
```
GRANT ALL PRIVILEGES ON DATABASE petstore_db TO petstore_dev;
```
Grant the schema permission to user
```
GRANT ALL ON SCHEMA public TO petstore_dev;
```
connect to database
```
\c petstore_db
```
### How to set up .env file
create a file called .env in /src/PetStoreAPI

add following lines to the .env file
```
DATABASE_URL="postgresql+psycopg2://petstore_dev:123456@localhost:5432/petstore_db"
JWT_SECRET_KEY="chalani"
```
### Testing
### Admin Accounts

   - User with ID = 1 or 2 or 3 is the administrator. So first 3 users are Admin users. 
   -  /register endpoint to create a user account
   -  /login endpoint to get a jwt access_token
```python
@jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity < 4:
            return {"is_admin": True}  # I assumed the User with ID = 1 or 2 or 3 is the administrator.
        return {"is_admin": False}
```

## R1: Explain the problem that PET STORE API will solve, and explain how this app solves or addresses the problem.

### Problem Significance for Pet Store API

The motivation to create the PET STORE API came from a personal experience of trying to buy a bird feeder online but being unable to find the desired product without visiting multiple stores. By creating the Pet Shop API, I aim to eliminate such frustrations for other pet owners, offering a seamless and efficient shopping experience that meets their needs conveniently.

The Pet Store API addresses a significant gap in the pet supply market by offering a centralized platform for pet owners to find a store and purchase pet items. Traditional shopping methods often require visiting multiple stores to find specific petitems, which can be time-consuming and inconvenient. The Pet Store API streamlines the process, making it easier for users to locate and buy the petitems they need.

Furthermore, The Pet Store API supports businesses by providing a robust system to manage stores, petitems and promotions effectively using badges. This leads to better user experience, as stores can ensure they have the right petitems available at the right times. It also allows for dynamic marketing strategies, such as applying discounts to specific petitems, which can drive sales and enhance customer satisfaction.

### FUNCTIONALITY AND FEATURES OF THE PET STORE API TO SOLVE THE PROBLEM

### Admin Features

1. Manage Stores (CRUD Operations)

   - Create a Pet Store: Admins can add a new store with name, locations details and contact information.
   - Read a Pet Store: Admins can view a list of all stores.
   - Read a Pet Store: Admins can view a specific store using store_id.
   - Delete a Pet Store: Admins can remove pet store that are no longer operational.
   - Admin should unlink all attached petitems before Delete a Pet Store. 

2. Manage Pet Items (CRUD Operations)

   - Create Pet Item: Admins can add new pet items to the inventory. It includes details like name, description, price.
   - Read Pet Item: Admins can view a list of all pet items or details of a specific pet item.
   - Update Pet Item: Admins can update information about pet items. As an example update the description, price.
   - Delete Pet Item: Admins can remove pet items from the inventory that are no longer available or needed.

3. Add Discounts Based on Badges
   - Admins can apply discounts to pet items based on their badges (Example - Blue, Green, Orange). This allows to add promotion to a specific pet items with special offers.

### Customer Features

1. User Account Management

   - Sign Up: Customers can create a new account by providing necessary details such as name, email, and password.
   - Log In: Customers can log in to their account using their credentials to access personalized features and perform actions securely.

2. Browsing and Exploring Pet Items

   - Browse Pet Items: Customers can view all available pet items in the pet store. Pet store has many items belong to many badges.
   - View Pet Item Details: Customers can see detailed information about a specific pet item. It includes pet item name, description, price and any available discounts. This helps customers make informed decisions about their purchases.


### User Stories Overview

### Admin Stories

    - Store Management:
       - Create, read, update and delete pet store to maintain the Pet Store effectively.

    - Pet Item Management:
       - Create, read, update and delete pet items to control inventory and keep track of available items.

    - Discount Management:
       - Add discounts to pet items based on badges (Example - Blue, Green, Orange) to promote specific items with special offers.

### Customer Stories

    - Account Management:
       - Sign up for an account to access and use the Pet Store API.
       - Log in to securely access personalized features and perform actions.

    - Pet Item Browsing:
       - Browse all available pet items in the pet store to explore the variety of items offered.
       - View details of specific pet item. It should include name, description, price and discounts. The details will help to make informed purchase decisions.

    - Reviews and Ratings:
       - Leave reviews and ratings for purchased pet items to share experiences and help other customers.

These user stories outline the essential functionalities required for both Admin and Customer roles within the Pet Store API. Pet Store API is addressing specific actions and facilitate tailored functionalities to each user's needs in managing and interacting with the pet store web application.

## R3: List and explain the third-party services, packages and dependencies used in this app.


## Flask-Smorest
Using Flask-Smorest for a Pet Store REST API offers many advantages. 

1. Automatic Documentation

   - Flask-Smorest integrates seamlessly with OpenAPI and generate interactive API documentation automatically. It provides Swagger (with Swagger UI) and other documentations out of the box. This is particularly useful for providing clear and accessible API documentation for my Pet Store API. It will be easy for frontend developers to understand and use Pet Store API endpoints.

2. Validation and Serialization

   - Flask-Smorest provides built-in request validation and response serialization using Marshmallow schemas. These features ensure that the data coming into and going out of Pet Store API is consistent and confirms the expected formats. It helps to reduce bugs and errors.

3. Modular Design

   - Flask-Smorest encourages a modular approach to building APIs. I can organize my endpoints into Blueprints and make Pet Store API codebase cleaner and more maintainable. For the Pet Store API, I created separate blueprints for handling different resources like PetItems, stores and badges.

4. Error Handling

   - Flask-Smorest offers structured and consistent error handling out of the box. This helps in providing clear error messages and status codes to the clients. It improves the overall Pet Store API user experience.

5. Ease of Use

   - Flask-Smorest is designed to be easy to use and integrates well with other Flask extensions. Its syntax and structure are straightforward. It makes development easy for developers who are already familiar with Flask.

6. Extensibility

   - The extension is highly customizable. It allows us to extend its functionality to meet our specific needs. For example, I can add custom authentication, authorization suitable for Pet Store API.

7. Compatibility

   - Flask-Smorest is part of the Flask ecosystem. Flask-Smorest is compatible with other Flask extensions and libraries. This allows us to leverage a wide range of existing tools and plugins to enhance Pet Store API.

Flask-Smorest makes sure that Pet Store REST API is well-documented, reliable, maintainable and user-friendly. Flask-Smorest provides a solid foundation for future development and scalability.

## PostgreSQL

   - PostgreSQL is a powerful, open-source relational database management system known for its advanced features and reliability. It supports complex queries, extensive data types and transactional integrity. PostgreSQL’s scalability, extensibility and compliance with ACID principles make it ideal for diverse applications. PostgreSQL is an excellent choice for small projects to large-scale enterprise systems.

## Flask

   - Flask is a lightweight, flexible web framework for Python. Flask is ideal for building web applications and APIs. It offers simplicity with its modular design, enabling developers to add extensions as needed. Flask's ease of use, comprehensive documentation and active community support make it a popular choice for developers.


## SQLAlchemy

   - SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a flexible and efficient way to interact with databases. It has features like schema generation, query construction and transaction management. SQLAlchemy simplifies complex database operations in Python applications.


## Psycopg2

   - Psycopg2 is a powerful PostgreSQL adapter for Python. It enables efficient database interactions. Psycopg2 has features like advanced transaction management, server-side cursors and asynchronous communication. It excels in performance and reliability. The psycopg2-binary package simplifies installation, providing a pre-compiled version suitable for various environments.


## passlib

   - Passlib.hash is a module within Passlib that provides a variety of secure password hashing algorithms. It simplifies the creation, verification and management of hashed passwords. It makes sure strong protection against attacks. This module supports adaptive algorithms and seamless upgrades. It is ideal for robust password security in Python applications.

## bcrypt

   - bcrypt is a robust password hashing library that enhances security by applying adaptive hashing. It incorporates a salt to protect against rainbow table attacks and adjusts the hashing complexity over time. bcrypt helps to securely hash and verify passwords. bcrypt ensures strong protection against unauthorized access.

## Marshmallow

   - Marshmallow is a Python library for object serialization and deserialization. Marshmallow converts complex data types into Python data structures and vice versa. It facilitates data validation, transformation and schema definition. Marshmallow is ideal for API development and data exchange. Marshmallow ensures streamlined data handling in Python applications.

## Flask-JWT-Extended

   - Flask-JWT-Extended is an extension for Flask that simplifies JWT (JSON Web Token) authentication. It provides easy-to-use tools for generating, decoding and validating tokens. Flask-JWT-Extended enhance security in web based applications. It has features like token refresh, custom claims and access controls. Flask-JWT-Extended streamlines the implementation of robust authentication systems.

## python-dotenv

   - python-dotenv is a Python library that loads environment variables from a .env file into the environment. It simplifies managing configuration settings and sensitive data by keeping them separate from the code. This tool is essential for manage environment-specific variables and improve security in development and production environments.

## R4: Explain the benefits and drawbacks of this app’s underlying database system.

### Benefits of Using PSQL for Pet Store REST API

1. Open Source

   - Cost-Effective: PostgreSQL is free to use. It is a cost-effective solution for businesses of all sizes.
   - Community Support: A large and active community continuously improves the database. They provide support and offers many extensions.

2. Scalability

   - Horizontal Scaling: Into and out of replication and partitioning techniques database can scale out horizontally to handle large volumes of data.
   - Vertical Scaling: Can efficiently use the resources of high-end hardware for vertical scaling.

3. Performance

   - Concurrency: Uses Multi-Version Concurrency Control (MVCC) to handle multiple transactions same time without conflicts.
   - Query Optimization: Advanced query planner and optimizer is ensuring efficient execution of complex queries.
   - Indexing Options: Supports many indexing methods like B-tree, hash, GiST, GIN and SP-GiST for improved performance.

4. Many Feature

   - ACID Compliance: Guarantee reliable transactions with Atomicity, Consistency, Isolation, and Durability.
   - Advanced Data Types: PostgreSQL supports JSON, XML and hstore for key value storage, arrays.
   - Full Text Search: PostgreSQL provides feature for full-text search. It is very useful for applications which need search functionality.

5. Extensibility

   - Custom Functions: PostgreSQL allows custom functions and procedures using languages like PL/pgSQL, PL/Python.

6. Security

   - Robust Security Features: PostgreSQL supports various authentication methods.
     examples - MD5, GSSAPI, SSPI, LDAP, SCRAM-SHA-256
   - Row-Level Security: Allows for specific access control by defining policies on tables.

7. Data Integrity

   - Foreign Keys: Guarantee data integrity by enforcing referential integrity through foreign keys.
   - Constraints: PostgreSQL supports unique, not null, check to maintain data correctness.

8. Backup and Recovery

   - Point in Time Recovery: Allows for accurate data recovery to any point in time using Write Ahead Logging (WAL).
   - Backup Tools: Advanced tools for backup and restore operations. As an Example tools like pg_dump, pg_restore, and pg_basebackup.

### Drawbacks of Using PSQL for Pet Store REST API

1. Complexity

   - Learning Curve: PostgreSQL has a steep learning curve. Most of the time for beginners or those are new to SQL databases. PostgreSQL has many features to learn.
   - Configuration: Need a reasonable amount of configuration and tuning to achieve optimal performance. Database tuning can be a complex task for a new developer.

2. Resource Intensive

   - Memory Usage: PostgreSQL can be memory intensive. Most of the time when it is dealing with large datasets and complex queries. We need relevant hardware resources to manage large scale applications effectively.

3. Performance in Certain Use Cases

   - Write Heavy Workloads: PostgreSQL performs well for most read and write operations. But PostgreSQL may not be as efficient compared to other databases like MySQL or specialized NoSQL databases when it comes to extremely write heavy environments.

4. Compatibility and Migration Issues

   - SQL Syntax: PostgreSQL is highly accommodating with SQL standards. But some time it can have differences in SQL syntax and functions compared to other SQL databases. These differences can lead to compatibility issues.

5. Version Upgrade Management

   - Upgrade Path: It is difficult to manage version upgrades. Most of the time minor updates are usually straightforward. But major version upgrades may require a lot of planning, testing. Maybe we need to plan ahead for a downtime. Web based application will be unavailable during the downtime.

### Conclusion

PostgreSQL is a flexible, powerful and reliable database system that offers a wealth of features and capabilities. It is open source with strong community support and extensive features. PostgreSQL makes an excellent choice for developers and businesses looking for a strong database solution.

## R5: Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in Pet Store REST API

### Pet Store REST API
### Features

1. Database Abstraction:

   - Cross-database Compatibility: Write database-independent code that works with multiple database backends like PostgreSQL, MySQL, SQLite, etc.
   - Schema Management: Automatically generate and manage database schemas using Python classes.

2. Object Relational Mapping (ORM):

   - Declarative Mapping: Define database tables and relationships using Python classes.
   - Relationships: Easily establish and manage complex relationships between tables. As an example one-to-many and many-to-many.

3. Query Construction:

   - SQL Expression Language: Build complex SQL queries programmatically using Python expressions.
   - ORM Queries: Query the database using Pythonic syntax with full support for SQL joins, filters and aggregations.

4. Session Management:

   - Unit of Work Pattern: Manage database transactions and sessions efficiently to make sure data consistency and integrity.
   - Lazy Loading: Optimize database access by loading related objects on demand.

5. Flexibility:

   - Raw SQL Execution: Execute raw SQL queries when needed. Provide fine-grained control over database interactions.
   - Custom Types: Define custom data types and behavior for specialized needs.

### Purpose
The primary purpose of using SQLAlchemy in the Pet Store REST API is to streamline database interactions by abstracting the complexities of SQL. It is easy to develop, maintain and work with database records as Python objects. 

### Functionalities

1. Define Models

   - Define models for entities like PetItemModel, UserModel and BadgeModel using Python classes. Each class maps to a corresponding table in the database.

2. CRUD Operations

   - Perform Create, Read, Update and Delete (CRUD) operations using SQLAlchemy ORM capabilities.
   - Example - Read operation from User.
   - ```python
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
        abort(409, message="A user with that username already exists.")
     ```

3. Relationships and Joins

   - Easily navigate and query related data using SQLAlchemy relationship management.

4. Transactions and Sessions

   - Manage transactions and sessions to ensure data consistency.

### Conclusion

SQLAlchemy usage in the Pet Store REST API simplifies the interaction with the database by providing a high-level, Pythonic interface for managing database records.
It offers robust features for ORM, query construction and session management. It makes a great choice for building scalable and maintainable web based applications.

## R6: Design an entity relationship diagram (ERD) for Pet Store REST API app database, and explain how the relations between the diagrammed models will aid the database design. 

### Database design BEFORE coding started - The project planning phase.

attach the diagram here. 

### Entities

   - Store
   - Badge
   - PetItem
   - User

### many-to-many relationship between PetItem and Badge
1. Relationship between Badges and PetItems

   - One PetItem can have many badges
   - One Badge can have many PetItems

2. In many-to-many relationship, one model could not have a single value as a foreign key.
   So we need another table (a secondary table) that has, in each row, a Badge ID and PetItem ID.

3. As an Example - 

   Entity Name - petitem_badge
   Table name - petitems_badges
   ```
   id , badge_id, petitem_id
   1      2          3
   2      2          4
   3      4          1
   4      3          1
   ```
4. Explanation of the table - petitems_badges

   - Badge with ID 2 is linked to petitems with IDs 3 and 4
   - Badge with ID 4 is linked to petitem with ID 1
   - Badge with ID 3 is linked to petitem with ID 1

   Because of that

   - petitem with IDs 3 and 4 are linked to Badge with ID 2
   - petitem with ID 1 is linked to Badge with ID 4
   - petitem with ID 1 is linked to Badge with ID 3

5. many-to-many relationships use a secondary table which stores which models of one side are related to which models of the other side.
6. This is how many-to-many relationships work. It is through the above secondary table. The Badge.petitems and PetItem.badges attributes will be populated by SQLAlchemy.
7. The rows in this table keep a link between a specific badge and a specific petitem.
   But without the need for those values to be stored in the badge or petitem models themselves.
### One-to-many Relationship between Stores and PetItems

   - One-to-many relationship between Store and PetItems
   - One Store can have many PetItems
   - Each PetItem has one Store

### One-to-many Relationship between Stores and Badges

   - One Store can have many Badges
   - Each Badge has one Store

### One-to-many Relationship between Stores and Users

   - One Store can have many Users
   - Each User has one Store

## R7: Explain the implemented models and their relationships, including how the relationships aid the database implementation.

### Database implementation AFTER coding has started - The project development phase of Pet Store REST API.

The models used in Pet Store REST API are in different files within the models folder. 

`StoreModel`
```python
class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(80), unique=True, nullable=False)
    store_location = db.Column(db.String(100), unique=True, nullable=False)

    petitems = db.relationship("PetItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
    badges = db.relationship("BadgeModel", back_populates="store", lazy="dynamic")
```
#### One-to-many Relationship between Stores and PetItems

   - One-to-many relationship between Store and PetItems
   - One Store can have many PetItems
   - Each PetItem has one Store

#### One-to-many Relationship between Stores and Badges

   - One Store can have many Badges
   - Each Badge has one Store

#### The above code snippet db.relationship command defines the relationship between the models in the Pet Store REST API

```python
petitems = db.relationship("PetItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
```
   - One Store can have many PetItems
   - Each PetItem belongs to a single store. 
   - If we want to delete a store which has attached petitems then it won't allow us to delete the store. 
   - When we delete a model that has a relationship to other models that still exist, then the default behavior in SQLAlchemy with PostgreSQL is to raise an error. 
   - This is because SQLAlchemy does not want to allow us to accidentally delete data that is still being used by other models.
   - Let's say we have a store 1 that has two petitems, petitem 1 and petitem 2. 
   - If we try to delete store 1 without first deleting petitem 1 and petitem 2, SQLAlchemy will raise an error because the petitems are still attached to the store.
   - This means the petitems have a Foreign Key that references the store we are trying to delete. If the store actually was deleted, then the petitems have a store ID that references something that doesn't exist.
   - To fix the issue, we can use a feature called "cascading deletes". Cascading deletes allow us to specify that when a model is deleted, any related models should also be deleted automatically.


`PetItemModel`
```python
class PetItemModel(db.Model):
    __tablename__ = "petitems"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80), unique=True, nullable=False)
    item_description = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)

    store = db.relationship("StoreModel", back_populates="petitems")
    badges = db.relationship("BadgeModel", back_populates="petitems", secondary="petitems_badges")
```
#### One-to-many Relationship between Stores and PetItems

   - One-to-many relationship between Store and PetItems
   - One Store can have many PetItems
   - Each PetItem has one Store
   - store_id ForeignKey references stores table

`BadgeModel`
```python
class BadgeModel(db.Model):
    __tablename__ = "badges"

    id = db.Column(db.Integer, primary_key=True)
    badge_name = db.Column(db.String(80), unique=True, nullable=False)
    colour_code = db.Column(db.String(20), unique=False, nullable=False)
    discount = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)

    store = db.relationship("StoreModel", back_populates="badges")
    petitems = db.relationship("PetItemModel", back_populates="badges", secondary="petitems_badges")
```
#### One-to-many Relationship between Stores and Badges

   - One Store can have many Badges
   - Each Badge has one Store
   - store_id ForeignKey references stores table

`PetItemBadgeModel`
```python
class PetItemBadgeModel(db.Model):
    __tablename__ = "petitems_badges"

    id = db.Column(db.Integer, primary_key=True)
    petitem_id = db.Column(db.Integer, db.ForeignKey("petitems.id"))
    badge_id = db.Column(db.Integer, db.ForeignKey("badges.id"))
```
#### many-to-many relationship between PetItem and Badge
1. Relationship between Badges and PetItems

   - One PetItem can have many badges
   - One Badge can have many PetItems

2. In many-to-many relationship, one model could not have a single value as a foreign key.
   So we need another table (a secondary table) that has, in each row, a Badge ID and PetItem ID.

3. As an Example - 

   Entity Name - petitem_badge
   Table name - petitems_badges
   ```
   id , badge_id, petitem_id
   1      2          3
   2      2          4
   3      4          1
   4      3          1
   ```
4. ForeignKey references

   - petitem_id ForeignKey references petitems table
   - badge_id ForeignKey references badges table

`UserModel`
```python
class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
```
#### One-to-many Relationship between Stores and Users

   - One Store can have many Users
   - Each User has one Store

## R8: Explain how to use Pet Store REST API endpoints. Each endpoint should be explained.

## stores 
#### Operations on pet stores

HTTP verb
### POST
Path or route
```
/store
```
Any required body data
#### Request body
```json
{
  "store_name": "string",
  "store_location": "string"
}
```
#### Example Request body
```json
{
	"store_name": "PetHeaven",
	"store_location": "Melboure"
}
```
#### Response
Code 201 Created

```json
{
  "id": 0,
  "store_name": "string",
  "store_location": "string",
  "petitems": [
    {
      "id": 0,
      "item_name": "string",
      "item_description": "string",
      "price": 0
    }
  ],
  "badges": [
    {
      "id": 0,
      "badge_name": "string",
      "colour_code": "string",
      "discount": 0
    }
  ]
}
```
#### Example Response
```json
{
	"badges": [],
	"id": 6,
	"petitems": [],
	"store_location": "Melboure",
	"store_name": "PetHeaven"
}
```
HTTP verb
### GET
Path or route
```
/store
```
#### Response
Code 200 OK
```json
[
  {
    "id": 0,
    "store_name": "string",
    "store_location": "string",
    "petitems": [
      {
        "id": 0,
        "item_name": "string",
        "item_description": "string",
        "price": 0
      }
    ],
    "badges": [
      {
        "id": 0,
        "badge_name": "string",
        "colour_code": "string",
        "discount": 0
      }
    ]
  }
]
```
#### Example Response
```json

[
	{
		"badges": [],
		"id": 1,
		"petitems": [
			{
				"id": 1,
				"item_description": "German Shepherd belt",
				"item_name": "Dog belt",
				"price": 29.75
			}
		],
		"store_location": "Melbourne",
		"store_name": "Chilly"
	},
	{
		"badges": [
			{
				"badge_name": "Bird food items",
				"colour_code": "Orange",
				"discount": 15.0,
				"id": 1
			},
			{
				"badge_name": "Dog food items",
				"colour_code": "Green",
				"discount": 10.0,
				"id": 2
			},
			{
				"badge_name": "Pet toys",
				"colour_code": "Yellow",
				"discount": 15.0,
				"id": 3
			},
			{
				"badge_name": "Dog collar",
				"colour_code": "Red",
				"discount": 5.0,
				"id": 4
			}
		],
		"id": 2,
		"petitems": [
			{
				"id": 2,
				"item_description": "Bird feeding stand",
				"item_name": "Bird feeder",
				"price": 42.5
			},
			{
				"id": 7,
				"item_description": "Pet Swimming assist",
				"item_name": "Pet Swimming assist",
				"price": 17.5
			},
			{
				"id": 8,
				"item_description": "Bird feed food item",
				"item_name": "Bird feed food",
				"price": 77.5
			}
		],
		"store_location": "Brisbane",
		"store_name": "HappyPet"
	},
	{
		"badges": [],
		"id": 6,
		"petitems": [],
		"store_location": "Melboure",
		"store_name": "Pet shop"
	}
]
		
```

HTTP verb
### GET
Path or route
```
/store/{store_id}
```
#### Example Path
```
/store/2
```
#### Response
#### When Successful
Code 200 OK
```json
{
  "id": 0,
  "store_name": "string",
  "store_location": "string",
  "petitems": [
    {
      "id": 0,
      "item_name": "string",
      "item_description": "string",
      "price": 0
    }
  ],
  "badges": [
    {
      "id": 0,
      "badge_name": "string",
      "colour_code": "string",
      "discount": 0
    }
  ]
}
```
#### Example Response
```json
{
	"badges": [
		{
			"badge_name": "Bird food items",
			"colour_code": "Orange",
			"discount": 15.0,
			"id": 1
		},
		{
			"badge_name": "Dog food items",
			"colour_code": "Green",
			"discount": 10.0,
			"id": 2
		},
		{
			"badge_name": "Pet toys",
			"colour_code": "Yellow",
			"discount": 15.0,
			"id": 3
		},
		{
			"badge_name": "Dog collar",
			"colour_code": "Red",
			"discount": 5.0,
			"id": 4
		}
	],
	"id": 2,
	"petitems": [
		{
			"id": 2,
			"item_description": "Bird feeding stand",
			"item_name": "Bird feeder",
			"price": 42.5
		},
		{
			"id": 7,
			"item_description": "Pet Swimming assist",
			"item_name": "Pet Swimming assist",
			"price": 17.5
		},
		{
			"id": 8,
			"item_description": "Bird feed food item",
			"item_name": "Bird feed food",
			"price": 77.5
		}
	],
	"store_location": "Brisbane",
	"store_name": "HappyPet"
}
```
#### Response
#### When Not Found
#### Code 404 NOT FOUND
```json
{
	"code": 404,
	"status": "Not Found"
}
```
#### Example Response
```json
{
	"code": 404,
	"status": "Not Found"
}
```

HTTP verb
### DELETE
Path or route
```
/store/{store_id}
```
#### Example Path
```
/store/4
```
#### Response
#### When Successful
#### Code 200 OK 
```json
{
	"message": "Pet Store deleted"
}

```
#### Response
#### When Not Found
#### Code 404 NOT FOUND
```json
{
	"code": 404,
	"status": "Not Found"
}
```
