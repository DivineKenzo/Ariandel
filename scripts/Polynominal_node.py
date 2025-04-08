#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float32

def polynomial_callback(data):
    # Получаем массив чисел
    numbers = data.data
    
    # Вычисляем полином: x^1, x^2, x^3 и т.д.
    multiplying = []
    for i, num in enumerate(numbers, start=1):
        multiplying.append(num ** i)
    
    # Публикуем результат
    pub.publish(Float32MultiArray(data=multiplying))
    rospy.loginfo(f"Multiplied polynomial: {multiplying}")

if __name__ == '__main__':
    rospy.init_node('Polynominal_node')
    
    # Публикуем в топик для Summing
    pub = rospy.Publisher('polynomial_results', Float32MultiArray, queue_size=10)
    
    # Подписываемся на топик от Request
    rospy.Subscriber('polynomial_input', Float32MultiArray, polynomial_callback)
    
    rospy.spin()