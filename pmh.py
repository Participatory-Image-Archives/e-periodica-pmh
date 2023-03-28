import pandas as pd  
from polymatheia.data.reader import OAIRecordReader            # read one metadata record from OAI

# e-periodica OAI-PMH Endpoint
oai = 'https://www.e-periodica.ch/oai'

# All records that have the DDC:390 (Ethnology, Fokflore) Set
reader = OAIRecordReader(oai, metadata_prefix='oai_dc', set_spec='ddc:390')

# Make lists from Dublin Core elements
creators = [record.get(['metadata', '{http://www.openarchives.org/OAI/2.0/oai_dc/}dc', 'dc_creator', '_text']) \
            for record in reader]
titles = [record.get(['metadata', '{http://www.openarchives.org/OAI/2.0/oai_dc/}dc', 'dc_title', '_text']) \
            for record in reader]
publishers = [record.get(['metadata', '{http://www.openarchives.org/OAI/2.0/oai_dc/}dc', 'dc_publisher', '_text']) \
            for record in reader]   
sources = [record.get(['metadata', '{http://www.openarchives.org/OAI/2.0/oai_dc/}dc', 'dc_source', '_text']) \
            for record in reader]
identifiers = [record.get(['metadata', '{http://www.openarchives.org/OAI/2.0/oai_dc/}dc', 'dc_identifier', '_text']) \
            for record in reader]                 


# Create a dictionary from the lists and turn the dictionary into a dataframe. Convert the dataframe to a CSV
dic = {'dc_creator': creators, 'dc_title': titles, 'dc:publisher': publishers, 'dc_source': sources, 'dc_identifier': identifiers} 
df = pd.DataFrame(dic)
df.to_csv('data/records.csv')
