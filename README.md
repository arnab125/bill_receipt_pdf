# Restaurant Bill Receipt Generator

This is a simple program that generates a receipt for a restaurant bill. It is written in Python 3.7.3.

## Getting Started
1. Clone the repository
```
$ git clone https://github.com/arnab125/bill_receipt_pdf.git
```

2. Install the required libraries
```
$ pip install -r requirements.txt
```

3. Run the script
```
$ python main.py
```

4. Enter the required inputs.
5. Input format:
```
1.No. of items
 for (no. of items) times:
    i. Food code
    ii. Food Name
    iii. Food quantity
    
 # For more information, refer to the sample input file.
```
   
5. The receipt will be generated in the same directory as the script.
6. The receipt will be named as `bill.pdf`.



## Prerequisites
- Python 3.6 or above
- reportlab, os and datetime python libraries.


## Built With
- Python 3.6
- Reportlab - PDF library for Python
- os - OS library for file and directory operations.
- datetime - Datetime library for python.


## Notes
- The receipt is generated in A4 size.
- The receipt is generated in PDF format.





## Sample Pdf Generated
<embed src="https://github.com/arnab125/bill_receipt_pdf/blob/main/bill.pdf" width="500" height="375" type='application/pdf'>
