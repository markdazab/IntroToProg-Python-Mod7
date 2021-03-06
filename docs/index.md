## Assignment Info
Mark Daza   
March 1st, 2022 
Foundations of Programming  
Assignment07  
https://github.com/markdazab/IntroToProg-Python-Mod7

# Assignment07

## Introduction
This document will record the steps that I took in performing Assignment07. Briefly, for this first assignment, 
we wrote a python script demonstrating how Pickling and Structured error handling work.  

## Process
After completing tasks 1-2, I started working on this week’s assignment script. Steps 2 and 3 included searching the web for examples
of exception and pickling features. I went through a couple of pages like docs.python.org, programiz.com, and w3schools.com, and they 
reinforced what we learned in this week’s lecture. Once that was completed, I felt prepared to work on this week’s assignment. Initially, 
I wanted to keep things simple and do an example of pickling by writing two variables into a list and then writing these objects into a byte stream. 
Then the error handling would be a separate part where using a try statement combined with an except clause to handle an exception. 
However, I wanted to challenge myself a little bit for this assignment and decided to combine these two functions as much as possible. 

My first step was to work on a function to write and read data in binary format. Using Randal’s example from his notes, I quickly stored the data with 
the pickle.dump method and read the data back with the pickle.load method. (Figure 1)

![Figure 1](https://github.com/markdazab/IntroToProg-Python-Mod7/blob/main/Figures/Figure1.png "Figure1")  
Figure1. Script for writing data in binary format and reading data from binary file

Next, I started a try statement with an except clause. Like in previous assignments, I created a variable requiring the user’s input to get a value 
for a task. Using an if statement, I started a custom condition to raise an error if a task was not entered. Next, I made a variable requiring the 
user’s input to get a value for a priority and immediately converted it to an integer with the int() function. I knew that any value, not an integer, 
would trigger a ValueError, so there was no need to use a custom condition here. And ended this block of code by creating a list containing both variables 
created before. (Figure 2). 

![Figure 2](https://github.com/markdazab/IntroToProg-Python-Mod7/blob/main/Figures/Figure2.png "Figure2")  
Figure 2. Scrip for user input, with the custom condition and list creation

Next, using the except clause, I captured any exceptions caused by the user’s input. This would catch any exception triggered by my custom clause or a 
ValueError. I purposefully kept it broad instead of using a specific exception type, just in case. (Figure 3). 

![Figure 3](https://github.com/markdazab/IntroToProg-Python-Mod7/blob/main/Figures/Figure3.png "Figure3")  
Figure 3. Scrip for except clause

Lastly, I decided to implement a try statement to capture any exceptions potentially caused by the pickle.dump method or pickle.load method such as  IOError
or NameError. (Figure 4)

![Figure 4](https://github.com/markdazab/IntroToProg-Python-Mod7/blob/main/Figures/Figure4.png "Figure4")  
Figure 4. Scrip for write_data_to_file function

# Summary
This week’s assignment was challenging because it differed from all previous weeks. I thrive when provided with a clear expectation, and when left to figure
out my goal on my own, I tend to overthink a lot. For example, for this week’s assignment, I pictured my code including a loop have a user to re-enter a 
value for the variables if an exception was raised. I spent hours working on this, failing to make it work I decided to go with what I described in this 
document. I have to admit that it was a great learning experience but ultimately understood that I should try to master the fundamentals first before I 
take on my complicated code. Below are the screenshots of the script running both in PyCharm. (Figure 5)

![Figure 5](https://github.com/markdazab/IntroToProg-Python-Mod7/blob/main/Figures/Figure5.png "Figure5")  
Figure 5. Screenshot of final script for Assignment07 running on PyCharm and Demo.dat file.
