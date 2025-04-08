#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import Float32MultiArray, Float32

def request_node():
    rospy.init_node('Request_node', anonymous=True)
    
    # Получаем аргументы командной строки
    if len(sys.argv) != 4:
        rospy.logerr("Usage: Request_node.py num1 num2 num3")
        return
    
    numbers = list(map(float, sys.argv[1:4]))
    
    # Публикуем числа в Polynomial
    pub = rospy.Publisher('polynomial_input', Float32MultiArray, queue_size=10)
    
    # Ждем подписчиков
    rospy.sleep(1)
    
    # Отправляем числа
    pub.publish(Float32MultiArray(data=numbers))
    rospy.loginfo(f"Sent numbers: {numbers}")
    
    # Ждем результат
    result = rospy.wait_for_message('final_result', Float32)
    rospy.loginfo(f"Final result: {result.data}")
    
    # Завершаем работу
    rospy.signal_shutdown("Request completed")

if __name__ == '__main__':
    request_node()