#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float32

def summing_callback(data):
    # Суммируем все числа
    final = sum(data.data)
    
    # Публикуем результат
    pub.publish(Float32(data=final))
    rospy.loginfo(f"Sum calculated: {final}")

if __name__ == '__main__':
    rospy.init_node('Summing_node')
    
    # Публикуем итоговый результат
    pub = rospy.Publisher('final_result', Float32, queue_size=10)
    
    # Подписываемся на топик от Polynomial
    rospy.Subscriber('polynomial_results', Float32MultiArray, summing_callback)
    
    rospy.spin()