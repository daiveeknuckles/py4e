"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 

The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 

After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

#create a dictionary to store the values of senders
sender = {}

# find line that starts with 'From' and to pull out all the emails from the line
for line in handle:
    if line.startswith("From:"):
        line = line.split()
        email = line[1]
        sender[email] = sender.get(email,0) + 1
        
 # assign the .items method in the sender dictionary to obtain the largest iteration for email.      
bigsender = None
bigcount = None
for word,count in sender.items():
    if bigcount is None or count > bigcount:
        bigsender = word
        bigcount = count
print(bigsender, bigcount)
        