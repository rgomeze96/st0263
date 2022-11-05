from mrjob.job import MRJob

class MRDataEmpleados(MRJob):

    def mapper(self, _, line):
        idemp, sector,salary,year = line.split(',')
        yield idemp, sector

    def reducer(self, idemp, sector):
        l = list(sector)
        values = []
        for i in l:
            if (i not in values):
                values.append(i)
        
        yield idemp, values

if __name__ == '__main__':
    MRDataEmpleados.run()