from abc import ABC, abstractmethod


class FeatureHandling(ABC):

    # Attributes:
    #   feature: string
    #   details: dict
    #   data: Pandas.Series()
    #   feature_data_type_read: string

    # Initializer
    @abstractmethod
    def __init__(self, feature, details, data, feature_data_type_read):
        self.feature = feature
        self.details = details
        self.data = data
        self.feature_data_type_read = feature_data_type_read

    @abstractmethod
    def datatype_checking(self):
        return


class NumericalHandling(FeatureHandling):

    # Initializer
    def __init__(
        self,
        *args
    ):
        super().__init__(*args)

    "Trigger of the sub-process"
    def handle(self):
        self.datatype_checking()
        self.missing_values_treatment()
        self.numerical_handling()
        self.rescaling()
        self.make_derived_feats()
        return self.data

    "Correct datatype validation"
    def datatype_checking(self):
        if ('float' in self.feature_data_type_read or
                'int' in self.feature_data_type_read):
            print(f"correct format read for: {self.feature}")  # Revisar
        else:
            print("incorrect format read")
            self.data[self.feature] = self.data[self.feature].astype('float64')
            print(f"format corrected for: {self.feature}")
        return

    def missing_values_treatment(self):
        treatment = self.details["missing_values"]
        impute_with = self.details["impute_with"]

        if treatment == 'Impute' and impute_with == "Average of values":
            self.data[self.feature] = self.data[self.feature].fillna(
                self.data[self.feature].mean()
                )
            print(f"Missing value imputation executed for: {self.feature}")

        elif treatment == 'Impute' and impute_with == "custom":
            # Revisar y probablemente, cambiar
            impute_value = self.details["impute_value"]
            self.data[self.feature] = self.data[self.feature].fillna(impute_value)
            print(f"Missing value imputation executed for: {self.feature}")
        return

    def numerical_handling(self):
        numerical_handling = self.details["numerical_handling"]
        if numerical_handling == "Keep as regular numerical feature":
            pass
        return

    def rescaling(self):
        rescaling = self.details["rescaling"]
        if rescaling == "No rescaling":
            pass
        return

    def make_derived_feats(self):
        make_derived_feats = self.details["make_derived_feats"]
        if not make_derived_feats:
            pass
        return


class TextHandling(FeatureHandling):

    # Initializer
    def __init__(
        self,
        *args
    ):
        super().__init__(*args)
        return

    "Correct datatype validation"
    def datatype_checking(self):
        if self.feature_data_type_read == 'object':
            print(f"correct format read for: {self.feature}")  # Revisar
        else:
            print("incorrect format read")
            self.data[self.feature] = self.data[self.feature].astype('object')
            print(f"format corrected for: {self.feature}")
        return
