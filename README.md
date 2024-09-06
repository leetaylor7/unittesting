Unit Test Notes

Atoms of Unit Test
- Assertions:
-   A definite statement about the outcome of a piece of code given a set of parameters


![image](https://github.com/user-attachments/assets/12e6f9da-4eb9-45e1-a6b7-14f5a92ed601)

Unittest Best Practices
- One assertion statement per test method
- Detailed class name describing system under test
- Detailed method name describning specific outcome being tested

Unittest module resources
-The ultimate resource for the unittest module is located at the official documentation here: https://docs.python.org/3/library/unittest.html

-This documentation is extensive, probably a little too extensive so if you’re short on time and want to zero-in on what you’ll need to know in order to complete the lab then make sure to check out the TestCase class: https://docs.python.org/3/library/unittest.html#unittest.TestCase

The TestCase provides several assert methods that allows you to check and report failures. If there’s one thing you’ll need to understand in the unittest module it’s in that section! 

-Also, if you get the chance, read up about the command line interface for unittest: https://docs.python.org/3/library/unittest.html#command-line-interface

This is a tool that allows you to test classes, modules, or individual methods from the command line. All you need to do is open the terminal and run it from the command line as shown below:

$ python -m unittest  module_one.py module_two.py module_three.py

You can include as many or as few as one module in the command line argument. To view the various command line options check this portion of the docs out: https://docs.python.org/3/library/unittest.html#command-line-options

If you get a chance, read all of the module; it contains tips and best practices with unittest. If you want some reading to quench your unit testing curiosity then read up on 
Junit
 and 
SUnit
. Junit begot unittest, and SUnit begot Junit, that’s the way that software evolved. 
