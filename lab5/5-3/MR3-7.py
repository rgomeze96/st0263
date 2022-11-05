from mrjob.job import MRJob
from mrjob.step import MRStep

class MRDataPeliculas(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapperMovie,
                   reducer=self.reduceRating),
            MRStep(mapper=self.mapperGenre,
                    reducer=self.reducer2)
        ]

    def mapperMovie(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield movie, [float(rating), genre]

    def reduceRating(self, movie, values):
        l = list(values)
        sum = 0
        cont = 0
        genre = l[0][1]
        for i in l:
            sum = sum + i[0]
            cont = cont + 1
        avg  =sum/cont
        yield None, [avg, movie, genre]

    def mapperGenre(self, _, array):
        yield array[2], [array[1], array[0]]

    def reducer2(self, genre, values):
        l = list(values)
        movies = ["j", "f"]
        vals = [0.0, 6.0]
        for i in l:
            if (i[1] > vals[0]):
                movies[0] = i[0]
                vals[0] = i[1]
            if (i[1] < vals[1]):
                movies[1] = i[0]
                vals[1] = i[1]
        yield genre, movies


if __name__ == '__main__':
    MRDataPeliculas.run()