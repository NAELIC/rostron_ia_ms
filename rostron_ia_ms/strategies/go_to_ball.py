from .strategies import Strategies

from geometry_msgs.msg import Point, PoseStamped
from rostron_ia_ms.utils.world import World


class GoToBall(Strategies):

    def __init__(self, robot_id):
        super().__init__()
        self.goTo = World().node_.create_publisher(
            PoseStamped, '/yellow/robot_%d/goal_pose' % robot_id, 1)

    def order_robot(self, x, y, theta):
        msg = PoseStamped()
        msg.header.frame_id = 'map'
        msg.pose.position.x = World().ball.position.x
        msg.pose.position.y = World().ball.position.y
        msg.pose.orientation = self.yaw_to_quaternion(0.0)
        self.goTo.publish(msg)

    def update(self):
        # TODO : Remove this !
        if World().ball.position:
            self.order_robot(World().ball.position.x, World().ball.position.x, 0)
            # print("test")
            return True
        else:
            return False