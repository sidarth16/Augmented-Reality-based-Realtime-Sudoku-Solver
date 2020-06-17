from __future__ import print_function
import cv2
import numpy as  np
from neural_model import NeuralModel
from sudoku_tools import *

cap = cv2.VideoCapture(0)
cv2.startWindowThread()

# Loading our neuralModel
NeuralModel.instance()
required_num_in_sol="123456789"
try:
    while True:
        _, img = cap.read()

        img_shape = img.shape
        output_shape = (img_shape[1] , img_shape[0])

        #check for a valid box corners
        corners = get_sudoku_box(img , draw_contours=True)
        if corners is not None:

            cropped_sudoku , sudoku_crop_thresh , extracted_digits ,predicted_unsolved_grid, img_cropped_sudoku , img_final , sudoku = sudoku_main(img , corners , required_num_in_sol=required_num_in_sol)


            #creating collage of cropped_thresholded_input_sudoku and solved_cropped_sudoku
            div  = np.zeros((250,25),np.float64)
            div.fill(255)
            input_sudoku = extracted_digits
            input_sudoku = cv2.resize(input_sudoku, (250, 250))
            pred_sudoku = predicted_input_grid(sudoku)
            pred_sudoku = cv2.resize(pred_sudoku, (250, 250))
            extracted_predicted = np.hstack(( input_sudoku  ,div/255 ,pred_sudoku.astype(np.float64)/255.0))

            #creating collage of preprocessed_extracted_grids and respective grid with the predicted number
            div  = np.zeros((250,25,3),np.float64)
            div.fill(255)
            sudoku_crop_thresh = cv2.resize(sudoku_crop_thresh, (250, 250))
            sudoku_crop_thresh_rgb = cv2.merge([sudoku_crop_thresh,sudoku_crop_thresh,sudoku_crop_thresh])
            img_cropped_sudoku = cv2.resize(img_cropped_sudoku, (250, 250)).astype(np.float64)/255.0
            sudoku_steps = np.hstack((sudoku_crop_thresh_rgb , div.astype(np.float64)/255.0 ,img_cropped_sudoku ))
            
            #to prevent unwanted predictions when no sudoku present
            zero_count=0
            for i in range(9):
                for j in range (9):
                    if(sudoku.grid[i,j].number==0):
                        zero_count = zero_count + 1
            if zero_count > 75:
                img_final = img.copy()

            #cv2.imshow("input", img)
            cv2.imshow("extracted__vs__predicted", extracted_predicted)
            cv2.imshow("sudoku_steps", sudoku_steps)
            cv2.imshow("img_final", img_final)


            key = cv2.waitKey(10)
            if key == 27:
                break
            elif (key in range(49,58)):
                print(chr(key)+" pressed")
                print("\tShowing instances of only "+chr(key)+" from the solution")
                if(required_num_in_sol=="123456789"):
                    required_num_in_sol=""
                required_num_in_sol = required_num_in_sol+chr(key)
            elif key==120:
                required_num_in_sol=""
            elif key==97:
                required_num_in_sol="123456789"
        else:
            img_final = img 
            cv2.imshow("img_final", img_final)
            key = cv2.waitKey(1)
            if key == 27:
                break
            if (key in range(49,58)):
                print("Showing instances of only "+chr(key)+" from the solution")
                required_num_in_sol = required_num_in_sol+chr(key)

finally:
    cv2.destroyAllWindows()
    cap.release()
