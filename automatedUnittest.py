import sys, unittest, doctest, pytest, time, os, ast
import matplotlib.pyplot as plt
from testify import *


# select test
def get_choice():
    while True:
        choice = int(input('Test Selection: '))
        if choice in [0,1,2,3,4]:
            return choice
        print('Enter a number between 0 and 4.')


def get_filename():  # Ask user for file nme to test 
    while True:
        filename= input('Enter file name: ')
        if os.path.isfile(filename):
            return filename
        print('Enter CORRECT file name: ')


def run_pytest(filename, times):  #1
    for name in check_functions(filename):
        start_time = time.time() 
        pytest.main(['-v', filename])
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{name}: {execution_time:.3f} seconds")
        times['pytest'].append(execution_time)


def run_unittest(filename, times): #2
    for name in check_functions(filename):
        start_time = time.time() 
        loader = unittest.TestLoader()
        suite  = loader.discover(start_dir='.', pattern=filename)
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{name}: {execution_time:.3f} seconds")
        times['unittest'].append(execution_time)


# doctest does not work yet but the same implementation was used 
# - It works! The problem was with the syntx from the actual test script
def run_doctest(filename, times): #3
    for name in check_functions(filename):
        start_time = time.time()
        doctest.testmod(verbose=True)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{name}: {execution_time:.3f} seconds")
        times['doctest'].append(execution_time)


def run_testify(filename, times): #4 
    for name in check_functions(filename):
        start_time = time.time() 
        loader = unittest.TestLoader()
        suite  = loader.discover(start_dir='.', pattern=filename)
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{name}: {execution_time:.3f} seconds")
        times['testify'].append(execution_time)

def menu():
    print(' [1] pytest')
    print(' [2] unittest')
    print(' [3] doctest')
    print(' [4] testify')
    print(' [0] Exit')


# checks for fucntion names and outputs an array of names
def check_functions(filename):
    with open(filename, "r") as f:
        contents = f.read()
    tree = ast.parse(contents)
    function_names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_names.append(node.name)
    return function_names


def save_results(filename, times, test, txtfile):
    
    function_names = check_functions(filename)
    with open(txtfile, 'a') as f:
        f.write(f"Execution times for {test}:\n")
        
        total_time = 0.0
        for i, time in enumerate(times[test]):
            execution_time = time
            total_time += execution_time
            f.write(f"{function_names[i]}: {execution_time:.3f} seconds\n")
        f.write(f"\nTotal time for {test}: {total_time:.3f} seconds\n\n")
    #return total_time

def plot_execution_time(txtfile):
    pytest_time=0
    unittest_time=0
    doctest_time=0
    testify_time= 0
    
    with open(txtfile, 'r') as f:
        
        for line in f:
            if   'Total time for pytest'  in line:
                pytest_time =   float(line.split(': ')[1].split()[0])
            elif 'Total time for unittest'in line:
                unittest_time=  float(line.split(': ')[1].split()[0])
            elif 'Total time for doctest' in line:
                doctest_time =  float(line.split(': ')[1].split()[0])
            elif 'Total time for testify' in line:
                testify_time =  float(line.split(': ')[1].split()[0])
   
    test_names = ['pytest', 'unittest', 'doctest','testify']
    test_times = [pytest_time, unittest_time, doctest_time,testify_time]
    plt.bar(test_names, test_times)
    plt.xlabel('Test')
    plt.ylabel('Total Execution Time (s)')
    plt.title('Total Execution Time by Test')
    plt.show()

# look up for test in local directory and test it.
def run_tests():
    while True:
        menu()
        choice = get_choice()

        if choice == 1:
            filename = get_filename()
            times = {'pytest':[]}
            run_pytest(filename, times)
            test = 'pytest'
            txtfile = input('Enter output file name: ')
            save_results(filename, times, test, txtfile)
                
        elif choice == 2:
            filename = get_filename()
            times = {'unittest':[]}
            run_unittest(filename, times)
            test = 'unittest'
            txtfile = input('Enter output file name: ')
            save_results(filename, times, test, txtfile)


        elif choice == 3:
            filename = get_filename()
            times = {'doctest':[]}
            run_doctest(filename, times)
            test = 'doctest'
            txtfile = input('Enter output file name: ')
            save_results(filename, times, test, txtfile)

        elif choice == 4:
            filename = get_filename()
            times = {'testify':[]}
            run_testify(filename, times)
            test = 'testify'
            txtfile = input('Enter output file name: ')
            save_results(filename, times, test, txtfile)

        elif choice == 0:
            #txtfile = input("Name of file to be plot: ")
            plot_execution_time(txtfile)
            sys.exit(0)


if __name__ == '__main__':
    run_tests()
    
          