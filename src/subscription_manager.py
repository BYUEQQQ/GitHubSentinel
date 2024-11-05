import json


class SubscriptionManager:
    def __init__(self, subscriptions_file):
        self.subscriptions_file = subscriptions_file
        self.load_subscriptions()

    def load_subscriptions(self):
        try:
            with open(self.subscriptions_file, 'r') as f:
                self.subscriptions = json.load(f)
        except FileNotFoundError:
            self.subscriptions = []  # 如果文件不存在，返回空列表

    def save_subscriptions(self):
        with open(self.subscriptions_file, 'w') as f:
            json.dump(self.subscriptions, f, indent=4)

    def list_subscriptions(self):
        self.load_subscriptions()  # 每次获取最新订阅
        return self.subscriptions

    def add_subscription(self, repo):
        if repo not in self.subscriptions:
            self.subscriptions.append(repo)
            self.save_subscriptions()
            return f"已添加订阅: {repo}", self.list_subscriptions()  # 确保返回两个值
        return f"订阅已存在: {repo}", self.list_subscriptions()  # 确保返回两个值

    def delete_subscription(self, repo):
        if repo in self.subscriptions:
            self.subscriptions.remove(repo)
            self.save_subscriptions()
            return f"已删除订阅: {repo}", self.list_subscriptions()  # 确保返回两个值
        return f"订阅不存在: {repo}", self.list_subscriptions()  # 确保返回两个值