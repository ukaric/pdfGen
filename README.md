## pdfGen - JPG to PDF generator.

A python script that compiles all of your properly formatted JPGs to categorised PDFs.

#### Rules
In order for script to work follow these simple rules: 
Folder path __needs__ to end with __\__
The images are supposed to be formated like: 

numb1-any number
numb1-any number
numb2-any number

ex.

233564-01
233564-02
200007-01
200007-02
200008-03

A folder containing JPGs formatted like that will output you with two PDF files, the first one beeing, '233564.pdf', containig all of the images with the
name prefix 233564, in this case '233564-01.jpg', 233564-02.jpg', and the second '200008.pdf' containing '200007-01', '200007-02',
'200008-03'.