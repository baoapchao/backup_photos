from main import *
print('What is the folder path?')
folderpath = input()

print(f'(Y/N) Do you want custom date format (default date format is {default_backup_foldername_format}?')
is_custom_date_format = input()

if is_custom_date_format == 'Y':
    print(fr'What is the date format (E.g: %Y-%m-%d)?')
    date_format = input()
elif is_custom_date_format == 'N':
    date_format = default_backup_foldername_format
else:
    raise Exception("Sorry, Y or N only")

tidy_folders(folderpath, date_format)