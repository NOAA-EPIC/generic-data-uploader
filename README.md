
<h1 align="center">
Generic Data Uploader for 
    UFS-Based Datasets to Cloud Data Storage
</h1>

<h5 align="center">
    
[About](#About) • [Prerequisites](#Prerequisites) • [Quick Start](#Quick-Start) • [Environment Setup](#Environment-Setup) • [What's Included](#What's-Included) • [Example](#Example) • [Status](#Status) • [Version](#Version)

</h5>

# About

__Purpose:__

The purpose of this program is to transfer the Unified Forecast System (UFS)-based data residing within the RDHPCS to cloud data storage via chaining API calls to communicate with its cloud data storage bucket. The program will support the data required for the UFS application release versions.

According to Amazon AWS, the following conditions need to be considered when transferring data to cloud data storage:

* Largest object that can be uploaded in a single PUT is 5 GB.
* Individual Amazon S3 objects can range in size from a minimum of 0 bytes to a maximum of 5 TB.
* For objects larger than 100 MB, Amazon recommends using the Multipart Upload capability.
* The total volume of data in a cloud data storage bucket are unlimited.

Tools which could be be utilized to perform data transferring & partitioning (Multipart Upload/Download) are:

* AWS SDK
* AWS CLI
* AWS S3 REST API

In this demontration, the framework will implement Python AWS SDK for transferring the UFS-based data (e.g. fixed & input model datasets) from the RDHPCS, Orion, to the cloud data storage with low latency. 

The AWS SDK will be implemented for the following reasons:
To integrate with other python scripts.
AWS SDK carries addition capabilities/features for data manipulation & transferring compare to the aforementioned alternate tools.


__Capabilities:__

The framework will be able to perform the following actions:

Multi-threading & partitioning the datasets to assist in the optimization in uploading performance of the datasets from on-premise to cloud. 

# Prerequisites
* Setting up AWS CLI configurations with IAM credentials: https://confluence.epic.oarcloud.noaa.gov/pages/viewpage.action?spaceKey=US&title=AWS+Command+Line+Interface+%28AWS+CLI%29+Credentials+Setup
* Clone this repository (generic data uploader)
* Setting up conda environment w/in RDHPCS.
    * Refer to [Environment Setup](#Environment-Setup)
* [![Version badge](https://img.shields.io/badge/Python-3.9-blue.svg)](https://shields.io/)

# Quick Start 
__To Migrate a Single File:__

1) Install miniconda per "Environment Setup" section.
   
2) Establish AWS credentials configuration file via the "AWS Command Line Interface (AWS CLI) Credentials Setup" page in Confluence.
   
3) Save data file you want to move within the repository's "main" folder & structure the data on-premise as you would like it structured in cloud. For example, 
    __generic-data-uploader/main/[new directory]/[new file]__
   
4) Move back to "main" directory and execute the following command within the terminal to migrate the data to cloud:
   
    * python __upload_file2cloud.py__ -b __BUCKET_NAME__ -k __FILE_DIR_TO_MIGRATE_TO_CLOUD_INCLUDING_FILENAME__
   
        * __BUCKET_NAME__:
            Use one of the below options for the available cloud buckets:

            *  "srw" (Short-Range Weather application's bucket) 
            *  "rt" (UFS-WM Regression Test's bucket)
            *  "land-da" (Land DA's bucket)
            *  "gdas" (Global Data Assimilation System bucket)
            *  "htf"  (Hierarchical Testing Framework bucket)
            *  "mrw"  (Mid-Range Weather application bucket)
            *  "coastal" (UFS Costal bucket)

        * __FILE_DIR_TO_MIGRATE_TO_CLOUD_INCLUDING_FILENAME:__
    
            * As an example for Land DA files, the relative directory of "FILENAME.tar.gz" could be saved as "current_land_da_release_data/FILENAME.tar.gz" within the "main" folder on-premise for its object's key to be set as "current_land_da_release_data/FILENAME.tar.gz" in cloud. In this scenario, __FILE_DIR_TO_MIGRATE_TO_CLOUD_INCLUDING_FILENAME__ would be set to "current_land_da_release_data/FILENAME.tar.gz".

            __generic-data-uploader/main/current_land_da_release_data/FILENAME.tar.gz__

__To Walk-Thru & Migrate Nested Files to Cloud (Set Each File as Object w/ Key Set As Their Relative On-Premise Directory Path):__
1) Install miniconda per "Environment Setup" section.
   
2) Establish AWS credentials configuration file via the "AWS Command Line Interface (AWS CLI) Credentials Setup" page in Confluence. Note: For this application, ensure the UFS-WM RT bucket has a profile set to "ufs-wm-rt-app" per the procedural setup described in the "AWS Command Line Interface (AWS CLI) Credentials Setup" page in Confluence.
   
3) Save data of interest to migrate to cloud within the repository's "main" folder & structure the data on-premise as you would like it structured in cloud. For example, "__PARENT_DATA_FOLDERNAME_TO_MIGRATE_TO_CLOUD__" should be saved under the "current_land_da_release_data" folder within the repository's "main" folder on-premise -- allows each of the folder's files to be set to an object with their key set as "current_land_da_release_data/__PARENT_DATA_FOLDERNAME_TO_MIGRATE_TO_CLOUD__/SUBFOLDERNAME/.../FILENAME" in cloud.
Each key will correspond to their object's relative directory path as seen on-premise.

