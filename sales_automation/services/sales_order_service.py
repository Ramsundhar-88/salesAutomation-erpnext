import frappe


def create_sales_order_from_quotation(quotation_doc):
    existing = frappe.db.exists("Sales Order", {"quotation": quotation_doc.name})
    if existing:
        return frappe.get_doc("Sales Order", existing)

    customer = quotation_doc.party_name

    so = frappe.get_doc({
        "doctype": "Sales Order",
        "customer": customer,
        "transaction_date": quotation_doc.transaction_date,
        "delivery_date": quotation_doc.get("valid_till"),
        "quotation": quotation_doc.name,
        "items": []
    })

    for item in quotation_doc.items:
        so.append("items", {
            "item_code": item.item_code,
            "qty": item.qty,
            "rate": item.rate
        })

    so.insert(ignore_permissions=True)
    return so
