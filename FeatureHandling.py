from abc import ABC, abstractmethod


class FeatureHandling(ABC):

    # Attributes:
    #   details: dict
    #   feature: string
    #   data: Pandas.Series()
    #   f_dtype_read: string

    # Initializer
    @abstractmethod
    def __init__(
        self,
        feature,
        data,
        f_dtype_read,
        details,
    ):
        self.feature = feature
        self.data = data
        self.f_dtype_read = f_dtype_read
        self.details = details
        self.datatype_checking()

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
        self.missing_values_treatment()
        self.numerical_handling()
        self.rescaling()
        self.make_derived_feats()
        return self.data

    "Correct datatype validation"
    def datatype_checking(self):
        if ('float' in self.f_dtype_read or
                'int' in self.f_dtype_read):
            print(f"correct format read for: {self.feature}")
        else:
            print("incorrect format read")
            self.data[self.feature] = self.data[self.feature].astype('float64')
            print(f"format corrected for: {self.feature}")

    def missing_values_treatment(self):
        treatment = self.details["missing_values"]
        impute_with = self.details["impute_with"]

        if treatment == 'Impute' and impute_with == "Average of values":
            print(f"Executing missing value imputation for: {self.feature}")
            self.data[self.feature] = self.data[self.feature].fillna(
                self.data[self.feature].mean()
                )

        elif treatment == 'Impute' and impute_with == "custom":
            print(f"Executing missing value imputation for: {self.feature}")
            impute_value = self.details["impute_value"]
            self.data[self.feature] = self.data[self.feature].fillna(impute_value)

    def numerical_handling(self):
        numerical_handling = self.details["numerical_handling"]
        if numerical_handling == "Keep as regular numerical feature":
            pass

    def rescaling(self):
        rescaling = self.details["rescaling"]
        if rescaling == "No rescaling":
            pass

    def make_derived_feats(self):
        make_derived_feats = self.details["make_derived_feats"]
        if not make_derived_feats:
            pass


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
        if self.f_dtype_read == 'object':
            print(f"correct format read for: {self.feature}")
        else:
            print("incorrect format read")
            self.data[self.feature] = self.data[self.feature].astype('object')
            print(f"format corrected for: {self.feature}")
