import frappe

@frappe.whitelist()
def get_status(quotation_name):
    q = frappe.get_doc("Quotation", quotation_name)
    return {
        "name": q.name,
        "status": q.status,
        "docstatus": q.docstatus,
        "grand_total": q.grand_total
    }
