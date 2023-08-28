import os 
import pickle
from collections import defaultdict
import subprocess


class GetNestedData():
    """
    Extract locality of the UFS datasets of interest & generate a list of the data files.
    
    """
    
    def __init__(self, main_data_dir):
        """
        Args:                  
            main_data_dir (str): Source main directory of the datasets. 
                                 NOTE: It is required that the main directory's 
                                 contents are readable.

        """
        # Walk thru directories to obtain all readable files' - allows one to mimic & set their 
        # directories as keys w/in cloud
        self.main_data_dir = main_data_dir
        
        # Extract all directories residing w/in main data directory.
        self.file_dirs = self.get_data_dirs()

    def get_data_dirs(self):
        """
        Extract list of all file directories in main data directory. 
        Note: Not applicable for single TAR file with nested data content.
        
        Args: 
            None
            
        Return (list): List of all file directories in datasets' main directory
        of interest.
        
        """
          
        # Generate List of all data folders/files' directories w/in main data directory.
        file_dirs = []
        root_dirs = []
        for root_dir, subfolders, filenames in os.walk(self.main_data_dir, followlinks=True):
            root_dirs.append(root_dir)
            for file in filenames:
                file_dirs.append(os.path.join(root_dir, file))
        root_list = os.listdir(self.main_data_dir)
        print("\033[1m" +\
              f"\nAll Primary Dataset Folders within Main Data Directory ({self.main_data_dir}):" +\
              f"\n\n\033[0m{root_dirs}\n")
        
        return file_dirs
