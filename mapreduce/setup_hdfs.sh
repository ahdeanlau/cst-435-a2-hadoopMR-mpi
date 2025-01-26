#!/bin/bash

# Define variables
HDFS_INPUT_DIR="/user/hadoop/input"
HDFS_OUTPUT_DIR="/user/hadoop/output"
LOCAL_FILE="/mapreduce/image_pixel_data_10_by_10.csv"

# Function to remove an HDFS directory if it exists
remove_hdfs_dir() {
    local dir=$1
    hdfs dfs -test -d $dir
    if [ $? -eq 0 ]; then
        echo "HDFS directory $dir exists. Removing it..."
        hdfs dfs -rm -r -skipTrash $dir
        if [ $? -ne 0 ]; then
            echo "Failed to remove HDFS directory $dir. Exiting."
            exit 1
        fi
        echo "Directory $dir successfully removed."
    fi
}

# Remove HDFS input directory if it exists
remove_hdfs_dir $HDFS_INPUT_DIR

# Recreate the HDFS input directory
echo "Creating HDFS directory $HDFS_INPUT_DIR..."
hdfs dfs -mkdir -p $HDFS_INPUT_DIR
if [ $? -ne 0 ]; then
    echo "Failed to create HDFS directory $HDFS_INPUT_DIR. Exiting."
    exit 1
fi
echo "HDFS directory $HDFS_INPUT_DIR successfully created."

# Remove HDFS output directory if it exists
remove_hdfs_dir $HDFS_OUTPUT_DIR

# Check if the file exists locally
if [ -f $LOCAL_FILE ]; then
    echo "Local file $LOCAL_FILE found. Uploading to HDFS..."
    hdfs dfs -put -f $LOCAL_FILE $HDFS_INPUT_DIR
    if [ $? -eq 0 ]; then
        echo "File $LOCAL_FILE successfully uploaded to $HDFS_INPUT_DIR."
    else
        echo "Failed to upload file $LOCAL_FILE to HDFS. Exiting."
        exit 1
    fi
else
    echo "Local file $LOCAL_FILE does not exist. Exiting."
    exit 1
fi
