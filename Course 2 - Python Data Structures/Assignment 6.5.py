"""
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 

Convert the extracted value to a floating point number and print it out.
"""

text = "X-DSPAM-Confidence:    0.8475"

# Using the find() method, slice the text and find the index position that has "0".  
# Set up a varible to host the sliced text. 

x = text.find("0")       
y = float(text[x:])    #convert the result to a float
print(y)
