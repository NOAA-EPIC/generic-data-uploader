# Demo: Walk-Thru & Upload Nested Data Files Residing in the Main Data Directory of Interest
import sys
sys.path.append( '../modules' )
from get_nested_data import GetNestedData
from upload_data import UploadData
from progress_bar import ProgressPercentage
import argparse

# User Inputs.
argParser = argparse.ArgumentParser()
argParser.add_argument("-b", "--bucket", help="Object's bucket label. Type: String. Options: 'land-da', 'srw', 'rt', 'gdas', 'htf', 'coastal")
argParser.add_argument("-m", "--main_data_dir", help="Dataset's parent folder. Type: String. Format: 'PARENT_DATA_FOLDERNAME_TO_MIGRATE_TO_CLOUD/'")

args = argParser.parse_args()

# Instantiate Class Object.
uploader_wrapper = UploadData(use_bucket=args.bucket)

# List Nested Data Files' Directories
print("Extracting list of all directories from main data directory of interest ...")
nested_data_dirs = GetNestedData(main_data_dir=args.main_data_dir).file_dirs

# Walk Thru & Upload Nested Data Files.
uploader_wrapper.upload_files2cloud(nested_data_dirs)
print("\033[1m" + f"\nData transfer to S3 bucket complete!" + "\033[0m") 



