from mrjob.job import MRJob
from mrjob.step import MRStep

class MRDataEmpresas(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapperStocks,
                   reducer=self.reducerDates),
            MRStep(mapper=self.mapperDates,
                    reducer=self.reducerSum),
            MRStep(reducer=self.reducerSelect)
        ]

    def mapperStocks(self, _, line):
        company, price, date = line.split(',')
        yield company, [float(price), date]

    def reducerDates(self, company, values):
        l = list(values)
        date = "1"
        val = 100000000.0
        for i in l:
            if (i[0] < val):
                val = i[0]
                date = i[1]
        yield company, date

    def mapperDates(self, company, date):
        yield date, 1

    def reducerSum(self, date, value):
        yield None, [sum(list(value)), date]

    def reducerSelect(self, _, val):
        yield max(val)
        

if __name__ == '__main__':
    MRDataEmpresas.run()