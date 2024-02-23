# -*- coding: utf-8 -*- 


from collections import defaultdict


class CTAnalyzer:
    
    def __init__(self,):
        self.iam_user_field = "userIdentity.arn"
        self.iam_users = defaultdict(int)

    def count_iam_users(self, data: list[dict]):
        for d in data:
            try:
                self.iam_users[d["userIdentity"]["arn"]] += 1
            except Exception as e:
                continue
    



