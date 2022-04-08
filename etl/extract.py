import requests


class BaseExtractor:

    def extract(self,  frequency='Q', country='AE'):
        pass


class MetadataBaseExtractor:

    def extract_metadata(self,  frequency='Q', country='AE'):
        pass


class IFSExtractor(BaseExtractor, MetadataBaseExtractor):

    def __init__(self):
        self.url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'

    def extract(self, frequency='Q', country='AE'):
        key = f'CompactData/IFS/{frequency}.{country}'
        return requests.get(f'{self.url}{key}').json()['CompactData']['DataSet']['Series']

    def extract_metadata(self, frequency='Q', country='AE'):
        key = f'GenericMetadata/IFS/{frequency}.{country}'
        return requests.get(f'{self.url}{key}').json()['GenericMetadata']['MetadataSet']['AttributeValueSet']

