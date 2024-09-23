import json
import os

class StatsManager:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)
    
    def load_stats(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)
    
    def update_stat(self, user_id, phrase):
        stats = self.load_stats()
        if user_id not in stats:
            stats[user_id] = {}
        if phrase not in stats[user_id]:
            stats[user_id][phrase] = 0
        stats[user_id][phrase] += 1
        with open(self.file_path, 'w') as f:
            json.dump(stats, f, indent=4)
