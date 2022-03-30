# BREAST CANCER

Description of the dataset
-------

The dataset contains the 569 observations of patients with a tumor. The characteristics includes the metrics of the tumor and label describing if the tumor is beningn or malign

-------

Questions
------

- What metrics are going to be used to measure the performance of the model?
  
All the metrics are important in the medical field due we are handling with diagnosis of
a all kinds of pathologies. In the case of tumor detections, as the goal is to minimize false
positives, the Precision is the main metric and the one that we want to optimize in the model.
The sensitivity is also very important as it will measure the probability that a classification
is correct.

Also, the F1 score is the metric in the case we want to avoid false negatives and false positives

- Metrics


ref:
  * https://www.analyticsvidhya.com/blog/2020/11/a-tour-of-evaluation-metrics-for-machine-learning/
  * https://www.sciencedirect.com/science/article/pii/S2001037014000464
  * https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234
  * https://www.intechopen.com/chapters/72044

- Justificación de las métrica de evaluación

En este proyecto se utilizarán las métricas de Accuracy, Sensitivity y Specificity debido a que
proyectos como [Syantra](https://www.syantra.com/for-healthcare-providers#:~:text=Syantra%20DX%20%7C%20Breast%20Cancer%20is%20an%20advanced%2C%20innovative%20precision%20medicine,early%20stages%2C%20before%20it%20spreads) de detección de cancer de mama usan estas mismas
métricas para evaluar su desempeño, por lo tanto sirven como punto de comparación.