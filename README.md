# ML_trigger

This repository contains code to trigger Machine Learnings steps programatically,  as part of a Screening Test for a DS internship. Steps are automatically triggered from a ```json``` file that contains the details of every step.

The algorithm implements a *"Template method"* design pattern. The superclass of the design pattern, where the procedure framework is defined, is ```Process abstract class``` in ```Process.py```.

## Code execution
___

**The code is executable from console, running ```main.py```.** All sub-processes are triggered from this execution.

Python files, csv files and ```json``` inputs should be in the same directory as ```main.py```.

For further explanation of the code, please read the sections below.

*PD: Code files in GitHub repository are not stored inside of other directories (and therefore, organizing it better) to facilitate testing procedures to evaluators.*

## Code explanation
___

### **```Trigger.py```**

```Trigger class``` contains the **highest abstraction layer for the execution** of the machine learning session. This class stores key attributes, and according to them, it instantiates ```Process abc``` sub-classes for each specific *type of regression to be run*.

#### Details of the class:

- ```Trigger class``` read the json file specified in ```line 5```, ```main.py```.
  - <span style="color: #30a44c
;">**For code execution with other json files, changing the relative path given in this section is needed.</span>**
- After reading the json file, ```Trigger class``` read the ```csv``` file specified in json, as argument parameter for data location.
- Then, ```Trigger class``` read the type of predictive algorithm specified in json (for example, *"Classification"*, *"Clustering"* or *"Regression"*) and the proper process is initialized.
  - Here you can see working the main *"Template method"* placed in. For any given main process, a different sub-class will be initialized.
- Finally, **```Trigger class``` starts the execution of the process initialized**.

### **```Process.py```**

This file contains the abstract class of the *"Template method"* and the sub-classes with the sequence of steps to be applied over the data.

Because only one ```json``` example containing regression steps was given, only one sub-class of ```Process abc``` was implementated. ... it's called ```Regression_process```. <!-- Revisar --> Specific formats of fields that could be given. such as ... filds, are not known.

#### Details of the abstract class:

```Process class``` has methods with **default implamentations that are very likely to never suffer changes**:
  - ```trigger_steps()```: generic instruction to start executing the sequence of steps.
  - ```read_target()```: in supervised learning, a ```Pandas.Series()``` vector to predict will always be uploaded to RAM. However, this functionality it's easily extensible for *"Clustering"* algorithms through overriding.
  - ```feature_handling()```: no matter what the algorithm is, there always will be a phase where features will be processed.

### **```FeatureHandling.py```**

Another *"Template method"* design pattern is placed in to make the code more friendly to read and more friendly to extend to another data types like categorical, timing and boolean variables.

This phase of the process contains several steps that can vary one from another depending if the feature is numerical or textual.

The main class is ```FeatureHandling abstract class```. Aside from other fine details, the entire working ```DataFrame``` is received in the ```__init__()``` method, because of ```missing_values_treatment()``` and ```make_derived_feats()``` sub-processes.
  - If the treatment to apply is to drop all rows with missing values, then this will not only affect the vector of the handled feature, but will affect the entire ```DataFrame```.
  - Also, if ```make_derived_feats()``` generates new features this will affect the entire ```DataFrame``` as well.

The sub-classes implementated are:
  - ```NumericalHandling```
  - ```TextualHandling```

## Assumptions and considerations
___

- It is assumed that the algorithm will provide an automated way to trigger Machine Learning processes *for three main types of predictive algorithms*:
  - Regression
  - Classification
  - Clustering

  In the absence of json examples for "Classification" and "Clustering", the algorithm implements and initialize the process only for "Regressions", but the code it's easily extensible for other types of predictive algorithms.

- Consider that at the inside of the ```json``` file provided, specifically, in the ```algoparams_from_ui.json["design_state_data"]["session_info"]``` dictionary, the following information was given:

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
  For locally testing reasons, this section of the ```json``` file in the Github repository was replaced for ```"iris.csv"```. Nonetheless, for new ```json``` files to be tested, any csv-filename should be read successfully, as long as the ```json``` indicates the csv-filename correctly. The only requirements are:

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
