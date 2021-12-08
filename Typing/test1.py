# from typing import List
# from pydantic import BaseModel


# class User(BaseModel):
#     first_name: str
#     last_name : str

# db: List[User] = [User( first_name="Jamila",last_name="moo" ),
#                   User( first_name="Jamila1",last_name="moo1" )]

# print(db)

from typing import TypedDict, List

class SalesSummary(TypedDict):
    sales: int
    country: str
    product_codes: List[str]


def get_sales_summary() -> SalesSummary:
    '''Return summary for yesterday’s sales'''
    return {
        "sales": 1_000,
        "country": "UK",
        "product_codes": ["XYZ","ABC","UKN"],
    }


print(get_sales_summary())

# or use ":"
dd : TypedDict=(get_sales_summary())

print(dd)

