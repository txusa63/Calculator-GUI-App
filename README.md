# Calculator-GUI-App
A Python Tkinter calculator GUI with tape features for recording calculations.

The app is able to perform the usual operations of addition, subtraction, multiplication, and division, storing the operation and result (ex: 2+3 = 5) on the tape located above the buttons and entry of the calculator. 
The calculations are stored in a local SQLite database stored as a file in the same directory as the project. This allows the calculations to be stored with the project instead of on a SQL database stored in a different computer not accessible to others.

In addition to the above, the user is able to square a value, calculate a percentage, delete a single value (ex: single digit or operator such as +), delete an entire entry (ex: 22+5), and the entire tape with a prompt appearing to verify if the user wishes to continue with the deletion.
The user is able to select a previous calculation for use by selecting the calculation on the tape. The result of the operation will be entered into the entry (ex: the result of 4 from the operation 1+3).

The application is able to detect if wrong operations are performed such as division by zero or if the user enters, for example, 2++5 instead of 2+5 with a window appearing alerting the user of the issue. The user won't be able to execute the operation for storage in the tape until the error is fixed.
