import frappe

@frappe.whitelist()
def get_status(sales_order_name):
    so = frappe.get_doc("Sales Order", sales_order_name)
    return {
        "name": so.name,
        "status": so.status,
        "docstatus": so.docstatus,
        "grand_total": so.grand_total
    }
