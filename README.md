# Documentation

#### Overview

This module is created to do one thing: count the number of words within a text file and spit out the ten most common occurrences.  

This is a single python file that is run from the command line. The arguments to the command line call is the **relative** path to the text file to analyse. 

The reason I used a class based method as well as developing some methods that aren't technically required for this is because software typically is not written once and needs to be extended. With this OOP design, this tiny program fulfils the task now as well as can be extended to do additional functionality later. 

**Assumptions Made**

Since no specification was made for what happens when there are the same number of occurrences (Example. "Wow " occurs twice, "Hello" occurs twice, which is returned as Top 10?). Currently this is done randomly through selecting top 10 after sorting by value within `getTopOccurrences`.

#### Usage 

Run the included `word_counter.py` file:

`./word_counter.py textFileToRead.txt`

This should give you the output of:

```Number of Words: N

Number of Words: N
Top 10 Words:
1. Example
2. Words
...
10. Last 

```

Where N is # of words within text file. 

#### Testing 

In order to run the tests please run the file `tests.py` within the directory.



