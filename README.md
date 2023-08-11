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

## Sample Input
![image](https://github.com/PrudhvirajuChekuri/NeuralMachineTranslator/assets/96725900/6b18ae6c-de26-4c7d-9fe7-5b8a9b9cc711)

## Sample Output
![image](https://github.com/PrudhvirajuChekuri/NeuralMachineTranslator/assets/96725900/42a70dac-cb83-4ca6-b073-dfd94a9356f8)
