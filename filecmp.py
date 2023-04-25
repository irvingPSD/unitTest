import re
from fractions import Fraction

# este es el script that trabaja con a.txt file
def get_execution_times():
    filename= input("Enter file Name: ")
    with open(filename, 'r') as f:
        contents = f.read()

    results = {}

    # Get pytest execution times
    match = re.search(r'pytest:\n(.*?)Total time for pytest:', contents, re.DOTALL)
    if match:
        pytest_times = match.group(1)
        for line in pytest_times.split('\n'):
            line = line.strip()
            if line:
                parts = line.split(':')
                func_name = parts[0].strip()
                time = float(parts[1].strip().split()[0])
                results[func_name] = {'pytest': time}

    # Get unittest execution times
    match = re.search(r'unittest:\n(.*?)Total time for unittest:', contents, re.DOTALL)
    if match:
        unittest_times = match.group(1)
        for line in unittest_times.split('\n'):
            line = line.strip()
            if line:
                parts = line.split(':')
                func_name = parts[0].strip()
                time = float(parts[1].strip().split()[0])
                if func_name in results:
                    results[func_name]['unittest'] = time
                else:
                    results[func_name] = {'unittest': time}

    # Get doctest execution times
    match = re.search(r'doctest:\n(.*?)Total time for doctest:', contents, re.DOTALL)
    if match:
        doctest_times = match.group(1)
        for line in doctest_times.split('\n'):
            line = line.strip()
            if line:
                parts = line.split(':')
                func_name = parts[0].strip()
                time = float(parts[1].strip().split()[0])
                if func_name in results:
                    results[func_name]['doctest'] = time
                else:
                    results[func_name] = {'doctest': time}

    # Get testify execution times
    match = re.search(r'testify:\n(.*?)Total time for testify:', contents, re.DOTALL)
    if match:
        testify_times = match.group(1)
        for line in testify_times.split('\n'):
            line = line.strip()
            if line:
                parts = line.split(':')
                func_name = parts[0].strip()
                time = float(parts[1].strip().split()[0])
                if func_name in results:
                    results[func_name]['testify'] = time
                else:
                    results[func_name] = {'testify': time}
                    
    # Calculate scores for each function
    total_packages = 4  # number de paquetes en este script
    for func_name, times in results.items():
        packages = [pkg for pkg in times.keys()]
        # Si queremos los resultados en fracciones
        #results[func_name]['score']= Fraction(round(len(packages) / total_packages, 2)).limit_denominator()
        results[func_name]['score'] = round(len(packages) / total_packages,2)*100
    return results


results = get_execution_times()

# Write results to file
output= input("enter output file: ")
with open(output, 'w') as f:
    f.write(f"\t --- Test Functions ---  \n")
    for func_name, times in results.items():
        packages = [pkg for pkg in times.keys()]
        if len(packages) > 0:
            score_str = str(times['score'])
            f.write(f"\n{func_name}: {' '.join(packages)} {score_str}%\n".replace('score', '\nScore:'))




