Import as module
------------

You can import the module and use it in your own scripts. 

.. code-block:: python

    from random_profile import RandomProfile
    rp = RandomProfile()

        # For first name
    rp.first_name(num=10)

    # For full name
    rp.full_name(num=8)

    # override the num value
    rp.full_profile(num=10)

    # For last name
    rp.last_name(num=6)
