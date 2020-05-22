import urllib.request, gzip, shutil, os
import pandas as pd

def downloadData():
    os.mkdir('temp')
    url = 'https://datasets.imdbws.com/title.basics.tsv.gz'
    urllib.request.urlretrieve(url, 'temp/title.basics.tsv.gz')
    
    url2 = 'https://datasets.imdbws.com/title.ratings.tsv.gz'
    urllib.request.urlretrieve(url2, 'temp/title.ratings.tsv.gz')


def unzipData():
    with gzip.open('temp/title.ratings.tsv.gz', 'r') as f_in, open('temp/ratings.tsv', 'wb') as f_out:
      shutil.copyfileobj(f_in, f_out)
      
    with gzip.open('temp/title.basics.tsv.gz', 'r') as f_in, open('temp/basics.tsv', 'wb') as f_out:
      shutil.copyfileobj(f_in, f_out)
     
def cleanData():
    ''' Read and convert missing data with na values readable to pandas '''
    na_vals = ['\\N'] 
    
    ''' Only read columns we need'''
    df1 = pd.read_csv('temp/ratings.tsv', sep='\t')
    df2 = pd.read_csv('temp/basics.tsv', sep='\t',
                      usecols=['tconst', 'primaryTitle', 'startYear', ],
                      dtype='string',  na_values=na_vals)
    
    '''Join dataframes with ratings and titles to one dataframe'''
    df3 = df1.join(df2.set_index('tconst'), on='tconst') # Both dataframes has 'tconst', so join by that
    
    ''' Sort dataframe a bit, I want to see most popular at the top'''
    df3.sort_values(by=['numVotes','averageRating'], ascending=False, inplace=True)
    
    """ Filter out unpopular titles (because I don't care about those in this project)"""
    df4 = df3[df3['numVotes'] > 10000]
    
    ''' Write cleaned data to csv '''
    df4.to_csv('cleanIMDB.csv', index=False)

    
def initiate():
    print('\nDownloading data...')
    downloadData()
    print('\nUnzipping...')
    unzipData()
    print('\nCleaning data...')
    cleanData()
    print('\nRemoving temporary files...')
    shutil.rmtree('temp')
    print('\nComplete!')

if __name__ == '__main__':
    initiate()