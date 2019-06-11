import fire

class Calculator(object):
    def double(self, number):
        print(2*number)
        return 2*number
    
if __name__ == 'main':
    fire.Fire(Calculator)