# Instructions to generate parallel datasets for low-resource languages.

1) Download the UIPath Studio and its browser extension. Enable the extension in your browser.
2) Download the ParallelCorpus.zip from the static directory.
3) Unzip it and place it in the UIPath directory(Path given during installation).
4) Collect the English sentences you want to use for training, and add them to a text file.
   Sentences should be separated by '\n' and a '$' key should be used after every 5000
   characters because of the limits.
5) After following the preprocessing in step-4, name the text file as input and replace it with
   the input.txt file in the ParallelCorpus directory.
6) Now open the UIPath studio and you can find the process named ParallelCorpus. Click on it
   and then click on the "open main workflow" dialogue.
7) You can now run the automation by clicking the "Debug file" button on the top left and then
   selecting "Run File".
8) The default source and target languages are English and Hindi. To change them, follow these
   steps:
   -> Scroll down until you see the "Browser URL" element.
   -> Then double-click on the URL and change the 'sl' and 'tl' values to your desired language codes.
9) The parallel dataset for your language can be found in the output.txt file. Execution time depends on the size of the input file. You can monitor the progress with the help of the count.txt file which stores the number of sentences processed.
10) Below are sample input and output files for your reference.

Sample Input

![image](https://github.com/PrudhvirajuChekuri/NeuralMachineTranslator/assets/96725900/c1891372-f338-42f3-be74-3bdac8ed5647)

Sample Output

![image](https://github.com/PrudhvirajuChekuri/NeuralMachineTranslator/assets/96725900/cda52f75-d06b-4db8-a430-ef520e007380)
