import json
import os

class StatsManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.stats = self.load_stats()

    def load_stats(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                return json.load(file)
        return {}

    def save_stats(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.stats, file)

    def increment_stat(self, key):
        if key in self.stats:
            self.stats[key] += 1
        else:
            self.stats[key] = 1
        self.save_stats()

    def get_most_selected_phrase(self):
        if not self.stats:
            return None, 0
        return max(self.stats.items(), key=lambda item: item[1])
