import unittest
from .models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''
    Test class to tst behaviour of the movie class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python series','https://developers,themoviedb.org/3/getting-started/images/khsjha27hbs',8.5,129993)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

        
if __name__ == '__main__':
    unittest.main()
