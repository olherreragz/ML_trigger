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
    def __init__(
        self,
        ml_steps,
        data_df,
    ):
        self.ml_steps = ml_steps
        self.df = data_df
        return

    "ML steps trigger"
    # @abstractmethod
    def trigger_steps(
        self,
    ):
        "Step 1"
        self.read_target()
        "Step 2"
        self.feature_handling()
        return

    "Step 1: Read the target"
    # @abstractmethod
    def read_target(self):
        self.y_target = self.df[self.ml_steps["design_state_data"]["target"]["target"]]

    "Step 2.0"
    # @abstractmethod
    def feature_handling(self):

        features = set(self.ml_steps["design_state_data"]["feature_handling"].keys())

        # Starting feature handling sub-process
        print("\nRunning Feature Handling\n")

        for feature in features:

            f_dtype_to_read = (
                self.ml_steps["design_state_data"]["feature_handling"][feature][
                    "feature_variable_type"
                    ]
            )
            f_dtype_read = str(self.df[feature].dtype)

            if f_dtype_to_read == "numerical":
                handler = NumericalHandling(
                    feature,
                    self.df,
                    f_dtype_read,
                    self.ml_steps["design_state_data"]["feature_handling"][feature][
                        "feature_details"
                        ],
                )
                self.df = handler.handle()

            elif f_dtype_to_read == "text":
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
