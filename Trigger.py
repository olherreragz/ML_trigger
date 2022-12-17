from Process import (
    Regression_process,
    Classification_process,
    Clustering_process
)
import pandas as pd
import json


class Trigger:

    # Attributes:
    #   ml_steps: json
    #   process: Process() sub-class

    # Initializer
    def __init__(self, json_path):

        "Load and store JSON"
        self.ml_steps = self.read_json(json_path)

        """
        Initialize main process:

        Initialize one of the three possible main processes
        with steps, according to the type of predictive
        algotithm to be run
        """
        if self.read_predicive_algorithm() == 'regression':
            self.process = Regression_process(
                self.ml_steps,  # json with steps details
                self.read_data(),  # pandas.DataFrame
            )
        elif self.read_predicive_algorithm() == 'classification':
            self.process = Classification_process(
                self.ml_steps,
                self.read_data(),
            )
        elif self.read_predicive_algorithm() == 'clustering':
            self.process = Clustering_process(
                self.ml_steps,
                self.read_data(),
            )

        return

    def read_json(self, relative_path):
        json_with_steps = open(relative_path)
        json_metadata = json.load(json_with_steps)
        return json_metadata

    "Read type of regression to be run"
    def read_predicive_algorithm(self):
        return self.ml_steps["design_state_data"]["target"]["type"]

    "Read data"
    # (method with csv default implemetation)
    def read_data(self):
        return pd.read_csv(
            self.ml_steps["design_state_data"]["session_info"]["dataset"]
        )
