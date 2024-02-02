'''find and output all functions'''
import sys
import os
import glob

dirPath = os.path.dirname(__file__)
sys.path.append(os.path.join(dirPath))

if __name__ == "__main__":
    all_functions = []
    file_loc = '.' if (len(sys.argv)<2) else sys.argv[1]
    for dir_name, subdir_list, file_list in os.walk(file_loc):
        function_files = glob.glob(dir_name + os.sep + "*-func.rosetta")
        print('in dir:', dir_name, ' found # files:', len(function_files))
        for func_file in function_files:
            file = open(func_file,'r')
            namespace = None
            while True:
                next_line = file.readline()
                if 'namespace' in next_line:
                    next_line.removesuffix('namespace ')
                    namespace = next_line.split(' ', 2)[1].replace(':','').replace('\n','')
                elif namespace is not None and next_line.startswith('func'):
                    name_and_comment = next_line.replace('"','').split(': ',2)
                    line = namespace + ',"' + name_and_comment[0].replace(':','').replace('\n','') +'"'
                    if(len(name_and_comment) > 1):
                        line = line + ',"' + name_and_comment[1].replace('\n','')+'"'
                    print(line)
                    all_functions.append (namespace + ',' + next_line)
                if not next_line:
                    break
            file.close()
