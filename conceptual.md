### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
    A standard for routes that need to be included.  GET, POST, PUT, PATCH, and DELETE.
- What is a resource?
  A resource is a what the website's URL returns. For instance, JSON. The resource is received, then developer decides what to do with it.

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
    Creating a user a POST request that sends information to the database, there is no need to render a form.

- What does idempotent mean? Which HTTP verbs are idempotent?
    An operation that can be performed many times (with same data) and the result will be the same as if it had been done once.  GET, PUT/PATCH, DELETE are examples. 

- What is the difference between PUT and PATCH?
    PUT updates the entire entry, whereas patch updates specific portions.
- What is one way encryption?
    Using bycrpt and it's setting how many work factors you want.

- What is the purpose of a `salt` when hashing a password?
    Extra measure of security added, so even if someone had a database of passwords, it would not be easy to find the correct one.
- What is the purpose of the Bcrypt module?
    To hash, to encrypt values, like passwords. 
- What is the difference between authorization and authentication?
        Authenticating is when you are verifying that a user and password match that which is in the database.  Whereas authorization deals with what access is provided. For instance an admin may be authorized to delete posts, where the average user is not.
