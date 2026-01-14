from sales_automation.config.constants import MAX_DISCOUNT_PERCENT


def get_discount_percent(quotation_doc) -> float:
    """
    ERPNext Quotation discount rule based on additional_discount_percentage.
    """
    return float(quotation_doc.get("additional_discount_percentage") or 0)

def is_discount_allowed(quotation_doc) -> bool:
    """
    Discount allowed if <= MAX_DISCOUNT_PERCENT
    """
    return get_discount_percent(quotation_doc) <= MAX_DISCOUNT_PERCENT
