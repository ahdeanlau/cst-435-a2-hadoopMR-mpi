
1. need to install python on all resourcemanager and nodemanagers
2. need to make sure the python is valid for the program to run


shell into a container bash: 
docker exec -it <container_id_or_name> /bin/bash

docker exec -i <container_name_or_id> bash -c "bash -s" < setup_python.sh

multipass transfer -r <local_folder_path> <vm_name>:<destination_path>
multipass transfer -r /Users/dlau/Documents/GitHub/cst-435-a2-hadoopMR-mpi/mapreduce worker1:/home/ubuntu/

sudo docker cp ./my_folder my_container_id:/app
sudo docker cp mapreduce my_container_id:/app

docker stack deploy -c docker-compose-swarm.yml hadoop