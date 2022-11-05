from mrjob.job import MRJob
from mrjob.step import MRStep

class MRDataPeliculas(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducerAvg),
            MRStep(reducer=self.reducerSelect)
        ]

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield date, int(rating)

    def reducerAvg(self, date, rating):
        l = list(rating)       
        avg = sum(l) / len(l) 
        yield None, [avg, date]

    def reducerSelect(self, _, dateCount):
        yield min(dateCount)


if __name__ == '__main__':
    MRDataPeliculas.run()