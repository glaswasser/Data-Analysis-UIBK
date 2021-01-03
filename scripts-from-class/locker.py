# Lock
# states: locked and unlocked
# interaction possiblities: using a proper key and turn
# transition rule:
#   1. if using key and state is locked, then state becomes unlocked
#   2. if using key and state is unlocked, then state becomes locked
# starting state: unlocked
# ending state: locked, unlocked, {}


class Lock:

    def turn_lock(self):
        if self.state == 'unlocked':
            self.state = 'locked'
        else:
            self.state = 'unlocked'

    def print_state(self):
        print('The lock is ' + self.state)

    def __init__(self, state):
        self.state = state


my_lock = Lock('unlocked')
my_lock.print_state()
my_lock.turn_lock()
my_lock.print_state()
my_lock.turn_lock()
my_lock.print_state()
