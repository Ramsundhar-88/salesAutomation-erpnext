import frappe

from sales_automation.config.constants import MAX_DISCOUNT_PERCENT, SALES_MANAGER_ROLE
from sales_automation.services.quotation_service import get_discount_percent, is_discount_allowed
from sales_automation.services.sales_order_service import create_sales_order_from_quotation


def validate(doc, method=None):
    if not is_discount_allowed(doc):
        discount = get_discount_percent(doc)

        if SALES_MANAGER_ROLE not in frappe.get_roles():
            frappe.throw(
                f"Discount {discount}% is above allowed {MAX_DISCOUNT_PERCENT}%. "
                f"{SALES_MANAGER_ROLE} approval required."
            )

def on_submit(doc, method=None):
    create_sales_order_from_quotation(doc)
