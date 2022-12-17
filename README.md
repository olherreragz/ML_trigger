# ML_trigger

This repository contains code to trigger Machine Learnings steps programatically, in an automated way from a ```json``` file, as part of a Screening Test for a DS internship.

The algorithm implements a *"Template method"* design pattern. The superclass, where the skeleton for the whole procedure is defined, is ```Process abstract class``` in ```Process.py```.

## Code execution
___

**The code is executable from console, running ```main.py```.** All processes are triggered with this execution.

Python files, csv files and ```json``` inputs should be in the same directory as ```main.py```.

In the GitHub repository, files are not stored in other directories (and therefore, organizing it better) to facilitate testing procedures to evaluators. 

For further explanation of the code, please read the sections below.

## Code explanation
___

### **```Trigger.py```**

```Trigger class``` contains the whole process. It stores key attributes and instantiates ```Process class``` sub-classes, according *to the type of regression to be run*.

#### Explanation of the class:

- ```Trigger class``` read the json file specified in line ```line 5```  of ```main.py```.
  - If you want to try execution of the code with another json file, you just have to change the relative path given in this line.
- After reading the json file, the ```Trigger class``` read the ```csv``` file specified in json as argument parameter.
- Then, ```Trigger class``` read the type of predictive algorithm specified in the json (for example, *"Classification"*, *"Clustering"* or *"Regression"*) and it initializes the proper processes.
  - Her, you can see working the main *"Template method"* placed in. For any given main process, a different sub-class will be initialized.
- Finally, **```Trigger class``` triggers the execution of process initialized** in the previous phase.

### **```Process.py```**

This file contains the abstract class of the *"Template method"* and the sub-classes that implamentates the sequence of steps to be applied over the data.

Because only one ```json``` example containing regression steps was given, only a sub-class for regressions, called ```Regression_process```, was implementated (we don't know what specific formats will be given in ```json``` x, y, z fields).

The ```Process class``` has methods with **default implamentations that are very likely to never suffer changes**:
  - ```trigger_steps()```: generic instruction to start executing a sequence of steps that won't change. Is the actions inside every step what it's very likely to change according to the type of algorithm running.
  - ```read_target()```: in supervised learning, a ```Pandas.Series()``` vector to predict will always be uploaded to RAM through this method. However, this functionality it's easily extensible for *"Clustering"* algorithms through overriding  in a ```Clustering_process sub-class```.
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
