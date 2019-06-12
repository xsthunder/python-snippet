import os
OUTPUT_DIR='input3'
output_dir = OUTPUT_DIR
all_data_dir = DATA_DIR
column_name = ['path', '序号', 'level', 'position']
output_list = []
for subdir, dirs, files in os.walk(all_data_dir):
    category_name = os.path.basename(subdir)
    for file in files:
        input_file = os.path.join(subdir, file)
        # filename contains information, match then out
        m = re.match(u'../../input-image-dmsa2vur/\d/(\d+--\d+)_(\d)_(left|right)', input_file) 
        index = m.group(1) # id
        level = m.group(2) # level
        position = m.group(3) # position
        output_list.append([input_file, index, level, position])

        
file_df=pd.DataFrame(output_list, columns=column_name)
