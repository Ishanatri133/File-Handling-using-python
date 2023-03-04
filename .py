import os
import shutil
import sqlite3



# set the source directory where the xlsx files are located
src_dir = './'

# set the destination directory where the copied files will be stored
dest_dir = 'output/'

# set the prefix for the files to be copied
prefix = 'abc-'

# set the file extension for the files to be copied
ext = '.xlsx'

# create a connection to a new sqlite database and create a table to store the data
conn = sqlite3.connect('ishan.db')


# loop through the files in the source directory
for file in os.listdir(src_dir):
    # check if the file has the correct prefix and extension
    if file.startswith(prefix) and file.endswith(ext):
        shutil.copy2(os.path.join(src_dir, file), dest_dir)
        
        # read the data from the specified tab
        df = pd.read_excel(os.path.join(dest_dir, file), sheet_name='Sheet1', header=0)

        # add the filename to the dataframe
        df['filename'] = file

        table_name = file.replace('.xlsx', '').replace('-', '_')
        
        # insert the data into the sqlite database in sql format
        df.to_sql(table_name, conn, if_exists='append', index=False)

        # print the data from the sqlite database



# save the changes to the sqlite database
conn.commit()

        
# close the sqlite connection
conn.close()
