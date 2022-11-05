from mrjob.job import MRJob

class MRDataPeliculas(MRJob):

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield user, int(rating)

    def reducer(self, user, rating):
        l = list(rating)
        avg = sum(l) / len(l)        
        yield user, [len(l), avg]

if __name__ == '__main__':
    MRDataPeliculas.run()