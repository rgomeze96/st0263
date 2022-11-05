from mrjob.job import MRJob
from mrjob.step import MRStep

class MRDataEmpresas(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducerCheck),
            MRStep(reducer=self.reducerSelect)
        ]

    def mapper(self, _, line):
        company, price, date = line.split(',')
        yield company, price

    def reducerCheck(self, company, values):
        l = list(values)
        boolV = "1"
        for i in range(1, len(l)):
            if (l[i] < l[i-1]):
                boolV = "0"
                break
        yield company, boolV

    def reducerSelect(self, company, value):
        if (str(value) == "1"):
            yield company, None
        

if __name__ == '__main__':
    MRDataEmpresas.run()