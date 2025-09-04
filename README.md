# PointCloudDataAnalysis

This is a repository containing code and results and figures obtained via the code for the following:

- Eye-tracking Data Analysis

- Machine Learning Models trained on QoE Data

- ITU-T P.1203 Model fine-tuned on QoE Data

The eye-tracking and QoE data is obtained from our experiments detailed in the following papers:

`Nguyen, M., Vats, S., Van Damme, S., Van Der Hooft, J., Vega, M. T., Wauters, T., ... & Hellwagner, H. (2023, June). Impact of Quality and Distance on the Perception of Point Clouds in Mixed Reality. In 2023 15th International Conference on Quality of Multimedia Experience (QoMEX) (pp. 87-90). IEEE.`

`Nguyen, M., Vats, S., Van Damme, S., van der Hooft, J., Vega, M. T., Wauters, T., ... & Hellwagner, H. (2023). Characterization of the Quality of Experience and Immersion of Point Cloud Videos in Augmented Reality through a Subjective Study. IEEE Access, 11, 128898-128910.`

`Nguyen, M., Vats, S., Zhou, X., Viola, I., Cesar, P., Timmerer, C., & Hellwagner, H. (2024, April). ComPEQ-MR: Compressed Point Cloud Dataset with Eye Tracking and Quality Assessment in Mixed Reality. In Proceedings of the 15th ACM Multimedia Systems Conference (pp. 367-373).`

## Repository Structure

`_Eye_Tracking` contains the gaze data in the form of JSON files, the code in the form of a Jupyter notebook, and the results from the code. The results are saved as both PDF and PNGs. The code is analysing the gaze data to obtain head and gaze movement velocities per second for the user and plot the data in various forms as deemed necessary.

`_ML_Models` also contains the code, the figures, and the results regarding the ML models. The code trains various ML models on our MOS data obtained from our subjective tests. The data is separated per-codec where applicable.

`_P1203` has the code for fine-tuning the ITU-T P.1203 model's mode 0 using the MOS data from our subjective testing rounds. The `.txt` files contain the results from the various optimization techniques. The final fine-tuned coefficients are also detailed in the Jupyter notebook. There are also template JSON files provided for filling with our point cloud video metadata when training the P.1203 model.

`_point_cloud_data` folder contains various informations regarding our point clouds, such as the PSNR values, the bitstream files, and the participants scores from our subjective tests. Our old code, as well as code for generating figures relating to the MOS data are also available. The figures obtained from the data are also present.

## Running the Code

This code is meant to be run on Linux or in a WSL environment, using Python 3.10.12.

You can replace the data in the `_point_cloud_data` folder with your own data. Be sure to adjust the filepaths to the data files accordingly. Also be sure you're using the correct units for the bitrates. Check the notes at the top of the `.ipynb` files for the same.

You might need to downgrade the `numpy` version if you get errors with installing `matplotlib` or `seaborn`.

## Citing

If using this code then please cite the following work (WIP, to be updated when the article is published):

```
@ARTICLE{,
  author={Vats, Shivi and Nguyen, Minh and Timmerer, Christian and Hellwagner, Hermann}, 
  title={{Eye-Tracking, Quality Assessment, and QoE Prediction Models for Point Cloud Videos: ComPEQ-MR Dataset Analysis}}, 
  year={2025},
}
```
