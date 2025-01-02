from mpi4py import MPI
import sys

def mapper(lines):
    results = []
    for line in lines:
        # Skip the header
        if line.startswith("Date"):
            continue
        
        # Parse the line
        line = line.strip().split(',')
        currentCountry = line[1].strip()
        if len(line[2]) == 0:
            continue
        currentFx = float(line[2])
        
        # Collect the country and FX rate as a key-value pair
        results.append((currentCountry, currentFx))
    return results

def reducer(mapped_data):
    from collections import defaultdict
    results = defaultdict(list)
    for country, fx in mapped_data:
        results[country].append(fx)
    
    reduced_results = []
    for country, fx_list in results.items():
        for i in range(1, len(fx_list)):
            percent_change = ((fx_list[i] - fx_list[i-1]) / fx_list[i-1]) * 100.0
            reduced_results.append((country, round(percent_change, 2)))
    return reduced_results

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        # Read input data
        with open('MPI\daily.csv', 'r') as f:
            lines = f.readlines()
        
        # Distribute lines to all processes
        chunks = [lines[i::size] for i in range(size)]
    else:
        chunks = None

    # Scatter the chunks to all processes
    local_lines = comm.scatter(chunks, root=0)

    # Perform the map phase
    local_mapped = mapper(local_lines)

    # Gather all mapped data to the root process
    all_mapped = comm.gather(local_mapped, root=0)

    if rank == 0:
        # Flatten the list of lists
        all_mapped = [item for sublist in all_mapped for item in sublist]

        # Perform the reduce phase
        reduced_results = reducer(all_mapped)

        # Output the results
        for country, percent_change in reduced_results:
            print(f"{country} = {percent_change}")

if __name__ == '__main__':
    main()