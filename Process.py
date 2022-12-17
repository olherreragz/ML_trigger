from FeatureHandling import (
    NumericalHandling,
    TextHandling,
)
from abc import ABC, abstractmethod


class Process(ABC):

    # Attributes:
    #   ml_steps: dict (json)
    #   df: Pandas.DataFrame()
    #   y_target: Pandas.Series()

    # Initializer
    @abstractmethod
    def __init__(self, ml_steps, data_df):
        self.ml_steps = ml_steps
        self.df = data_df
        return

    "ML steps trigger"
    # @abstractmethod
    def trigger_steps(self):
        "Step 1"
        self.read_target()
        "Step 2"
        self.feature_handling()
        return

    "Step 1: Read the target"
    # @abstractmethod
    def read_target(self):
        # Reading and storing
        self.y_target = self.df[self.ml_steps["design_state_data"]["target"]["target"]]

    "Step 2.0"
    # @abstractmethod
    def feature_handling(self):

        features = set(self.ml_steps["design_state_data"]["feature_handling"].keys())

        # Starting feature handling sub-process
        print("\nRunning Feature Handling\n")

        for feature in features:

            correct_datatype = (
                self.ml_steps["design_state_data"]["feature_handling"][feature][
                    "feature_variable_type"
                    ]
            )

            datatype_read = str(self.df[feature].dtype)

            if correct_datatype == "numerical":
                handler = NumericalHandling(
                    feature,
                    self.ml_steps["design_state_data"]["feature_handling"][feature][
                        "feature_details"
                        ],  # steps details of the handling sub-process
                    self.df,
                    datatype_read,
                )
                self.df = handler.handle()

            elif correct_datatype == "text":
                pass

            # Feature selection

            is_selected = (
                self.ml_steps["design_state_data"]["feature_handling"][feature][
                    "is_selected"
                    ]
            )

            if is_selected:
                pass

        return

    def feature_selection(self):
        pass


class Regression_process(Process):

    # Initializer
    def __init__(
        self,
        *args
    ):
        super().__init__(*args)


class Classification_process(Process):

    # Initializer
    def __init__(
        self,
        *args
    ):
        super().__init__(*args)


class Clustering_process(Process):

    # Initializer
    def __init__(
        self,
        *args
    ):
        super().__init__(*args)
