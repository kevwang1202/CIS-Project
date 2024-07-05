# Final Project (lwang308)

For the Online Order application, customers will be able to select the amount they want for 
each item and submit their order.

## Install requried libraries
Ensure that you are in the main directory and run the following:

This must be done before you can run the application if you are 
not using the included venv.

```shell
$ pip install tkinter
$ pip install pillow
$ pip install json
$ pip install random
$ pip install time
$ pip install pytest
```
Note: You can also import those packages in your Python file

## To run the program
Click the green triangle run icon in the top-right corner of the PyCharm window.
or
```shell
$ python lwang308_ProjectGUI.py
```
#### In the login prompt, use the following credential (optional)
* Order Name: ``Kevin Wang``
* Phone Number: ``7191234567``
* DOUBLE-DOUBLE COMBOS: ``0``
* CHEESEBURGER COMBOS: ``0``
* HAMBURGER COMBOS: ``0``
* DOUBLE-DOUBLE: ``0``
* CHEESEBURGER: ``0``
* HAMBURGER: ``0``
* FRENCH FRIES: ``0``
* SOFT DRINK (S): ``0``
* SOFT DRINK (M): ``0``
* SOFT DRINK (L): ``0``
* SOFT DRINK (XL): ``0``
* CHOCOLATE SHAKES: ``0``
* STRAWBERRY SHAKES: ``0``
* VANILLA SHAKES: ``0``
* Notes: ``Animal Style``

## Functionality

### Next Button
The next button allows the user to go to the Order Summary page when clicked and user's input value will also be 
display on the Order Summary page.

### Bock Button
The back button alLows the user to go back to the previous page when clicked.
So the user can make changes to their original input value.

### Clear Button
The clear button will delete all entered values on the specific page, but will not delete any values from the previous pages.

### Submit Button
The submit button will save and submit the user's entered values onto a data JSON-file called orders.csv. User's input value will also be 
display on the Final Order Detail page.

### Home Button
The home button brings the user back to the main/first page of the form when clicked.

### Contact Button
The contact button brings the user to the contact page of the form when clicked.

### Exit Button
The exit button will cleanly exit out of the form when clicked.

## Data Files
### orders.json
This contains the transaction data in the following format:

| Order Time               | Order Number | Order Name   | Phone Number   | Order Cost | DOUBLE-DOUBLE COMBOS | CHEESEBURGER COMBOS | HAMBURGER COMBOS | DOUBLE-DOUBLE | CHEESEBURGER | HAMBURGER | FRENCH FRIES | SOFT DRINK (S) | SOFT DRINK (M) | SOFT DRINK (L) | SOFT DRINK (XL) | CHOCOLATE SHAKES | STRAWBERRY SHAKES | VANILLA SHAKES | Notes         |
|--------------------------|--------------|--------------|----------------|------------|----------------------|---------------------|------------------|---------------|--------------|-----------|--------------|----------------|----------------|----------------|-----------------|------------------|-------------------|----------------|---------------|
| Wed Apr 19 20:41:33 2023 | 32           | Kevin Wang   | 123456789      | 23.26      | 0                    | 0                   | 0                | 2             | 3            | 0         | 2            | 0              | 0              | 0              | 0               | 2                | 0                 | 0              | Grilled Onion |
| Wed Apr 19 20:42:36 2023 | 853          | Mickey Mouse | 987654321      | 85.51      | 5                    | 5                   | 0                | 0             | 0            | 0         | 3            | 0              | 0              | 0              | 0               | 0                | 0                 | 6              | No Tomato     |

### orders.json
This contains the information related to the order that customers made in the following format.
```json
[{"Order Time": "Wed Apr 19 20:41:33 2023", "Order Number": 32, "Order Name": "Kevin Wang", 
  "Phone Number": "123456789", "Order Cost": 23.26, "DOUBLE-DOUBLE COMBOS": 0, "CHEESEBURGER COMBOS": 0, 
  "HAMBURGER COMBOS": 0, "DOUBLE-DOUBLE": 2, "CHEESEBURGER": 3, "HAMBURGER": 0, "FRENCH FRIES": 2, 
  "SOFT DRINK (S)": 0, "SOFT DRINK (M)": 0, "SOFT DRINK (L)": 0, "SOFT DRINK (XL)": 0, "CHOCOLATE SHAKES": 2, 
  "STRAWBERRY SHAKES": 0, "VANILLA SHAKES": 0, "Notes": "Grilled Onion"}, 
  {"Order Time": "Wed Apr 19 20:42:36 2023", "Order Number": 853, "Order Name": "Mickey Mouse", 
    "Phone Number": "987654321", "Order Cost": 85.51, "DOUBLE-DOUBLE COMBOS": 5, "CHEESEBURGER COMBOS": 5, 
    "HAMBURGER COMBOS": 0, "DOUBLE-DOUBLE": 0, "CHEESEBURGER": 0, "HAMBURGER": 0, "FRENCH FRIES": 3, 
    "SOFT DRINK (S)": 0, "SOFT DRINK (M)": 0, "SOFT DRINK (L)": 0, "SOFT DRINK (XL)": 0, "CHOCOLATE SHAKES": 0, 
    "STRAWBERRY SHAKES": 0, "VANILLA SHAKES": 6, "Notes": "No Tomato"}]
```

## Class
### Orders Class
#### Variables
Each Orders instance has the following instance variables:
1. order_time: private, string data type
2. order_num: private, string data type
3. order_name: private, integer data type
4. order_phone: private, string data type
5. order_cost: private, float data type
6. doubos_num: private, integer data type
7. cheebos_num: private, integer data type
8. hambos_num: private, integer data type
9. double_num: private, integer data type
10. cheese_num: private, integer data type
11. ham_num: private, integer data type
12. fries_num: private, integer data type
13. softdrinks_num: private, integer data type
14. softdrinkm_num: private, integer data type
15. softdrinkl_num: private, integer data type
16. softdrinkxl_num: private, integer data type
17. chocoshakes_num: private, integer data type
18. strawshakes_num: private, integer data type
19. vanishakes_num: private, integer data type
20. order_note: private, string data type


#### Methods
The Orders class has the following methods:
* The dunder "__init__" method
* The dunder "__str__" method

## Auto Testing
Run the following command to test the test_lwang308_ProjectClass.py file. 
There are 1 test cases.

```shell
$ pytest -v test_lwang308_ProjectClass.py
```