"""
The template of the main script of the machine learning proces
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        ball_x = scene_info["ball"][0]
        ball_y = scene_info["ball"][1]

        platform_x = scene_info["platform"][0]
        platform_y = scene_info["platform"][0]+40
        if ball_x > platform_y:
            command="MOVE_RIGHT"
        else: 
            if ball_x < platform_x:
                command="MOVE_LEFT"
   

        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"
        else:
            command = "MOVE_LEFT"

        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
