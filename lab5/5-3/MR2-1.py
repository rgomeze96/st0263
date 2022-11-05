from mrjob.job import MRJob

class MRDataEmpresas(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        yield company, [price, date]

    def reducer(self, company, values):
        l = list(values)
        dates = [0, 0]
        values = [1000000000000000000000000000.0, 0.0]
        for i in l:
            if (float(i[0]) < values[0]):
                values[0] = float(i[0])
                dates[0] = i[1]

            if (float(i[0]) > values[1]):
                values[1] = float(i[0])
                dates[1] = i[1]
        
        yield company, dates

if __name__ == '__main__':
    MRDataEmpresas.run()