3dna
====

Generate a printable 3D model from your genome.

![OpenSCAD screenshot](http://wp.me/a2utRQ-rc)


###REQUIREMENTS

*  A chromosome file (3dna was designed using files from 23andme but other sources might be simular?)
*  Python
*  OpenSCAD

###BASIC USAGE

Aquire a genome file (if you use 23andme this can be downloaded from their website).  Then run the following command:

     python 3dna.py genomefile.txt 100 > genome.scad

This will generate a model file that can be opened in OpenSCAD.  Open this file, select "Compile and Render" from the "Design" menu, then select "Export as STL" from the "Design" menu and the resulting STL file can be sliced and printed on the 3d printer of your choice.

###DETAILS

The first argument to the 3dna.py script is the filename of the genome file to process.  

The second argument is the "resolution" to process.  Processing the entire file results in models that are very large and complex.  This parameter lets you reduce the number of points in the genome file that are analized (currently this truncates the data, a better solution would be to average it).

The output of the script is a 3d model in OpenSCAD format.  Later versions of the script may skip this step and go directly to STL, etc. but this intermediary step was found useful in debugging, and provides the user with an opportunity to tweak the output to better suit their particular printer, etc.

###EXAMPLES
In the example directory you can find examples of the output generated by the 3dna.py script in OpenSCAD format, STL files generated from these OpenSCAD files and some photographs of printed output as well (so far only failed attempts due to printer malfunctions...).

I'm working on sourceing a sample genome file to include in the repository, if you know of one please feel free to submit a pull request :)

###TODO
Please post bugs, feature requests, etc. to the Issues list.  There are a number of improvements I'd like to see as well and will tend to as time allows, but again pull requests are appreciated.

