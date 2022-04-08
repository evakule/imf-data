import pandas as pd


class BaseTransformer:

    def transform(self, ifs_raw_data):
        pass

    def transform_metadata(self, ifs_metadata):
        pass


class IfsTransformer(BaseTransformer):

    def transform(self, ifs_raw_data):
        df = pd.DataFrame(columns=['indicator', 'time_period', 'value'])
        for i, indicator in enumerate(ifs_raw_data):
            list_to_add = [[]]
            for value in indicator['Obs']:
                try:
                    list_to_add.append(
                        [
                            indicator['@INDICATOR'],
                            value['@TIME_PERIOD'],
                            value['@OBS_VALUE']
                        ]
                    )
                except KeyError:
                    pass
            del list_to_add[0]
            df = df.append(pd.DataFrame(list_to_add, columns=['indicator', 'time_period', 'value']))

        df.reset_index(inplace=True)
        df.drop(['index'], axis=1, inplace=True)
        return df

    def transform_metadata(self, ifs_metadata):
        key_value_list = [[]]
        for indicator in ifs_metadata:
            try:
                key = indicator['ReportedAttribute'][1]['ReportedAttribute'][1]['Value']['#text']
                value = indicator['ReportedAttribute'][1]['ReportedAttribute'][3]['Value']['#text']
                key_value_list.append([key, value])
            except IndexError:
                pass

        return pd.DataFrame(key_value_list, columns=['indicator', 'indicator_full_name'])

