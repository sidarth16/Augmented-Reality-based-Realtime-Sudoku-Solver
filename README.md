# Augmented-Reality-based-Realtime-Sudoku-Solver
An AR program, which reads the Sudoku problem from webcam feed and using computer vision techniques digitize the image through CNN approach , then solves, displays the solution in the same perspective of the input feed , thus implementing Augmented reality

<img width="537" alt="sudoku_thumb" src="https://user-images.githubusercontent.com/38394431/84931343-4be28f00-b0f0-11ea-9279-c3c7e7cdbbf8.PNG">

# Directions to run the program
* Firstly make sure u have all the required libs installed from the *requirements.txt* 
* Traverse your terminal to this folder location.
* Then , In your terminal type **python sudoku_main.py** and hit enter 
<br/>
# Workflow of prog :
<br/>
## 1) Input:
![input](https://user-images.githubusercontent.com/38394431/85228274-35924700-b400-11ea-85ab-11285e401f45.JPG)

its the input raw_img passes to the system through the cam feed
<br/><br/>
## 2) Extract and Thresholding sudoku:
![thresh](https://user-images.githubusercontent.com/38394431/85227888-b4d24b80-b3fd-11ea-9a26-7e70a1161926.jpg)
<br/>Here the sudoku is extracted , warped and thesholded from the raw_image . </br>
<br/><br/>
## 3) grid-extraction and number prediction:
![ext_pred](https://user-images.githubusercontent.com/38394431/85227770-f57d9500-b3fc-11ea-8a45-ba01e73d395a.JPG)
<br/>Here ,<br/> 
* the left image is collection of all extracted number-img-grids collaged together.
* the right image is collection of all predicted numbers of the respective grids by the CNN model
<br/><br/>
## 4) Solving and updating the sudoku:
![solved](https://user-images.githubusercontent.com/38394431/85227977-417d0980-b3fe-11ea-87f7-c74c157a198a.jpg)
<br/>After solving , the cropped and warped sudoku is updated with solution.
<br/><br/>
## 5) Final Output Image:
![output](https://user-images.githubusercontent.com/38394431/85228014-7be6a680-b3fe-11ea-81a1-44190f1e6d04.JPG)
<br/>Here , the solved-cropped sudoku is warped_inversed to the original image in the same perspective 
<br/><br/>





