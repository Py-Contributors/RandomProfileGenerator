Run test cases
==============

For the test cases, we are using `pytest`. The test cases are located in the `tests` directory. To run the test cases, you can use the following command:

.. code-block:: bash 

    # check the code coverage and run the test cases
    coverage run -m pytest
    coverage report

.. code-block:: bash

    pytest tests

.. code-block:: bash

    flake8 . --ignore=E501,E402


You can also run the test cases with coverage:

