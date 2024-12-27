from mrjob.job import MRJob

class MRMapper(MRJob):
    def mapper(self, _, line):
        # Skip the header
        if line.startswith("header_column1"):
            return
        
        # Parse the line
        line = line.strip().split(',')
        currentCountry = line[1].strip()
        if len(line[2]) == 0:
            return
        currentFx = float(line[2])
        
        # Yield the country and FX rate as a key-value pair
        yield currentCountry, currentFx

    def reducer(self, country, fx_values):
        # Process values for each country
        fx_list = list(fx_values)
        for i in range(1, len(fx_list)):
            percent_change = ((fx_list[i] - fx_list[i-1]) / fx_list[i-1]) * 100.0
            yield country, round(percent_change, 2)

if __name__ == '__main__':
    MRMapper.run()
