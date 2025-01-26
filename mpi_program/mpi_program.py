from mpi4py import MPI
from collections import defaultdict
import time
import argparse

def mpi_mapper(lines):
    results = []
    for line in lines:
        if line.startswith("image"):
            continue

        line = line.strip().split(',')
        
        try:
            currentCountry = line[0].strip()  
            red = line[3].strip()
            green = line[4].strip()
            blue = line[5].strip()

            currentKey = currentCountry + " (" + red + " , " + green + " , " + blue + ")"
            results.append((currentKey, 1)) 

        except Exception as e:
            continue
    
    return results

def mpi_reducer(mapped_data):
    counts = defaultdict(int)
    
    for key, value in mapped_data:
        counts[key] += value
    
    return [(key, count) for key, count in counts.items()]

def main():
    parser = argparse.ArgumentParser(description='MPI Program')
    args = parser.parse_args()

    start_time = time.time()
    
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        with open(args.filename, 'r') as f:
            lines = f.readlines()

        chunks = [lines[i::size] for i in range(size)]
    else:
        chunks = None

    local_lines = comm.scatter(chunks, root=0)

    local_mapped = mpi_mapper(local_lines)
    all_mapped = comm.gather(local_mapped, root=0)

    if rank == 0:
        all_mapped = [item for sublist in all_mapped for item in sublist]
        reduced_results = mpi_reducer(all_mapped)
        for key, count in reduced_results:
            print(key + " = " + str(count))
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    if rank == 0:
        print(f"Total time taken: {elapsed_time} seconds")

if __name__ == '__main__':
    main()