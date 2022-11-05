from mrjob.job import MRJob

class MRDataPeliculas(MRJob):

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield movie, int(rating)

    def reducer(self, movie, rating):
        l = list(rating)
        avg = sum(l) / len(l)        
        yield movie, [len(l), avg]

if __name__ == '__main__':
    MRDataPeliculas.run()