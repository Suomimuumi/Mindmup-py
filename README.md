# Mindmup-py
This open source Python project allow you to create JSON data trees using Minmup.com. I try to develop this project all the time. But feel free to use :).

This project started at 1/29/2022.

The MindMup-py.exe will work, if you have python already installed in your pc.
The project is 100% open source. So if it doesen't work: you can always code it better by you self :).

How it works:

1. Download MindMup-py.exe. It might warn about virus/troijan. Because i'm not a verified publisher and pepole make viruses with python. So just pass it.
2. In MindMup, go to File -> Download As -> MindMup.
3. Fire up the software.
4. It will ask input for .mup file. So insert the path of your mindmap file.
5. If it can convert the file, enter the path you want to save your new shiny .json file (Remember to enter <filename>.json at the end of the path).
  
 
MindMup format.
  - Currently you can have only 2 parents. for example: "Root->Child->Child's_child", so make sure that every value has maximium of 2 parents.
  - Value should appear at format "<key> = <value>", for example: "Root->Child->Child's_child = alex".
  - If node does not have any children, make sure that it has a value at format: "<key> = <data>".

![This is an image](https://www.linkpicture.com/download.php?filename=Capture_189.png)
