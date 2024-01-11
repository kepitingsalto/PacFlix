from dataclasses import dataclass
from datetime import datetime
from dateutil import relativedelta
from plan import Plan

@dataclass
class User:
    username: str
    plan: Plan
    start_subs: datetime=datetime.now()
    referral: str=None

    def __post_init__(self):
        self.total = self.plan.price
        
    def change_plan(self, new_plan):
        #check if downgrade
        if new_plan.level < self.plan.level:
            print("tidak bisa melakukan downgrade")
            return
        selisih = relativedelta.relativedelta(datetime.now(), self.start_subs)
        
        self.plan = new_plan
        self.start_subs = datetime.now()
        
        discount = 0
        
        if selisih.years > 1 :
            discount = self.plan.price * 0.05
        self.total = self.plan.price - (discount)