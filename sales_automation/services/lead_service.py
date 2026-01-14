import frappe

def create_lead(full_name, phone=None, email=None, requirement=None, source="Website"):
    lead = frappe.get_doc({
        "doctype": "Lead",
        "lead_name": full_name,
        "mobile_no": phone,
        "email_id": email,
        "notes": requirement,
        "source": source
    })
    lead.insert(ignore_permissions=True)
    return lead
