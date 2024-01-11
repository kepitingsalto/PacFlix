from tabulate import tabulate
from dataclasses import dataclass

@dataclass
class Plan:
    can_stream: bool
    can_download: bool
    has_sd: bool
    has_hd: bool
    has_uhd: bool
    price: int
    num_device: int
    content: str
    plan_name: str
    level: int

    def check_plan(self):
        data = [
        ["Service", self.plan_name],
        ["Streaming", u'\u2713' if self.can_stream else 'x'],
        ["Downloadable", u'\u2713' if self.can_download else 'x'],
        ["Kualitas Standar", u'\u2713' if self.has_sd else 'x'],
        ["Kualitas HD", u'\u2713' if self.has_hd else 'x'],
        ["Kualitas 4K", u'\u2713' if self.has_uhd else 'x'],
        ["Biaya", f"Rp{self.price:,}"],
        ["Maksimal jumlah device", self.num_device],
        ["Kontent", self.content]
        ]
        
        print(tabulate(data, headers = "firstrow"))

basic_plan = Plan(
    can_stream = True,
    can_download = True,
    has_sd = True,
    has_hd = False,
    has_uhd = False,
    price = 120_000,
    num_device = 1,
    content = "3rd movie party",
    plan_name = "Basic Plan",
    level = 1
)

standard_plan = Plan(
    can_stream = True,
    can_download = True,
    has_sd = True,
    has_hd = True,
    has_uhd = False,
    price = 160_000,
    num_device = 2,
    content = "Basic plan + sports",
    plan_name = "Standard Plan",
    level = 2
)

premium_plan = Plan(
    can_stream = True,
    can_download = True,
    has_sd = True,
    has_hd = True,
    has_uhd = True,
    price = 200_000,
    num_device = 4,
    content = "Standard plan + originals",
    plan_name = "Premium Plan",
    level = 3
)