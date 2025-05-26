import os 
from mlProject import logger 
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir,sep=";")
            data_cols = set(col.strip().lower() for col in data.columns)
            schema_cols = set(col.strip().lower() for col in self.config.all_schema.keys())

            print("Data columns:", data_cols)
            print("Schema columns:", schema_cols)
            print("Difference (data - schema):", data_cols - schema_cols)
            print("Difference (schema - data):", schema_cols - data_cols)

            validation_status = data_cols == schema_cols

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e