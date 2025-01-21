import time
from mrjob.job import MRJob
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class MRMapper(MRJob):
    def mapper_init(self):
        """Initialize timer for the mapper phase."""
        self.start_time = time.time()
    
    def mapper_final(self):
        """Log total time taken by the mapper phase."""
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        logging.info(f"Mapper Phase Completed in {elapsed_time:.4f} seconds")

    def mapper(self, _, line):
        """Mapper logic."""
        if line.startswith("Date"):
            return
        
        # Parse the line
        line = line.strip().split(',')
        currentCountry = line[1].strip()
        if len(line[2]) == 0:
            return
        currentFx = float(line[2])
        
        # Yield the country and FX rate as a key-value pair
        yield currentCountry, currentFx

    def reducer_init(self):
        """Initialize timer for the reducer phase."""
        self.start_time = time.time()
    
    def reducer_final(self):
        """Log total time taken by the reducer phase."""
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        logging.info(f"Reducer Phase Completed in {elapsed_time:.4f} seconds")

    def reducer(self, country, fx_values):
        """Reducer logic."""
        fx_list = list(fx_values)
        for i in range(1, len(fx_list)):
            percent_change = ((fx_list[i] - fx_list[i-1]) / fx_list[i-1]) * 100.0
            yield country, round(percent_change, 2)

if __name__ == '__main__':
    logging.info("Starting MapReduce Job")
    total_start_time = time.time()

    MRMapper.run()

    total_end_time = time.time()
    total_time = total_end_time - total_start_time
    logging.info(f"MapReduce Job Completed in {total_time:.4f} seconds")
