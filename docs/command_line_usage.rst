Command line usages
=========

`Random Profile Generator` can be used as a command line tool. 
It can be used to generate a random profile and save it to a file. 
It can also be used to generate a random profile and print it to the console.

Usages:

.. code-block:: bash

    random-profile --help
    Usage: random-profile [OPTIONS]

    random-profile -n 10 -p

    optional arguments:
        -h, --help      show this help message and exit
        -n N            Number of random profiles
    
        -f, --fullname  Get full name instead of first name
        -p, --profile   Get full profile instead of first name
        -l, --lastname  Get last name instead of first name
        -ip, --ipv4     Get an ipv4 IP address
        -j, --jobtitle  Get job title
    
Get Random Profile:
------------

.. code-block:: bash

    # n = number of random profiles, p = profile
    random_profile -n 10 -p

Get First Name:
------------

.. code-block:: bash

    # n = number of random profiles, f = first name
    random_profile -n 10 -f 

Get Last Name:
------------

.. code-block:: bash

    # n = number of random profiles, l = last name
    random_profile -n 10 -l

Get Job Title:
------------

.. code-block:: bash

    # n = number of random profiles, j = job title
    random_profile -n 10 -j

Get IPv4 Address:
------------

.. code-block:: bash

    # n = number of random profiles, ip = ipv4
    random_profile -n 10 -ip

Get Random Profile and Save to File:
------------

.. code-block:: bash

    # n = number of random profiles, p = profile
    random_profile -n 10 -p > random_profiles.txt

Get Random Profile version:
------------

.. code-block:: bash

    random_profile --version

    random-profile 0.2.3


Get Only Gender Specific Profiles:
------------

To get gender specific profiles, use the `-ma` or `-fe` flags.

.. code-block:: bash

    # n = number of random profiles, p = profile -ma male
    random_profile -n 10 -p -ma

    # n = number of random profiles, p = profile -fe female
    random_profile -n 10 -p -fe

