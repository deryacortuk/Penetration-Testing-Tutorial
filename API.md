 # GraphQL APIs

 GraphQL APIs use a custom query language and a single endpoint 
for all the API’s functionality. These endpoints are commonly located at /graphql, /gql, or /g. GraphQL has two main kinds of operations: queries 
and mutations. Queries fetch data, just like the GET requests in REST APIs.
Mutations create, update, and delete data, just like the POST, PUT, and 
DELETE requests in REST APIs.


# API-Centric Applications
Increasingly, APIs aren’t used as simply a mechanism to share data with outside developers. You’ll also encounter API-centric applications, or applications 
built using APIs. Instead of retrieving complete HTML documents from the 
server, API-centric apps consist of a client-side component that requests and 
renders data from the server by using API calls. Many mobile applications are built this way. When a company already has 
a web app, using an API-centric approach to build mobile apps saves time. 
APIs allow developers to separate the app’s rendering and data-transporting 
tasks: developers can use API calls to transport data and then build a separate rendering mechanism for mobile, instead of reimplementing the same 
functionalities.

GraphQL Playground (https://github.com/graphql/graphql-playground/) is 
an IDE for crafting GraphQL queries that has autocompletion and error 
highlighting.
ZAP has a GraphQL add-on (https://www.zaproxy.org/blog/2020-08-28
-introducing-the-graphql-add-on-for-zap/) that automates GraphQL introspection and test query generation. Clairvoyance (https://github.com/nikitastupin/
clairvoyance/) helps you gain insight into a GraphQL API’s structure when 
introspection is disabled.

