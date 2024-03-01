# Bookstore API

## Setup

Create a `.env` file in the root of the project and add the environment variables listed in the `.env.example` file.

## Docker

You can also run the server using Docker. Just run the following command:

```bash
docker-compose build
docker-compose up -d
```

This will start the server and the database.

## Initial data

Three users will be created by default when the server starts. The credentials are:

- user1@example.com:password123 (librarian)
- user2@example.com:password456 (admin)
- user3@example.com:password789 (customer)

## API

The API documentation is available at `/docs`.

