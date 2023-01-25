import random

class Motor:
    def __init__(self):
        self.distance = 0
        
    def forward(self):
        print('앞으로 이동')
        self.distance += 1
        
    def backward(self):
        print('뒤로 이동')
        self.distance -= 1
        
class Robot:
    
    def __init__(self):
        self.motor = Motor()    
        # 포함 관계
        # 한 클래스가 다른 클래스의 멤버로 포함되는 관계
        
    def __str__(self):
        return '이동 한 거리 : {}'.format( self.motor.distance )
    
    
robot = Robot()

for i in range(10):
    if random.randint(0, 1):    # random.randint(0, 1) :  0~1 사이의 랜덤 수
        robot.motor.forward()
    else:
        robot.motor.backward()
        
print(robot)

    
    
    