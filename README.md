FUNCTIONALITY AND FEATURES OF THE PET STORE API

### Admin Features

1. Manage Stores (CRUD Operations)

   - Create a Pet Store: Admins can add a new store with name, locations details and contact information.
   - Read a Pet Store: Admins can view a list of all stores or details of a specific store.
   - Update a Pet Store: Admins can modify pet store details to keep information up-to-date.
   - Delete a Pet Store: Admins can remove pet store that are no longer operational.

2. Manage Pet Items (CRUD Operations)

   - Create Pet Item: Admins can add new pet items to the inventory. It includes details like name, description, price and pet type (example - Bird, Cat, Dog).
   - Read Pet Item: Admins can view a list of all pet items or details of a specific pet item.
   - Update Pet Item: Admins can update information about pet items. As an example update the description, price or availability.
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

3. Reviews and Ratings
   - Leave Reviews and Ratings: Customers can leave a feedback and rate pet items they have purchased, sharing their experiences to help other customers make informed decisions.

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


Trello Board URL -
https://trello.com/b/V7dw2MOe/pet-shop-flask-api


### PET STORE API using Flask, PostgreSQL Database and JWT.

activate python virtual environment:
```
source .venv/bin/activate
```

How to install requirements:
```
pip install -r requirements.txt
```
How to add list of all the installed packages with their corresponding versions in the Python environment to requirements.txt
```
pip freeze > requirements.txt
```

OPENAPI SWAGGER UI PATH
```
http://127.0.0.1:5000/swagger-ui
```

### Pet Store REST API
### stores 
#### Operations on pet stores
HTTP verb
### POST
Path or route
```
/store
```
Any required body data
#### Request body
```
{
  "store_name": "string",
  "store_location": "string"
}
```
#### Example Request body
```
{
	"store_name": "PetHeaven",
	"store_location": "Melboure"
}
```
#### Response
Code 201 Created

```
{
  "id": 0,
  "store_name": "string",
  "store_location": "string",
  "petitems": [
    {
      "id": "string",
      "item_name": "string",
      "item_description": "string",
      "price": 0
    }
  ]
}
```
#### Example Response
```
{
	"id": 4,
	"store_name": "PetHeaven",
	"store_location": "Melboure",
	"petitems": [
		{
			"id": "4",
			"item_description": "Food and Water Dispenser",
			"item_name": "Food and Water Bowl",
			"price": 17.5
		}
	]
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
```
[
  {
    "id": 0,
    "store_name": "string",
    "store_location": "string",
    "petitems": [
      {
        "id": "string",
        "item_name": "string",
        "item_description": "string",
        "price": 0
      }
    ]
  }
]
```
#### Example Response
```
[
	{
		"id": 1,
		"petitems": [
			{
				"id": "1",
				"item_description": "German Shepherd belt",
				"item_name": "Dog belt",
				"price": 35.0
			}
		],
		"store_location": "Melbourne",
		"store_name": "Chilly"
	},
	{
		"id": 2,
		"petitems": [
			{
				"id": "2",
				"item_description": "Bird feeding stand",
				"item_name": "Bird feeder",
				"price": 42.5
			}
		],
		"store_location": "Brisbane",
		"store_name": "HappyPet"
	},
	{
		"id": 4,
		"petitems": [
			{
				"id": "4",
				"item_description": "Food and Water Dispenser",
				"item_name": "Food and Water Bowl",
				"price": 17.5
			}
		],
		"store_location": "Melboure",
		"store_name": "PetHeaven"
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
/store/4
```
#### Response
#### When Successful
Code 200 OK
```
{
  "id": 0,
  "store_name": "string",
  "store_location": "string",
  "petitems": [
    {
      "id": "string",
      "item_name": "string",
      "item_description": "string",
      "price": 0
    }
  ]
}
```
#### Example Response
```
{
	"id": 4,
	"petitems": [
		{
			"id": "4",
			"item_description": "Food and Water Dispenser",
			"item_name": "Food and Water Bowl",
			"price": 17.5
		}
	],
	"store_location": "Melboure",
	"store_name": "PetHeaven"
}
```
#### Response
#### When Not Found
#### Code 404 NOT FOUND
```
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
```
{
	"message": "Pet Store deleted"
}

```
#### Response
#### When Not Found
#### Code 404 NOT FOUND
```
{
	"code": 404,
	"status": "Not Found"
}
```
