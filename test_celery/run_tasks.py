from .tasks import longtime_add, capital_cities, more_complex, run_simulation
import time

if __name__ == '__main__':
    result = run_simulation.delay(21,'hola')
    # result = capital_cities.delay(China = "Beijing", Slovenia = "Ljubljana", Finland = "Helsinki")
    # result = more_complex.delay(2,6,-12)
    # at this time, our task is not finished, so it will return False
    print ('Task finished? ', result.ready())
    print ('Task result: ', result.result)
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print ('Task finished? ', result.ready())
    print ('Task result: ', result.result)