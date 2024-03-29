# Ramsey

Open-source and better alternative to [AWS Neptune](https://aws.amazon.com/neptune/)

Ramsey, named after [Frank Ramsey](<https://en.wikipedia.org/wiki/Frank_Ramsey_(mathematician)>), is a open-source managed graph database.

## Why?

Neptune DB has some glaring [limitations](https://docs.aws.amazon.com/neptune/latest/userguide/limits.html) that make it unfit for many applications. Ramsey is an attempt to solve some of those issues.

Some particular ones to note:

1. There is a size limit of 55 MB on the size of an individual property or label.
2. The total size of Gremlin and SPARQL HTTP requests must be less than 150 MB.
3. A Neptune cluster volume can grow to a maximum size of 128 tebibytes (TiB) (this one might be hard for Ramsey to solve)

## Query engine

- **Gremlin**

## Simplified High-Level Overview for a Gremlin Query Engine

1. WebSocket Interface: Establish a WebSocket service that allows users to submit Gremlin queries in real-time. This will be the main interface for communication between the user and the database.

2. API Key Authentication: Use API key authentication to verify users before they can submit queries, ensuring that only authorized users can access the database.

3. Gremlin Database Connection: Maintain a connection to the Gremlin database, where the engine executes received queries and returns results to the user via the WebSocket connection.