5) Execute the following command within the terminal to migrate each individual data file w/in the data folder to cloud as individual objects. 
*Note: Each object will have their keys set as their data directory/location as seen on their local source's disk. It is required that the data of interest has its permissions set to readable.
   
   * python __upload_nested_files2cloud.py__ -b __BUCKET_NAME__ -m __PARENT_DATA_FOLDERNAME_TO_MIGRATE_TO_CLOUD__/
     
        * __BUCKET_NAME__:
            Use one of the below options for the available cloud buckets:
            
            *  "srw" (Short-Range Weather application's bucket) 
            *  "rt" (UFS-WM Regression Test's bucket)
            *  "land-da" (Land DA's bucket)
            *  "gdas" (Global Data Assimilation System bucket)
            *  "htf"  (Hierarchical Testing Framework bucket)
            *  "mrw"  (Mid-Range Weather application bucket)
            *  "coastal" (UFS Costal bucket)

# Environment Setup:

* Install miniconda on your machine. Note: Miniconda is a smaller version of Anaconda that only includes conda along with a small set of necessary and useful packages. With Miniconda, you can install only what you need, without all the extra packages that Anaconda comes packaged with:
Download latest Miniconda (e.g. 3.9 version):

    * wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh

* Check integrity downloaded file with SHA-256:

    * sha256sum Miniconda3-py39_4.9.2-Linux-x86_64.sh

Reference SHA256 hash in following link: https://docs.conda.io/en/latest/miniconda.html

* Install Miniconda in Linux:

    * bash Miniconda3-py39_4.9.2-Linux-x86_64.sh

* Next, Miniconda installer will prompt where do you want to install Miniconda. Press ENTER to accept the default install location i.e. your $HOME directory. If you don't want to install in the default location, press CTRL+C to cancel the installation or mention an alternate installation directory. If you've chosen the default location, the installer will display “PREFIX=/var/home//miniconda3” and continue the installation.

* For installation to take into effect, run the following command:

source ~/.bashrc

* Next, you will see the prefix (base) in front of your terminal/shell prompt. Indicating the conda's base environment is activated.

Note: The first option below is the recommended approach for using the generic data uploader as the YAML file is provided in the repository (__generic-data-uploader/env/cloud_xfer_env.yml__). A .yml file is a text file that contains a list of dependencies, which channels a list for installing dependencies for the given conda environment. For the code to utilize the dependencies, you will need to be in the directory where the environment.yml file lives.

    * To create a new environment from an existing YAML file (if a YAML file is provided):

        * conda env create -f cloud_xfer_env.yml (the env file for generic-data-uploader)
    
(OR)

    * To create a new environment (if a YAML file is not provided)

        * conda create -n [Name of your conda environment you wish to create]

(OR)

    * To ensure you are running Python 3.9:

        * conda create -n myenv Python=3.9

### Activate the new environment via:

conda activate [Name of your conda environment you wish to activate]

* Verify that the new environment was installed correctly via:

    * conda info --env

*Note:

* From this point on, must activate conda environment prior to .py script(s) or jupyter notebooks execution using the following command: conda activate
    * To deactivate a conda environment:
        * conda deactivate

### Additonal Information for Environment

To create a .yml file, execute the following commands:

* Activate the environment to export:

    * conda activate myenv

* Export your active environment to a new file:

    * conda env export > [ENVIRONMENT FILENAME].yml

# What's Included
Within the download of this repository you will find the following directories and files:
* Scripts:
    * Modules:
         * __upload_data.py__
            * Uploads the UFS Land DA Application via AWS SDK
        * progress_bar.py
            * Monitors uploading progress of datasets to cloud   
    * Main:
        * __upload_file2cloud.py__
            * Main executable script for extracting & uploading the datasets residing on-prem to cloud. Sets
            unique key for the tar.gz data supporting the UFS-based application. Note: Must save data of interest to migrate to cloud within the repository's "main" folder 
            & structure it on-premise as you would like it structured in cloud. For example, the relative directory of "FILENAME.tar.gz" should be saved as "current_land_da_release_data/FILENAME.tar.gz" within the "main" folder on-premise for the object's key to be set as "current_land_da_release_data/FILENAME.tar.gz" within the Land DA established cloud storage on AWS.
        * __upload_nested_files2cloud.py__
            * Main executable script for walking thru nested files within a folder.
              It will extract & uploading each file as object to cloud with each object's key set as their corresponding relative directory paths.
        * __get_objects_list.py__
            * Obtains list of unique data files within the Land DA cloud storage
        * __delete_cloud_object.py__
            * Main executable script for deleting the objects of the Land DA in datasets in cloud based on their unique key.
    * env:
        * __cloud_xfer_env.yml__
            * The main conda environment YML file used for the generic data uploader.

### Link Home Directory to Dataset Location on RDHPCS Platform

* Unfortunately, there is no way to navigate to the "/work/" filesystem from within the Jupyter interface when working on the remote server, Orion. The best way to workaround is to create a symbolic link in your home folder that will take you to the /work/ filesystem. Run the following command from a linux terminal on Orion to create the link:

    * ln -s /work /home/[Your user account name]/work

* Now, when you navigate to the /home/[Your user account name]/work directory in Jupyter, it will take you to the /work folder. Allowing you to obtain any data residing within the /work filesystem that you have permission to access from Jupyter. This same procedure will work for any filesystem available from the root directory.

*Note: On Orion, user must sym link from their home directory to the main directory containing the datasets of interest.

## Open & Run Application on Jupyter Notebook

* Open OnDemand has a built-in file explorer and file transfer application available directly from its dashboard via:

    * Login to https://orion-ood.hpc.msstate.edu/

* In the Open OnDemand Interface, select Interactive Apps > Jupyter Notbook

# Example 

Below is an example of what the files and directory look like in the AWS S3 bucket. This specific example is for the Land DA bucket with its most recent release.

<p align="center">
    <img src=images/landdaex.jpg" width="690" height="350">
</p>

# Status

[![Development badge](https://img.shields.io/badge/development-passing-green)](https://shields.io/)
[![Build badge](https://img.shields.io/badge/build-passing-blue)](https://shields.io/)

# Version:
* Draft as of 11/21/24
