class Mission:
    def __init__(self, name, description, reward, requirements, mission_type):
        self.name = name
        self.description = description
        self.reward = reward
        self.requirements = requirements
        self.mission_type = mission_type

    def display_details(self):
        return f"MISSION: {self.name}\nDESCRIPTION: {self.description}\nREWARD: {self.reward} credits\nTYPE: {self.mission_type}\n"

    def get_choices(self):
        if self.mission_type == "hacking":
            return ["Use brute force", "Use stealth exploit", "Abort"]
        elif self.mission_type == "stealth":
            return ["Sneak in quietly", "Disable security systems", "Abort"]
        elif self.mission_type == "puzzle":
            return ["Try a Caesar cipher", "Use frequency analysis", "Give up"]
        elif self.mission_type == "trace":
            return ["Scan logs", "Use traceroute tool", "Abort"]
        elif self.mission_type == "advanced":
            return ["Deploy AI malware", "Run deep scan", "Abort"]
        elif self.mission_type == "hijack":
            return ["Hack signal tower", "Disrupt controller network", "Abort"]
        elif self.mission_type == "neural":
            return ["Inject logic bomb", "Bypass neural firewall", "Abort"]
        else:
            return ["Abort"]

    def evaluate_choice(self, choice, player_skills):
        if choice == "Abort":
            return False, "You aborted the mission."

        if any(req in player_skills for req in self.requirements):
            return True, f"You chose '{choice}' and executed it successfully using your skills."
        else:
            return False, f"You chose '{choice}' but lacked the necessary skills."
