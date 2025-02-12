import os
import zarr
import shutil

# Define the paths
zarr_file_path = '/Users/piotr/Downloads/Munkholmen-2024.10.1-2024.10.31-sea_water_temperature-20250210_1552.47.zarr'
examples_folder_path = '_sources/zarr_attrs_sdn/examples/'

# Open the Zarr file
zarr_root = zarr.open(zarr_file_path, mode='r')

# Function to copy .zattrs files
def copy_zattrs_files(zarr_group, current_path=''):
    print("items: ", zarr_group.items())
    for name, item in zarr_group.items():
        item_path = os.path.join(current_path, name)
        print(f"Processing item: {item_path}")  # Debugging statement
        zattrs_path = os.path.join(item.store.path, item_path, '.zattrs')
        print(f"Checking for .zattrs at: {zattrs_path}")  # Debugging statement
        if os.path.exists(zattrs_path):
            dest_path = os.path.join(examples_folder_path, f'.zattrs-{item_path.replace("/", "-")}')
            print(f"Copying .zattrs to: {dest_path}")  # Debugging statement
            shutil.copy(zattrs_path, dest_path)
        else:
            print(f".zattrs not found at: {zattrs_path}")  # Debugging statement
        if isinstance(item, zarr.Group):
            copy_zattrs_files(item, item_path)

# Start copying .zattrs files from the root
copy_zattrs_files(zarr_root)