 
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    print('\n')
    tests_passed = 0
    tests_failed = 0

    try:
        tests_passed = len(terminalreporter.stats['passed'])
    except KeyError:
        return

    try:
        tests_failed = len(terminalreporter.stats['failed'])
    except KeyError:
        pass

    assignmentPoints = (tests_passed / (tests_passed + tests_failed)) * 4
    assignmentPoints = round(assignmentPoints, 2)
    print('number of passed tests: ' + str(tests_passed))
    print('number of failed tests: ' + str(tests_failed))
    print('=========================================')
    print('points reached in assignment: ' + str(assignmentPoints))
    print('=========================================')
