import os
OUTPUT_DIR='input3'
output_dir = OUTPUT_DIR
all_data_dir = DATA_DIR
column_name = ['path', 'level', 'position']
output_list = []
index_list = []
for subdir, dirs, files in os.walk(all_data_dir):
    category_name = os.path.basename(subdir)
    for file in files:
        input_file = os.path.join(subdir, file)
        # filename contains information, match then out
        m = re.match(u'../../input-image-dmsa2vur/\d/(\d+--\d+)_(\d)_(left|right)', input_file) 
        index = m.group(1) # id
        level = m.group(2) # level
        position = m.group(3) # position
        path = input_file[len('../../input-image-dmsa2vur/'):]
        output_list.append([path, index, level, position])
        index_list.append(index)

        
file_df=pd.DataFrame(output_list, columns=column_name, index=index_list)
file_df.index.name = '序号'
