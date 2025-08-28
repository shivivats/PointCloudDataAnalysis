import sys
import math


def get_third_substring_after_line(filename, search_term):
    """Finds a line in a file, gets the next line, and splits it with "     ".
       Returns the 3rd substring.

    Args:
      filename: The name of the file to search.
      search_line: The line to search for.

    Returns:
      The 3rd substring of the next line after the search line, or None if not found.
    """

    with open(filename, 'r') as f:
        results = []
        for line in f:
            if search_term in line.strip():
                next_line = next(f)
                if 'a' in next_line and 'nan' not in next_line:
                    split_line = next_line.split('  ')
                    # print(split_line)
                    results.append(float(split_line[7]))
        return results


if __name__ == '__main__':
    #   if len(sys.argv) < 2:
    #     print("Usage: python script.py <filename1> <filename2> ...")
    #     sys.exit(1)
    #   i=1
    #   while i < len(sys.argv):
    #     filename = sys.argv[i]
    filenames = [
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/BlueSpin/r01/encode/BlueSpin_r01.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/BlueSpin/r02/encode/BlueSpin_r02.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/BlueSpin/r03/encode/BlueSpin_r03.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/BlueSpin/r04/encode/BlueSpin_r04.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/BlueSpin/r05/encode/BlueSpin_r05.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/FlowerDance/r01/encode/FlowerDance_r01.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/FlowerDance/r02/encode/FlowerDance_r02.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/FlowerDance/r03/encode/FlowerDance_r03.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/FlowerDance/r04/encode/FlowerDance_r04.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/FlowerDance/r05/encode/FlowerDance_r05.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/ReadyForWinter/r01/encode/ReadyForWinter_r01.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/ReadyForWinter/r02/encode/ReadyForWinter_r02.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/ReadyForWinter/r03/encode/ReadyForWinter_r03.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/ReadyForWinter/r04/encode/ReadyForWinter_r04.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/ReadyForWinter/r05/encode/ReadyForWinter_r05.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/CasualSquat/r01/encode/CasualSquat_r01.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/CasualSquat/r02/encode/CasualSquat_r02.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/CasualSquat/r03/encode/CasualSquat_r03.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/CasualSquat/r04/encode/CasualSquat_r04.txt',
        '/mnt/d/ComPEQ-MR/Compressed-point-cloud/VPCC/CasualSquat/r05/encode/CasualSquat_r05.txt',
    ]
    for filename in filenames:
        print(filename.split('/')[-1])
        search_term = 'Total Frames'
        results = get_third_substring_after_line(filename, search_term)
        if len(results) == 0:
            print('didnt find anything!')
        else:
            # print(results)
            # print(sum(results) /  len(results))
            print(round(sum(results) / 1000, 2))
        # i+=1
