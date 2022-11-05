from mrjob.job import MRJob
from mrjob.step import MRStep

class MRDataPeliculas(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducerSum),
            MRStep(reducer=self.reducerSelect)
        ]

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield date, 1

    def reducerSum(self, date, rating):
        l = list(rating)        
        yield None, [len(l), date]

    def reducerSelect(self, _, dateCount):
        yield max(dateCount)


if __name__ == '__main__':
    MRDataPeliculas.run()