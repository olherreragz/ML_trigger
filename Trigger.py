from Process import Regression_process
import pandas as pd
import json


class Trigger:

    # Attributes:
    #   json_path: string
    #   ml_steps: json
    #   process: Process() sub-class

    # Initializer
    def __init__(
        self,
        json_path,
    ):

        "Load and store JSON"
        self.json_path = json_path
        self.ml_steps = self.read_json()

        """
        Initialize one of the three main process
        according to what is required
        """
        if self.regression_type() == 'regression':
            self.process = Regression_process(
                self.ml_steps,
                self.read_data(),
            )

        "Trigger process"
        self.process.trigger_steps()

    "Read JSON and returning it"
    def read_json(
        self,
    ):
        json_with_steps = open(self.json_path)
        json_metadata = json.load(json_with_steps)
        return json_metadata

    "Read data"
    # (method with csv default implemetation)
    def read_data(
        self,
    ):
        return pd.read_csv(
            self.ml_steps["design_state_data"]["session_info"]["dataset"]
        )

    "Read type of regression to be run"
    def regression_type(
        self,
    ):
        return self.ml_steps["design_state_data"]["target"]["type"]
