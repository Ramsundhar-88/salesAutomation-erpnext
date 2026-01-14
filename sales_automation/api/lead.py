import frappe

from sales_automation.services.lead_service import create_lead


@frappe.whitelist(allow_guest=True)
def create(full_name, phone=None, email=None, requirement=None):
    lead = create_lead(full_name, phone, email, requirement, source="Website")
    return {"status": "success", "lead": lead.name}
