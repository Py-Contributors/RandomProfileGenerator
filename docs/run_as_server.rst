Run as server
=============

To run as a server, you need to specify the port to listen on:


.. code-block:: bash

    default port is 8000
    $ rp --server --port 8080

This will start a server on port 8080. You can then use the client to connect to it:

Test it with postman

.. code-block:: bash

    $ curl -X GET http://localhost:8080/ -H 'Content-Type: application/json'

Interactive Api Documentation

`http://localhost:<port>/docs`

API Endpoints
-------------

`localhost:8000/api/v1/random_profile/full_profile?num=10`
`localhost:8000/api/v1/random_profile/first_name?num=10`
`localhost:8000/api/v1/random_profile/last_name?num=10`
`localhost:8000/api/v1/random_profile/full_name?num=10`