import frappe
from frappe.utils import add_days, nowdate
from sales_automation.config.constants import REMINDER_DAYS_OLD

def remind_pending_quotations():
    cutoff = add_days(nowdate(), -REMINDER_DAYS_OLD)

    pending = frappe.get_all(
        "Quotation",
        filters={
            "docstatus": 0,
            "transaction_date": ["<=", cutoff]
        },
        fields=["name", "owner"]
    )

    for q in pending:
        frappe.sendmail(
            recipients=[q.owner],
            subject="Reminder: Pending Quotation",
            message=f"Your quotation {q.name} is pending for more than {REMINDER_DAYS_OLD} days."
        )
