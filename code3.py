# Option #2 for making tables in Flink API - SQL / Database Language

# Import necessary libraries from pyflink.table package
from pyflink.table import EnvironmentSettings, TableEnvironment

# Initialize the environment settings in streaming mode
env_settings = EnvironmentSettings.in_streaming_mode()

# Create a streaming table environment using the settings
table_env = TableEnvironment.create(env_settings)
table_env.execute_sql("""
    CREATE TABLE random_source (
        id BIGINT, 
        data TINYINT 
    ) WITH (
        'connector' = 'datagen',
        'fields.id.kind'='sequence',
        'fields.id.start'='1',
        'fields.id.end'='3',
        'fields.data.kind'='sequence',
        'fields.data.start'='4',
        'fields.data.end'='6'
    )
""")

#  Unlike previous tables, there is a column, "op"
#  Operation Type, +I represents an insertion, -D represents a deletion
# This is default from anytime "datagen" is used as connector

# Data Generator - make synthetic data, for id and string
# In this case, it's sequence for both ID and data, from 1-3 for id, and for 4-6 for sequence

# Retrieve the "random_source" table from the table environment
table = table_env.from_path("random_source")

# Execute the table operation and display the results
table.execute().print()
