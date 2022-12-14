# ML_trigger

This repository contains code to trigger Machine Learnings steps programatically,  as part of a Screening Test for a DS internship. Steps are automatically triggered from a ```json``` file that contains the details of every step.

The algorithm implements a *"Template method"* design pattern. The super-class of the design pattern, where the framework for the whole procedure is defined, is ```Process abstract class``` in ```Process.py```.

## Code execution
___

**The code is executable from console, running ```main.py```.** All sub-processes are triggered from this execution.

Python files, csv files and ```json``` inputs should be in the same directory as ```main.py```.

For further explanation of the code, please read the sections below.

*PD: Code files in GitHub repository are not stored inside of other directories (and therefore, organizing it better) to facilitate testing procedures to evaluators.*

## Code explanation
___

### **```Trigger.py```**

```Trigger class``` is the **highest abstraction layer** for the execution of the session. This class stores key attributes, and according to them, it instantiates ```Process abc``` sub-classes for each specific *type of regression to be run*.

#### Details of the class:

- ```Trigger class``` read the json file specified in ```line 5```, ```main.py```.
  - <span style="color: #30a44c
;">**For code execution with other json files, relative path change is needed in this section.</span>**
- After reading the json file, ```Trigger class``` read the csv file specified as json argument for data location.
- After reading the csv, ```Trigger class``` read the type of predictive algorithm specified in json. For example, *"Classification"*, *"Clustering"* or *"Regression"*. Then, the appropiate process is initialized.
  - The main *"Template method"* placed in, starts working. For any given main process, a different sub-class will be initialized.
- Finally, **```Trigger class``` starts the execution of the predictive algorithm**.

### **```Process.py```**

This file implements the *"Template Method"* abstract class and its sub-classes that contain the sequence of steps to be applied to the data.

Only one ```json``` example was provided that contained regression steps. Therefore, only one of the three sub-classes of ```Process abc``` was implemented. Specifically, the ```Regression_process``` sub-class.

<!-- Revisar -->
This is because specific formats that might be given for certain json values, are unknown. For example, ```optomize_model_hyperparameters_for```, ```optimize_threshold_for``` and ```model_name```, are not parameter arguments of any function of the ```scikit-learn``` library. Therefore, it is assumed that they correspond to organization-specific parameters.

#### Details of the abstract class:

```Process class``` has methods with **default implamentations that are very likely to never suffer changes**:
  - ```trigger_steps()```: generic instruction to start executing steps.
  - ```read_target()```: in supervised learning, a ```Pandas.Series()``` vector to predict will always be uploaded to RAM. However, this functionality it's easily extensible for *"Clustering"* algorithms through overriding.
  - ```feature_handling()```: phase where features will be manipulated.

### **```FeatureHandling.py```**

<!-- Revisar -->

Each attribute must be handled. This is delegated to ```FeatureHandling class```, implemented in this file.

This phase of the process contains several steps that can vary depending if the feature is numerical or textual. Another *"Template method"* design pattern was placed in to separate the different types of sub-processes and to make the code more easily extensible for other data types. For example, categorical, timing and boolean variables.

The main class is ```FeatureHandling abstract class```. The sub-classes of the *"template method"* implemented are:
  - ```NumericalHandling```
  - ```TextualHandling```

In addition to other fine details, the entire data frame is received in the initializer method due to implications of ```missing_values_treatment()``` and ```make_derived_feats()``` numerical sub-processes.
  - If the missing values treatment to apply is to drop rows, then this will not only affect the vector of the handled feature, but will affect vectors of the entire ```DataFrame```.
  - Also, if ```make_derived_feats()``` generates new features this will affect the entire ```DataFrame``` as well.

Consequently, for each feature sub-process the whole dataframe must be treated.


## General assumptions and considerations
___

- It is assumed that the algorithm will provide an automated way to trigger Machine Learning processes *for three main types of predictive algorithms*:
  - Regression
  - Classification
  - Clustering

  As mentioned before, in the absence of json examples for "Classification" and "Clustering", the code implements and initialize the process only for "Regressions", but the code it's easily extensible for other types of predictive algorithms.

- Consider that at the inside of the json file provided, in the ```algoparams_from_ui.json["design_state_data"]["session_info"]``` node, the following information was given:

  ```
      "session_info" : {
        "project_id": "1",
        "experiment_id": "kkkk-11",
        "dataset":"iris_modified.csv",
        "session_name": "test",
        "session_description": "test"
        },
  ```

  However, no ```iris_modified.csv``` file was provided.

  <!-- Revisar -->
  For locally testing reasons, this section of the json file was replaced for ```"iris.csv"```. The json in the Github repository corresponds to this version.
  
  Nonetheless, for new json files to be tested, any csv-filename should be read successfully. The only requirements are:

  - Locally, the ```.csv``` extension file exists and it's stored in the same directory as the code.
  - **It is assumed that the ```json``` will always handle over a relative path,** with its root placed in the same directory where the code is stored.

## Dependencies
___

- External libraries:
  - ```numpy```
  - ```pandas```
- Built-in functions:
  - ```ABC```
  - ```json```
