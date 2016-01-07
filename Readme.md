# Online-Handwritten George Washington Dataset

The [George Washington dataset] is a very popular collection of scanned pages of handwritten letters from George Washington and his affiliates. More specifically, data from Series 2, Letterbook 1, pages 270-279 and 300-309 is often used in word spotting experiments (see also [Fischer et al.]). I needed to have an online-handwritten version of those pages and since no such dataset was available, I created one myself.

### Format
You will find a subfolder for each of the 20 pages of the original George Washington dataset. There is a text file for each single word (words that are split by a return are usually also split into two text files). The first line in each file contains the string representation of the word. The other lines each contain a single point and have the format
```
x<space>y<space>pen-state
```
where
 - x and y are the coordinates of the point in the coordinate system with the origin in the bottom left corner and the y-axis growing upwards
 - pen-state tells whether the pen stayed on the writing surface after creating the point (0) or was lifted up (1).

The render.py tool will render a given trajectory using numpy and matplotlib.

Terms of Use
----

This dataset may only be used for non-commercial research and educational purposes. Use the following paper as citation in your scientific work:

Christian Wieprecht, Leonard Rothacker, Gernot A. Fink, "Word Spotting in Historical Document Collections with Online-Handwritten Queries", In Proc. IAPR Int. Workshop on Document Analysis Systems, Santorini, Greece, 2016

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [George Washington dataset]: <http://memory.loc.gov/ammem/gwhtml/>

   [Fisher et al.] <http://www.iam.unibe.ch/fki/databases/iam-historical-document-database/washington-database>


