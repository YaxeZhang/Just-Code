import threading

class Foo:
    def __init__(self):
        self.condition = threading.Condition()
        self.stage = 1

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        with self.condition:
            self.condition.wait_for(lambda: self.stage == 1)
            printFirst()
            self.stage += 1
            self.condition.notify_all()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.condition:
            self.condition.wait_for(lambda: self.stage == 2)
            printSecond()
            self.stage += 1
            self.condition.notify_all()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.condition:
            self.condition.wait_for(lambda: self.stage == 3)
            printThird()
            self.stage += 1
            self.condition.notify_all()