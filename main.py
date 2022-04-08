import pandas as pd

from etl.extract import IFSExtractor
from etl.transform import IfsTransformer


ifs_extractor = IFSExtractor()
ifs_transformer = IfsTransformer()

ifs_source_data = ifs_extractor.extract()
ifs_metadata = ifs_extractor.extract_metadata()

ifs_transformed_data = ifs_transformer.transform(ifs_source_data)
ifs_transformed_metadata = ifs_transformer.transform_metadata(ifs_metadata)

result_df = pd.merge(left=ifs_transformed_data,
                     right=ifs_transformed_metadata,
                     how='left',
                     left_on='indicator',
                     right_on='indicator')

result_df.to_csv('result.csv')

