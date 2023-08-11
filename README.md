To generate parallel datasets for low-resource languages follow the instructions:

1) Download UIPath studio.
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
   -> Then double-click on the URL and change the 'sl' and 'tl' values to your desired languages.
