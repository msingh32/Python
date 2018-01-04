import os
def rename_files():
    #get file names from foleder
    file_list=os.listdir(r"C:\Users\Mili\Downloads\prank")
    print(file_list)
    saved_path=os.getcwd()
    print("Current Working Directory is:"+saved_path)
    os.chdir(r"C:\Users\Mili\Downloads\prank")
    #for each file rename filename
    for file_name in file_list:
        file_name_bytes = str.encode(file_name)
        os.rename(file_name,file_name_bytes.translate(None,b"0123456789"))
    os.chdir(saved_path)

rename_files()